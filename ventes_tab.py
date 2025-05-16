from achats_ventes_tabs import AchatsVentesTabs
from sales_utils import sqlite_database_columns, sqlite_table_name


class VentesTab(AchatsVentesTabs):
    def __init__(self, sqlite, mw, tableWidget, comboBox):
        super().__init__(sqlite, mw, sqlite_table_name, sqlite_database_columns, tableWidget, comboBox)

        self.tableWidget.itemClicked.connect(self.on_table_item_clicked)
        self.tableWidget.itemSelectionChanged.connect(self.selection_changed)
        self.mw.venteLineEdit.textChanged.connect(self.filter_table_widget)
        self.mw.venteSuivantButton.clicked.connect(self.next)
        self.mw.ventePrecedentButton.clicked.connect(self.previous)
        self.mw.venteSupprimerButton.clicked.connect(self.delete_transaction_record)

