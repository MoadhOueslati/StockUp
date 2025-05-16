from buy_style import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from fournisseurs import Fournisseurs
from purchase_utils import sqlite_table_name, sqlite_database_columns
from PyQt5.uic import loadUi
from purchase_utils import current_supplier




class BuyWindow(QDialog): #Ui_Dialog
    def __init__(self, sqlite, mw, category=None, product_name=None):
        super().__init__()
        # self.setupUi(self)
        loadUi("styles/buy.ui", self)
        self.sqlite = sqlite
        self.mw = mw
        self.category = category
        self.product_name = product_name
        self.nomProduitLabel.setText(self.product_name)
        self.categorieLabel.setText(self.category)

        self.fournisseurs = Fournisseurs(self.sqlite)

        self.addFournisseurPushButton.clicked.connect(self.select_fournisseur)


        self.enregistrerButton.clicked.connect(self.save_changes)
        self.annulerButton.clicked.connect(self.close_window)


        today_date = self.mw.get_today_date()
        self.dateEntreeLineEdit.setText(today_date)
    
    def close_window(self):
        self.close()

    def select_fournisseur(self):
        self.fournisseurs.tableWidget.itemClicked.connect(self.fournisseurs.on_table_item_clicked)
        self.fournisseurs.update_table()
        self.fournisseurs.exec_()
        if self.fournisseurs.fournisseur_is_selected:
            self.fill_contact_details()


    def fill_contact_details(self):
        self.fournisseurLineEdit.setText(current_supplier["name"])
        self.phoneNumberLineEdit.setText(current_supplier["phone_number"])
        self.addressLineEdit.setText(current_supplier["address"])
        self.emailLineEdit.setText(current_supplier["email"])



    def save_changes(self):
        # Insert data to sqlite
        product_data = self.retrieve_purchase_details()

        # Force required buying informations on user
        if int(product_data["quantity_purchased"]) == 0 or float(product_data["purchase_price"]) == 0.0:
            empty_data_error_msg = f"Veuillez remplir toutes les informations requises."
            self.mw._handle_user_error(empty_data_error_msg)
            return
        
        # Increasing row id by 1
        self.mw.achats_tab.rows_count += 1
        record_id = self.mw.achats_tab.rows_count 
        product_data['record_id'] = record_id

        
        self.sqlite.insert_data_sqlite(sqlite_table_name, sqlite_database_columns, list(product_data.values()))

        # Update sqlite total values
        column1 = "quantite_achetee_totale"
        column2 = "total_depense"
        column3 = "quantite_actuelle"

        select_query = f"SELECT {column1}, {column2}, {column3} FROM {self.mw.sqlite_table_name} WHERE categorie = ? AND nom_du_produit = ?"
        data = self.sqlite.db.fetch_data(select_query, (self.category, self.product_name))

        current_quantity_purchased_in_total = int(data[0])
        current_purchase_spendings_in_total = float(data[1])
        current_available_quantity = int(data[2])

        current_quantity_purchased_in_total += int(product_data['quantity_purchased'])
        current_purchase_spendings_in_total += float(product_data['purchase_price'])
        current_available_quantity += int(product_data['quantity_purchased'])

        current_purchase_spendings_in_total = round(current_purchase_spendings_in_total, 3)

        update_query = f"UPDATE {self.mw.sqlite_table_name} SET {column1} = ?, {column2} = ?, {column3} = ? WHERE categorie = ? AND nom_du_produit = ?"
        self.sqlite.db.insert_data(update_query, (current_quantity_purchased_in_total, current_purchase_spendings_in_total, current_available_quantity, self.category, self.product_name))

        if len(self.fournisseurLineEdit.text()) != 0:
            self.verify_new_fournisseur()

        self.mw.update_profits(self.category, self.product_name)
        self.mw.fill_product_data_to_table()
        self.mw.quantiteActuelleSpinBox.setValue(current_available_quantity)
        self.mw.quantiteAchatTotaleSpinBox.setValue(current_quantity_purchased_in_total)

        try:
            # just to appear selected :p
            self.mw.tableWidget.selectRow(self.mw.current_row_count)
        except: pass

        self.close()

    def verify_new_fournisseur(self):
        fournisseurs = self.sqlite.fetch_data_sqlite("Fournisseurs", ["fournisseur"])
        fournisseur_already_exists = self.fournisseurLineEdit.text().lower() in [fournisseur[0] for fournisseur in fournisseurs]
        if not fournisseur_already_exists : self.add_new_fournisseur()

    def add_new_fournisseur(self):
        fournisseur_data = [
            self.fournisseurLineEdit.text().lower(),
            self.phoneNumberLineEdit.text(),
            self.addressLineEdit.text(),
            self.emailLineEdit.text()
        ]
        self.sqlite.insert_data_sqlite("Fournisseurs", ["fournisseur", "phone_number", "address", "email"], fournisseur_data)

        self.mw.fournisseursWindow.rows_count += 1
        

    def retrieve_purchase_details(self):
        # Retrieve data from interface
        product_name = self.nomProduitLabel.text()
        quantity_purchased = self.quantiteAchatSpinBox.value()
        purchase_price = self.prixAchatDoubleSpinBox.value()
        supplier = self.fournisseurLineEdit.text()
        category = self.categorieLabel.text()
        entry_date = self.dateEntreeLineEdit.text()
        notes = self.plainTextEdit.toPlainText()

        product_data = {
            "record_id": None,
            "product_name": product_name,
            "quantity_purchased" : quantity_purchased,
            "purchase_price" : purchase_price,
            "supplier" : supplier,
            "category": category, 
            "entry_date" : entry_date,
            "notes" : notes,
        }
        
        return product_data