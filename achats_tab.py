from achats_ventes_tabs import AchatsVentesTabs
from purchase_utils import sqlite_database_columns, sqlite_table_name


class AchatsTab(AchatsVentesTabs):
    def __init__(self, sqlite, mw, tableWidget, comboBox):
        super().__init__(sqlite, mw, sqlite_table_name, sqlite_database_columns, tableWidget, comboBox)
        
        self.supplier_count = 999


        self.tableWidget.itemClicked.connect(self.on_table_item_clicked)
        self.tableWidget.itemSelectionChanged.connect(self.selection_changed)
        self.mw.achatLineEdit.textChanged.connect(self.filter_table_widget)
        self.mw.achatSuivantButton.clicked.connect(self.next)
        self.mw.achatPrecedentButton.clicked.connect(self.previous)
        self.mw.achatSupprimerButton.clicked.connect(self.delete_transaction_record)
        





 
