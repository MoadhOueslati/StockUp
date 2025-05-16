from contact import Contact
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class Clients(Contact, QDialog):
    def __init__(self, sqlite):
        QDialog.__init__(self)
        loadUi("styles/clients.ui", self)
        sqlite_table_name = "Clients"
        sqlite_table_columns = ["client", "phone_number", "address", "email"]
        self.current_client = {
            "name" : "",
            "phone_number" : "",
            "address" : "",
            "email" : "",
        }
        self.client_is_selected = False
        tableWidget = self.clientsTableWidget
        Contact.__init__(self, sqlite, tableWidget, sqlite_table_name, sqlite_table_columns)
