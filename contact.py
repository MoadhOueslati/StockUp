from PyQt5.QtWidgets import QTableWidgetItem
from sales_utils import current_client
from purchase_utils import current_supplier

class Contact:
    def __init__(self, sqlite, tableWidget, sqlite_table_name, sqlite_table_columns):
        self.sqlite = sqlite
        self.tableWidget = tableWidget
        self.sqlite_table_name = sqlite_table_name
        self.sqlite_table_columns = sqlite_table_columns
        self.rows_count = 0


    def on_table_item_clicked(self, item):
        selected_row = item.row()
        row_data = []
        for column_index in range(len(self.sqlite_table_columns)):
            item = self.tableWidget.item(selected_row, column_index)
            row_data.append(item.text())

        # for filling the sell window inputs
        if self.sqlite_table_name == "Clients":
            current_client["name"] = row_data[0]
            current_client["phone_number"] = row_data[1]
            current_client["address"] = row_data[2]
            current_client["email"] = row_data[3]
        
            self.client_is_selected = True

        # for filling the buy window inputs
        if self.sqlite_table_name == "Fournisseurs":
            current_supplier["name"] = row_data[0]
            current_supplier["phone_number"] = row_data[1]
            current_supplier["address"] = row_data[2]
            current_supplier["email"] = row_data[3]
        
            self.fournisseur_is_selected = True

        self.close()
            
    
    def update_table(self):
        self.tableWidget.setRowCount(0)
        data = self.sqlite.fetch_data_sqlite(self.sqlite_table_name, self.sqlite_table_columns)

        row_count = len(data)
        column_count = len(self.sqlite_table_columns)

        for row_index in range(row_count):
            self.tableWidget.insertRow(row_index)
            for column_index in range(column_count):
                if len(str(data[row_index][column_index])) != 0:
                    cell_data = str(data[row_index][column_index])
                else:
                    cell_data = "-"
                    
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(cell_data))

        self.rows_count = self.tableWidget.rowCount()

        self.tableWidget.resizeColumnsToContents()        
