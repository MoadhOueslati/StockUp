from contact import Contact
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class Fournisseurs(Contact, QDialog):
    def __init__(self, sqlite):
        QDialog.__init__(self)
        loadUi("styles/fournisseurs.ui", self)
        sqlite_table_name = "Fournisseurs"
        sqlite_table_columns = ["fournisseur", "phone_number", "address", "email"]
        self.current_client = {
            "name" : "",
            "phone_number" : "",
            "address" : "",
            "email" : "",
        }
        self.fournisseur_is_selected = False
        tableWidget = self.fournisseursTableWidget
        Contact.__init__(self, sqlite, tableWidget, sqlite_table_name, sqlite_table_columns)
