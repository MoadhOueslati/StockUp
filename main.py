import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QDialog, QDesktopWidget, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QPixmap, QColor, QIcon
from PyQt5.QtCore import QTimer
from database import Sqlite
from buy import BuyWindow
from sell import SellWindow
from achats_tab import AchatsTab
from ventes_tab import VentesTab
from clients import Clients
from fournisseurs import Fournisseurs
from category_settings import CategorieSettings
from publish import Publish
import interface_images
from datetime import date, datetime
from PyQt5.uic import loadUi
from main_style import Ui_MainWindow
from freemium_over import Ui_Dialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class MainWindow(QMainWindow):  # Ui_MainWindow
    def __init__(self):
        super().__init__()
        loadUi("styles/main.ui", self)

        # Create a QWebEngineView instance
        self.browser = QWebEngineView()
        
        # Set the QWebEngineView as the widget of youtubeWidget
        self.youtubeWidget.setLayout(QVBoxLayout())
        self.youtubeWidget.layout().addWidget(self.browser)


        video_url = "https://youtu.be/Wh-0FcxP-kU"
        self.browser.load(QUrl(video_url))


        self.achatModifierButton.setVisible(False)
        self.venteModifierButton.setVisible(False)

        # self.setupUi(self)
        self.sqlite = Sqlite()
        self.sqlite_table_name = "Products"

        self.columns_to_fetch_data_from = [
            'nom_du_produit',
            'quantite_actuelle',
            'quantite_achetee_totale',
            'quantite_vendue_totale',
            'total_depense',
            'total_gagne',
            'benefices',
            'categorie',
            'date_dentree',
            'notes',
            'benefices'
        ]
                  
        self.sqlite_database_columns = [
            'nom_du_produit',
            'quantite_actuelle',
            'quantite_achetee_totale',
            'quantite_vendue_totale',
            'categorie',
            'prix_achat',
            'prix_vente',
            'date_dentree',
            'notes',
            'image_path',
            'total_depense',
            'total_gagne',
            'benefices'
        ]

        self.current_product_data = None

        self.acheteeButton.setVisible(False) 
        self.vendueButton.setVisible(False)

        today_date = self.get_today_date()
        self.dateEntreeLineEdit.setText(today_date)

        self.buy_window = BuyWindow(self.sqlite, self)
        self.sell_window = SellWindow(self.sqlite, self)

        self.tableWidget.itemClicked.connect(self.on_table_item_clicked)
        self.tabWidget.currentChanged.connect(self.on_tab_changed)

        self.tableWidget.itemSelectionChanged.connect(self.selection_changed)

        self.searchLineEdit.textChanged.connect(self.filter_table_widget)

        # Fills category combo boxes
        self.update_category_combos()

        self.categorieFilterComboBox.currentTextChanged.connect(self.sort_categorie)


        self.ajouterCategorieButton.clicked.connect(self.open_categories_window)

        

        self.selection_enabled = False
        self.supprimerButton.clicked.connect(lambda: self.delete(self.tableWidget, self.sqlite_table_name, self.selection_enabled)) 

        # Purchase and Sell buttons
        self.acheteeButton.clicked.connect(self.open_buy_window)
        self.vendueButton.clicked.connect(self.open_sell_window)

        # Left Container Buttons
        self.ajouterImageButton.clicked.connect(self.insert_image)
        
        self.selected_image_path = None
        self.current_row_count = -1
        self.searched_categorie = "----------TOUT----------"

        self.achats_tab = AchatsTab(self.sqlite, self, self.achatTableWidget, self.achatComboBox)
        self.ventes_tab = VentesTab(self.sqlite, self, self.venteTableWidget, self.venteComboBox)

        self.achats_tab.update_table()   # <--- maybe put these two inside the achats_ventes_tab in init methode instead ?
        self.ventes_tab.update_table()   # <---

        self.clientsWindow = Clients(self.sqlite)
        self.clientsWindow.update_table()    

        self.fournisseursWindow = Fournisseurs(self.sqlite)
        self.fournisseursWindow.update_table()    

        self.fill_product_data_to_table()
        self.tableWidget.resizeColumnsToContents()

        self.product_name_column_number = 0
        self.category_column_number = 7

        # DashBoard Buttons
        self.clientsPushButton.clicked.connect(self.open_clients)
        self.fournisseursPushButton.clicked.connect(self.open_fournisseurs)
        self.achatsButton.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.ventesButton.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))
        # Bottom Buttons
        self.nouveauButton.clicked.connect(self.refresh_product_entry)
        self.enregistrerButton.clicked.connect(self.save)
        self.precedentButton.clicked.connect(self.previous)
        self.suivantButton.clicked.connect(self.next)
        self.modifierButton.clicked.connect(self.modify)
        self.annulerButton.clicked.connect(self.cancel)

        self.start_number_animation()

        self.publish_window = None

    def filter_table_widget(self, text):
        self.refresh_product_entry()
        column_index = 0
        # Filter the rows based on the search input
        items = self.sqlite.fetch_data_sqlite(self.sqlite_table_name, self.columns_to_fetch_data_from)
        filtered_items = [item for item in items if item[column_index].lower().startswith(text.lower())]

        # Clear the current rows in the table and repopulate it with filtered items
        self.tableWidget.clearContents()
        self.fill_product_data_to_table(filtered_items)
    

    def open_clients(self):
        self.clientsWindow = Clients(self.sqlite)
        self.clientsWindow.update_table()
        self.clientsWindow.exec_()

    def open_fournisseurs(self):
        self.fournisseursWindow = Fournisseurs(self.sqlite)
        self.fournisseursWindow.update_table()
        self.fournisseursWindow.exec_()
    
    def start_number_animation(self):
        # dashboard_data = self.get_dashboard_data()  useless pprobs
        client_count = self.clientsWindow.rows_count
        supplier_count = self.fournisseursWindow.rows_count
        purchases_count = self.achats_tab.rows_count
        sales_count = self.ventes_tab.rows_count
        total_benefices = self.get_total_benefices()
        total_gagnes = self.get_total_gagne()
        total_depenses = self.get_total_depense()
        # Upper cards
        self.total_benefices_animation = NumberAnimation(self.beneficesLabel, total_benefices, False)
        self.total_gagnes_animation = NumberAnimation(self.recettesLabel, total_gagnes, False)
        self.total_depeses_animation = NumberAnimation(self.depensesLabel, total_depenses, False)
        # Bottom cards
        self.clients_number_animation = NumberAnimation(self.clientsLabel, client_count)
        self.fournisseurs_number_animation = NumberAnimation(self.fournisseursLabel, supplier_count)
        self.achats_number_animation = NumberAnimation(self.achatsLabel, purchases_count)
        self.ventes_number_animation = NumberAnimation(self.ventesLabel, sales_count)

    def get_total_benefices(self):
        return self._get_total("benefices")
    
    def get_total_gagne(self):
        return self._get_total("total_gagne")
    
    def get_total_depense(self):
        return self._get_total("total_depense")
    
    def _get_total(self, column_name):
        data_list = self.sqlite.fetch_data_sqlite("Products", [column_name])
        return round(sum(float(value[0]) for value in data_list), 3)


    def resizeEvent(self, event):
        pass
        # width = self.width()
        # height = self.height()
        # # print(width, height)

    def open_buy_window(self):
        self.buy_window = BuyWindow(self.sqlite, self, self.current_product_data["category"], self.current_product_data["product_name"])
        if self.selected_image_path is None:
            pass
        else:
            self.buy_window.imageLabel.setPixmap(QPixmap(self.selected_image_path))
        self.buy_window.exec_()

    def open_sell_window(self):
        self.sell_window = SellWindow(self.sqlite, self, self.current_product_data["category"], self.current_product_data["product_name"])
        if self.selected_image_path is None:
            pass
        else:
            self.sell_window.imageLabel.setPixmap(QPixmap(self.selected_image_path))
        self.sell_window.exec_()

    def fetch_all_data_by_column_name(self, table_name, column_name):
        # Retrieve All Categories
        sqlite_table_name = table_name
        column_to_fetch_data_from = column_name
        select_query = f"SELECT {column_to_fetch_data_from} FROM {sqlite_table_name}"
        data = self.sqlite.db.fetch_all_data(select_query)
        data = [category[0] for category in data]
        return data

    def open_categories_window(self):
        categories = self.fetch_all_data_by_column_name("Categories", "category")
        self.categories_window = CategorieSettings(self, self.sqlite, categories) 
        self.categories_window.exec_()


    def _handle_user_error(self, msg):
        QMessageBox.warning(None, "ERROR 303", msg)

    def on_tab_changed(self, index):
        self.tab_text = self.tabWidget.tabText(index)
        if self.tab_text == "Accueil":
            # self.update_dashboard_data()
            self.start_number_animation()
        elif self.tab_text == "Produits":
            self.searchLineEdit.clear()
            self.categorieFilterComboBox.setCurrentText("----------TOUT----------")
            # just to appear selected :p
            try:
                self.tableWidget.selectRow(self.current_row_count)
            except: pass

        elif self.tab_text == "Achats":
            self.achats_tab.update_table()
            self.achatLineEdit.clear()
            self.achatComboBox.setCurrentText("Nom du Produit")
            try:
            # just to appear selected :p
                self.achatTableWidget.selectRow(self.achats_tab.current_row_count)
            except: pass
        elif self.tab_text == "Ventes":
            self.ventes_tab.update_table()
            self.venteLineEdit.clear()
            self.venteComboBox.setCurrentText("Nom du Produit")
            try:
            # just to appear selected :p
                self.venteTableWidget.selectRow(self.ventes_tab.current_row_count)
            except: pass

        elif self.tab_text == "Annoncer":
            if self.publish_window == None:
                self.publish_window = Publish(self)
            self.publish_window.email_worker.refresh_list()


    def refresh_product_entry(self):
        # Reset the current row and the selection mode 
        self.current_row_count = -1
        self.tableWidget.clearSelection()

        # Clear the products Entry
        # self.searchLineEdit.clear()
        self.nomProduitLineEdit.setText("")
        self.prixAchatSpinBox.setValue(0)
        self.prixVenteSpinBox.setValue(0)
        self.categorieComboBox.setCurrentText("Non catégorisé")
        self.quantiteAchatTotaleSpinBox.setValue(0)
        self.quantiteActuelleSpinBox.setValue(0)
        self.quantiteVendueTotaleSpinBox.setValue(0)
        self.plainTextEdit.clear()
        self.productPictureLabel.setPixmap(QPixmap("pictures/photo.jpg"))
        self.selected_image_path = None

        today_date = self.get_today_date()
        self.dateEntreeLineEdit.setText(today_date)

                  
        self.acheteeButton.setVisible(False) 
        self.vendueButton.setVisible(False)

    def product_is_unique(self, data_tuple):   
        unique = True
        query = "SELECT categorie, nom_du_produit FROM Products"
        data = self.sqlite.db.fetch_all_data(query)
        data_length = len(data)
        count = 0
        while unique == True and count < data_length:
            unique = data[count] != data_tuple
            count += 1
        return unique

    def retrieve_product_details(self):
        # Retrieve data from interface
        product_name = self.nomProduitLineEdit.text()
        category = self.categorieComboBox.currentText()
        # This case if he has 0 categories
        if category == "": 
            category = "Non catégorisé"
        total_quantity_purchased = self.quantiteAchatTotaleSpinBox.value()
        quantity_current = self.quantiteActuelleSpinBox.value()
        total_quantity_sold = self.quantiteVendueTotaleSpinBox.value()
        selling_price = self.prixVenteSpinBox.value()
        buying_price = self.prixAchatSpinBox.value()
        entry_date = self.dateEntreeLineEdit.text()
        notes = self.plainTextEdit.toPlainText()
        image_path = self.selected_image_path

        product_data = {
            "product_name" : product_name,
            "total_quantity_purchased" : total_quantity_purchased,
            "quantity_current" : quantity_current,
            "total_quantity_sold" : total_quantity_sold,
            "category" : category,
            "buying_price": buying_price,
            "selling_price": selling_price,
            "entry_date" : entry_date,
            "notes" : notes,
            "image_path" : image_path,
            "benefices" : 0
        }

        return product_data


    def reassign_row_ids(self, sqlite_table_name):  
        # Fetch existing rowids from the SQLite table
        fetch_query = f"SELECT rowid FROM {sqlite_table_name}"
        existing_rowids = self.sqlite.db.fetch_all_data(fetch_query)

        existing_rowids = [row[0] for row in existing_rowids]

        
        for index, rowid in enumerate(existing_rowids):
            new_id = index + 1
            
            query = f"UPDATE {sqlite_table_name} SET record_id = ? WHERE rowid = ?"
            self.sqlite.db.cursor.execute(query, (new_id, rowid))

        if sqlite_table_name == "Purchases":
            self.achats_tab.update_table()
            self.achatLineEdit.clear()
        elif sqlite_table_name == "Sales":
            self.ventes_tab.update_table()
            self.venteLineEdit.clear()

        
        self.sqlite.db.connection.commit()


    def modify(self):
        if self.selection_enabled == True:
            warning_message = f'Êtes-vous sûr de vouloir appliquer les modifications ?'
            reply = QMessageBox.question(
            self,
            "Modifier le produit",
            warning_message,
            QMessageBox.Ok | QMessageBox.Cancel,  
            QMessageBox.Cancel
            )
            if reply == QMessageBox.Ok:
                entry_check = self.entry_check("modify")
                if entry_check == False: return
                product_data = self.retrieve_product_details()
                update_query = f"""
                    UPDATE Products 
                    SET categorie=?, nom_du_produit=?, prix_vente=?, prix_achat=?, quantite_actuelle=?, quantite_achetee_totale=?, quantite_vendue_totale=?, notes=?, image_path=?
                    WHERE categorie=? AND nom_du_produit=?
                """
                self.sqlite.db.insert_data(update_query, (product_data["category"], product_data["product_name"], product_data["selling_price"], product_data["buying_price"], product_data["quantity_current"], product_data["total_quantity_purchased"], product_data["total_quantity_sold"], product_data["notes"], product_data["image_path"], self.current_product_data["category"], self.current_product_data["product_name"]))
                self.fill_product_data_to_table()
                self.current_product_data = self.retrieve_product_details()
            else:
                pass
        else:
            select_to_delete_message = "Veuillez sélectionner le produit que vous souhaitez modifier."
            self._handle_user_error(select_to_delete_message)
        
    def entry_check(self, method=None):
        product_data = self.retrieve_product_details()

        if not self.product_is_unique((product_data["category"], product_data["product_name"])):
            if not(method == "modify" and (product_data["product_name"] == self.current_product_data["product_name"] and self.current_product_data["category"] == product_data["category"])):
                unique_error_msg = f"Un produit existe déjà avec le nom ({product_data['product_name']}) dans la catégorie ({product_data['category']}) !"
                self._handle_user_error(unique_error_msg)
                return False

        # Force required product informations on user
        if len(product_data["product_name"]) == 0 or product_data["buying_price"] == 0.0 or product_data["selling_price"] == 0.0:
            empty_data_error_msg = f"Veuillez remplir toutes les informations requises."
            self._handle_user_error(empty_data_error_msg)
            return False
        
    def save(self):
        product_data = self.retrieve_product_details()
        product_data["total_sales"] = 0
        product_data["total_gains"] = 0

        entry_check = self.entry_check()
        if entry_check == False: return

        self.sqlite.insert_data_sqlite(self.sqlite_table_name, self.sqlite_database_columns, list(product_data.values()))

        self.fill_product_data_to_table()

        self.refresh_product_entry()
        self.tableWidget.selectRow(self.current_row_count)

    def sort_categorie(self):
        self.searched_categorie = self.categorieFilterComboBox.currentText()
        self.refresh_product_entry()
        self.fill_product_data_to_table()

    def fill_product_data_to_table(self, data=None):
        # Fetch All data from sqlite db then insert it to product details tab
        if data is None:
            # Fetch data sqlite
            data = self.sqlite.fetch_data_sqlite(self.sqlite_table_name, self.columns_to_fetch_data_from)

        # Insert all data into the table widget
        self.tableWidget.setRowCount(0)
        row_count = len(data)
        column_count = len(self.columns_to_fetch_data_from)

        row_index = 0
        row_index_sorted = 0

        while row_index < row_count:
            if data[row_index][7] == self.searched_categorie or self.searched_categorie == "----------TOUT----------":
                self.tableWidget.insertRow(row_index_sorted)
                for i in range(column_count):
                    self.tableWidget.setItem(row_index_sorted, i, QTableWidgetItem(str(data[row_index][i])))
                row_index_sorted += 1
            row_index += 1

        self.update_profit_colors()

        # self.current_row_count = -1  #this line is useless as far as i know if you get an error someday remove the comment maybe :D
        self.tableWidget.resizeColumnsToContents()
    
    def update_category_combos(self):
        top_text_search_category = "----------TOUT----------"
        top_text_selected_category = "Non catégorisé"
        table_name = "Categories"
        column_name = "category"
        categories = self.fetch_all_data_by_column_name(table_name, column_name)
        search_categories = categories + [top_text_search_category]
        selection_categories = categories + [top_text_selected_category]

        # Select category combo box
        self.categorieComboBox.clear()
        self.categorieComboBox.addItems(selection_categories)

        # Search category combo box
        self.categorieFilterComboBox.clear()
        self.categorieFilterComboBox.addItems(search_categories)
        self.categorieFilterComboBox.setCurrentText(top_text_search_category)


    def previous(self):
        if self.current_row_count <= 0:
            self.current_row_count = self.tableWidget.rowCount()
            if self.tableWidget.rowCount() == 0:  # if there are no products at all disable previous
                return

        self.current_row_count -= 1
        self.tableWidget.selectRow(self.current_row_count)
        self.acheteeButton.setVisible(True) 
        self.vendueButton.setVisible(True)
        self.fill_product_details(self.current_row_count)

    def next(self):
        if self.current_row_count >= self.tableWidget.rowCount()-1:
            self.current_row_count = -1
            if self.tableWidget.rowCount() == 0:  # if there are no products at all disable next
                return
        
        self.current_row_count += 1
        self.tableWidget.selectRow(self.current_row_count)
        self.acheteeButton.setVisible(True) 
        self.vendueButton.setVisible(True)
        self.fill_product_details(self.current_row_count)

    def cancel(self):
        self.searchLineEdit.clear()
        if self.selection_enabled:
            self.fill_product_details(self.current_row_count)


    def delete(self, table_widget, sqlite_table_name, selection_enabled):
            # By default 0 & 7 for the product table widget
            if selection_enabled == True:
                try:
                    if table_widget == self.tableWidget:
                        product_name = table_widget.item(self.current_row_count, self.product_name_column_number).text()
                        category = table_widget.item(self.current_row_count, self.category_column_number).text()
                        # Confirm deletion
                        reply = QMessageBox.question(self, 'Confirmer la Suppression.', 
                                                        f"Êtes-vous sûr de vouloir supprimer le produit '{product_name}' de la catégorie '{category}' ?",
                                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                        if reply == QMessageBox.Yes:
                            deleting_query = f"DELETE FROM {sqlite_table_name} WHERE nom_du_produit = ? AND categorie = ?"
                            self.sqlite.db.delete_data(deleting_query, (product_name, category))
                            table_widget.removeRow(self.current_row_count)
                            table_widget.clearSelection()
                            self.refresh_product_entry()

                    elif table_widget == self.achatTableWidget:   
                        record_id = table_widget.item(self.achats_tab.current_row_count, 0).text()
                        # Confirm deletion
                        reply = QMessageBox.question(self, 'Confirmer la Suppression.', 
                                                        f"Are sure you want to delete the purchase record where id = {record_id} ? ",
                                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                        if reply == QMessageBox.Yes:
                            return True
                            
                    elif table_widget == self.venteTableWidget:   
                        record_id = table_widget.item(self.ventes_tab.current_row_count, 0).text()
                        # Confirm deletion
                        reply = QMessageBox.question(self, 'Confirmer la Suppression.', 
                                                        f"Are sure you want to delete the sale record where id = {record_id} ? ",
                                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                        if reply == QMessageBox.Yes:
                            return True

                except: 
                    pass
            else:
                select_to_delete_message = "Veuillez sélectionner le produit que vous souhaitez supprimer."
                self._handle_user_error(select_to_delete_message)

        

    def delete_by_category(self, category):
        deleting_query = f"DELETE FROM {self.sqlite_table_name} WHERE categorie = ?"
        self.sqlite.db.delete_data(deleting_query, (category,))
        self.refresh_product_entry()


    def insert_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        if file_name:
            self.productPictureLabel.setPixmap(QPixmap(file_name))
            self.selected_image_path = file_name

    def fill_product_details(self, current_row_count):
        try:
            selected_row_data = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(current_row_count, column)
                selected_row_data.append(item.text())
            
            self.nomProduitLineEdit.setText(selected_row_data[0])
            self.quantiteActuelleSpinBox.setValue(int(selected_row_data[1]))
            self.quantiteAchatTotaleSpinBox.setValue(int(selected_row_data[2]))
            self.quantiteVendueTotaleSpinBox.setValue(int(selected_row_data[3]))
            self.categorieComboBox.setCurrentText(selected_row_data[7])
            self.dateEntreeLineEdit.setText(selected_row_data[8])
            self.plainTextEdit.setPlainText(selected_row_data[9])

            # Fetch product buying & selling price then display it 
            query = "SELECT prix_vente, prix_achat FROM Products WHERE categorie=? AND nom_du_produit=?" 
            prix_achat_vente = self.sqlite.db.fetch_all_data(query, (selected_row_data[7], selected_row_data[0]))[0]
            
            prix_vente = prix_achat_vente[0]
            prix_achat = prix_achat_vente[1]

            self.prixVenteSpinBox.setValue(prix_vente)
            self.prixAchatSpinBox.setValue(prix_achat)

            # Fetch picture path from sqlite db
            query = "SELECT image_path FROM Products WHERE categorie = ? AND nom_du_produit = ?"
            self.selected_image_path = self.sqlite.db.fetch_data(query, (selected_row_data[7], selected_row_data[0]))[0]
            
            if self.selected_image_path is None:
                self.productPictureLabel.setPixmap(QPixmap("pictures/photo.jpg")) 
            else:
                self.productPictureLabel.setPixmap(QPixmap(self.selected_image_path)) 
            
            self.current_product_data = self.retrieve_product_details()
        except:
            pass

    def selection_changed(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            self.selection_enabled = True
        else:
            self.selection_enabled = False  
            self.current_row_count = -1

    def on_table_item_clicked(self, item):
        self.current_row_count = item.row()
        self.fill_product_details(self.current_row_count)
        self.acheteeButton.setVisible(True) 
        self.vendueButton.setVisible(True)
        
    def closeEvent(self, event): 
        self.sqlite.db.close_connection()
        event.accept()
        
    def update_profits(self, category, product_name):
        select_query = f"SELECT benefices, total_depense, total_gagne FROM {self.sqlite_table_name} WHERE categorie = ? AND nom_du_produit = ?"
        data = self.sqlite.db.fetch_data(select_query, (category, product_name))

        benefices = data[0]
        total_depense = data[1]
        total_gagne = data[2]

        benefices = round(total_gagne - total_depense, 3)

        update_query = f"UPDATE {self.sqlite_table_name} SET benefices = ? WHERE categorie = ? AND nom_du_produit = ?"
        self.sqlite.db.insert_data(update_query, (benefices, category, product_name))

        self.update_profit_colors()


    def update_profit_colors(self):
        category_column_index = 6
        category_target = "Bénéfices"
        for column_index in range(self.tableWidget.columnCount()):
            if self.tableWidget.horizontalHeaderItem(column_index).text() == category_target: 
                for row_index in range(self.tableWidget.rowCount()):
                    profit = self.tableWidget.item(row_index, category_column_index)
                    # Checking if the profit is good or nah
                    if float(profit.text()) > 0:
                        profit.setBackground(QColor(134, 255, 120))
                    elif float(profit.text()) < 0:
                        profit.setBackground(QColor(255, 82, 85))
                    elif float(profit.text()) == 0:
                        profit.setBackground(QColor(190, 190, 190))
            else:
                for row_index in range(self.tableWidget.rowCount()):
                    item = self.tableWidget.item(row_index, column_index)
                    try:
                        item.setBackground(QColor(190, 190, 190))
                    except:
                        pass
    
    def get_today_date(self):
        today = datetime.today()
        formatted_date = today.strftime("%d/%m/%Y")
        return formatted_date
    

        
class NumberAnimation:
    """
    This animation sucks af
    fix
    it
    fast
    """
    def __init__(self, label, number, animate=True):
        self.label = label
        self.number = number
        interval = 0
        if animate:
            if  0 <= self.number <= 50:
                    self.counter = 0
                    interval = 30
            elif 50 < self.number < 100:
                self.counter = 0
                interval = 15
            else: 
                self.counter = self.number - 100
                interval = 1
        else:
            self.counter = self.number
            interval = 1
    
        self.timer = QTimer()
        self.timer.timeout.connect(self.increase_number)
        self.timer.start(interval)  
    
    def increase_number(self):
        self.label.setText(str(self.counter))
        if self.counter >= self.number:
            self.timer.stop()
        self.counter += 1


class Freemium:
    def __init__(self, mainwindow):
        self.sqlite = Sqlite()
        self.mw = mainwindow
        self.start_date_table_name = "emit"
        self.today_date = None
        self.start_date = None
        self.end_date = None
        self.freemium_is_over = False
        self.warning_not_mentioned = True
        self.today_date = date.today()
        self.store_start_date(self.start_date_table_name)
        self.timer = QTimer()
        self.check_if_freemium_is_over()
        self.timer.timeout.connect(self.check_if_freemium_is_over)
        self.timer.start(1000000)

    def check_if_freemium_is_over(self):
        self.freemium_is_over = self.check_freemium_plan(self.start_date, self.today_date)
        if self.freemium_is_over and self.warning_not_mentioned:
            self.mw.setEnabled(False)
            freeOverWindow = FreeOver()
            freeOverWindow.show()
            freeOverWindow.exec_()
            self.warning_not_mentioned = False
        else: 
            pass
    
    def store_start_date(self, table_name):
        query = f"SELECT {table_name} FROM Emit"
        self.start_date = self.sqlite.db.fetch_data(query)[0]
        if self.start_date is None:
            self.start_date = self.today_date
            query = f"""UPDATE Emit
                        SET {table_name} = ?
                        """
            self.start_date = self.encrypt(str(self.start_date))
            self.sqlite.db.insert_data(query, (self.start_date,))
        else: 
            pass
        self.start_date = self.decrypt(str(self.start_date))

    
    def check_freemium_plan(self, start_date, today_date):
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        date_difference = today_date - start_date
        days_between = date_difference.days

        query = "SELECT syad FROM Emit"
        freemium_period = self.sqlite.db.fetch_data(query)[0]
        freemium_period = freemium_period // (28 * 12 * 2002)

        return days_between < freemium_period
    
    def encrypt(self, text):
        encrypted_text = ""
        for letter in text:
            encrypted_text += chr(ord(letter) + 19)
        return encrypted_text

    def decrypt(self, text):
        dycrypted_text = ""
        for letter in text:
            dycrypted_text += chr(ord(letter) - 19)
        return dycrypted_text


class FreeOver(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        # loadUi("styles/freemium_over.ui", self)
        self.setupUi(self)

        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QIcon('diamond.png'))
    window.resize(1580, 880)
    # Centering the window on the screen
    screen = QDesktopWidget().screenGeometry()
    x = (screen.width() - window.width()) // 2
    y = 0
    window.move(x, y)
    freemium = Freemium(window)
    sys.exit(app.exec_())
