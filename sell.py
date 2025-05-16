from sell_style import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from clients import Clients
from sales_utils import sqlite_table_name, sqlite_database_columns
from PyQt5.uic import loadUi
from sales_utils import current_client


class SellWindow(QDialog): #Ui_Dialog
    def __init__(self, sqlite, mw, category=None, product_name=None):
        super().__init__()
        # self.setupUi(self)
        loadUi("styles/sell.ui", self)
        self.sqlite = sqlite
        self.mw = mw
        self.category = category
        self.product_name = product_name

        self.nomProduitLabel.setText(self.product_name)
        self.categorieLabel.setText(self.category)

        self.clients = Clients(self.sqlite)

        self.addClientPushButton.clicked.connect(self.select_client)

        self.enregistrerButton.clicked.connect(self.save_changes)
        self.annulerButton.clicked.connect(self.close_window)

        today_date = self.mw.get_today_date()
        self.dateEntreeLineEdit.setText(today_date)

    def close_window(self):
        self.close()

    def select_client(self):
        self.clients.tableWidget.itemClicked.connect(self.clients.on_table_item_clicked)
        self.clients.update_table()
        self.clients.exec_()
        if self.clients.client_is_selected:
            self.fill_contact_details()


    def fill_contact_details(self):
        self.costumerlineEdit.setText(current_client["name"])
        self.phoneNumberLineEdit.setText(current_client["phone_number"])
        self.addressLineEdit.setText(current_client["address"])
        self.emailLineEdit.setText(current_client["email"])


    def save_changes(self):
        # Insert data to sqlite
        product_data = self.retrieve_purchase_details()

        # Force required selling informations on user
        if int(product_data["quantity_sold"]) == 0 or float(product_data["sale_price"]) == 0.0:
            empty_data_error_msg = f"Veuillez remplir toutes les informations requises."
            self.mw._handle_user_error(empty_data_error_msg)
            return
        
        # Update sqlite total values
        column1 = "quantite_vendue_totale"
        column2 = "total_gagne"
        column3 = "quantite_actuelle"

        select_query = f"SELECT {column1}, {column2}, {column3} FROM {self.mw.sqlite_table_name} WHERE categorie = ? AND nom_du_produit = ?"
        data = self.sqlite.db.fetch_data(select_query, (self.category, self.product_name))

        current_quantity_sold_in_total = int(data[0])
        current_sales_spendings_in_total = float(data[1])
        current_available_quantity = int(data[2])

        # Display Error if the quantity to sell > available quantity
        if int(product_data["quantity_sold"]) > current_available_quantity:
            error_msg = "Vous n'avez pas ce montant."
            self.mw._handle_user_error(error_msg)
            return
        
        # Increasing row id by 1
        self.mw.ventes_tab.rows_count += 1
        record_id = self.mw.ventes_tab.rows_count 
        product_data['record_id'] = record_id

        current_quantity_sold_in_total += int(product_data['quantity_sold'])
        current_sales_spendings_in_total += float(product_data['sale_price'])
        current_available_quantity -= int(product_data['quantity_sold'])

        current_sales_spendings_in_total = round(current_sales_spendings_in_total, 3)

        update_query = f"UPDATE {self.mw.sqlite_table_name} SET {column1} = ?, {column2} = ?, {column3} = ? WHERE categorie = ? AND nom_du_produit = ?"
        self.sqlite.db.insert_data(update_query, (current_quantity_sold_in_total, current_sales_spendings_in_total, current_available_quantity, self.category, self.product_name))

        self.sqlite.insert_data_sqlite(sqlite_table_name, sqlite_database_columns, list(product_data.values()))

        if len(self.costumerlineEdit.text()) != 0:
            self.verify_new_client()

        self.mw.update_profits(self.category, self.product_name)
        self.mw.fill_product_data_to_table()
        self.mw.quantiteActuelleSpinBox.setValue(current_available_quantity)
        self.mw.quantiteVendueTotaleSpinBox.setValue(current_quantity_sold_in_total)

        try:
            # just to appear selected :p
            self.mw.tableWidget.selectRow(self.mw.current_row_count)
        except: pass

        self.close()

    def verify_new_client(self):
        clients = self.sqlite.fetch_data_sqlite("Clients", ["client"])
        client_already_exists = self.costumerlineEdit.text().lower() in [client[0] for client in clients]
        if not client_already_exists : self.add_new_client()

    def add_new_client(self):
        client_data = [
            self.costumerlineEdit.text().lower(),
            self.phoneNumberLineEdit.text(),
            self.addressLineEdit.text(),
            self.emailLineEdit.text()
        ]
        self.sqlite.insert_data_sqlite("Clients", ["client", "phone_number", "address", "email"], client_data)

        self.mw.clientsWindow.rows_count += 1
        
        
    def retrieve_purchase_details(self):
        # Retrieve data from interface
        product_name = self.nomProduitLabel.text()
        quantity_sold = self.quantiteVendueSpinBox.value()
        sale_price = self.prixVendueDoubleSpinBox.value()
        customer = self.costumerlineEdit.text()
        category = self.categorieLabel.text()
        entry_date = self.dateEntreeLineEdit.text()
        notes = self.plainTextEdit.toPlainText()


        product_data = {
            "record_id": None,
            "product_name": product_name,
            "quantity_sold" : quantity_sold,
            "sale_price" : sale_price,
            "customer" : customer,
            "category": category, 
            "entry_date" : entry_date,
            "notes" : notes,
        }
        
        return product_data
    
 
