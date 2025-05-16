from PyQt5.QtWidgets import QTableWidgetItem

class AchatsVentesTabs:
    def __init__(self, sqlite, mw, sqlite_table_name, sqlite_database_columns, tableWidget, comboBox):
        self.sqlite = sqlite
        self.sqlite_table_name = sqlite_table_name
        self.sqlite_database_columns = sqlite_database_columns
        self.mw = mw
        self.tableWidget = tableWidget
        self.selection_enabled = False
        self.current_row_count = -1
        self.items = None
        self.rows_count = None  
        
        self.product_name_column_number = 1
        self.category_column_number = 5

        self.comboBox = comboBox
    
    def filter_table_widget(self, text):
        column_index = ""
        filtre_by = self.comboBox.currentText()
        if filtre_by == "Nom du Produit": column_index = 1
        elif filtre_by == "Catégorie": column_index = 5
        # Filter the rows based on the search input
        filtered_items = [item for item in self.items if item[column_index].lower().startswith(text.lower())]

        # Clear the current rows in the table and repopulate it with filtered items
        self.tableWidget.clearContents()
        self.update_table(filtered_items)
            


    def update_table(self, data=None):
        # clear before inserting 
        self.tableWidget.setRowCount(0)
        if data is None:
            # Fetch sqlite data and insert to the Tab 
            columns_to_fetch_data_from = self.sqlite_database_columns
            data = self.sqlite.fetch_data_sqlite(self.sqlite_table_name, columns_to_fetch_data_from)
            self.items = data 


        row_count = len(data)
        column_count = len(self.sqlite_database_columns)

        for row_index in range(row_count):
            self.tableWidget.insertRow(row_index)
            for column_index in range(column_count):
                if len(str(data[row_index][column_index])) != 0:
                    cell_data = str(data[row_index][column_index])
                else:
                    cell_data = "-"

                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(cell_data))

        if self.rows_count is None: self.rows_count = self.tableWidget.rowCount()

        self.tableWidget.resizeColumnsToContents()    

    
    def delete_transaction_record(self):
        transaction_record_deleted = self.mw.delete(self.tableWidget, self.sqlite_table_name, self.selection_enabled)
        if transaction_record_deleted: 
            try:
                self.update_after_deletion()
            except: pass

            deleting_query = f"DELETE FROM {self.sqlite_table_name} WHERE record_id = ?"
            record_id = self.tableWidget.item(self.current_row_count, 0).text()
            self.sqlite.db.delete_data(deleting_query, (record_id,))
            self.tableWidget.removeRow(self.current_row_count)
            self.tableWidget.clearSelection()
            self.rows_count -= 1
            self.mw.reassign_row_ids(self.sqlite_table_name)
            self.current_row_count = -1
            

    def update_after_deletion(self):
        product_name = self.tableWidget.item(self.current_row_count, self.product_name_column_number).text()
        category = self.tableWidget.item(self.current_row_count, self.category_column_number).text()
        amount = int(self.tableWidget.item(self.current_row_count, 2).text())
        price = float(self.tableWidget.item(self.current_row_count, 3).text())


        if self.sqlite_table_name == "Purchases":
            fetch_query = f"SELECT total_depense, quantite_actuelle, quantite_achetee_totale, benefices FROM Products WHERE nom_du_produit = ? AND categorie = ?"
            data_fetched = self.sqlite.db.fetch_data(fetch_query, (product_name, category))

            total_depense = float(data_fetched[0])
            quantite_actuelle = int(data_fetched[1])
            quantite_achetee_totale = int(data_fetched[2])
            benefices = float(data_fetched[3])

            total_depense -= price
            quantite_actuelle -= amount
            quantite_achetee_totale -= amount
            benefices += price
            total_depense = round(total_depense, 3)
            benefices = round(benefices, 3)

            if not (quantite_achetee_totale < 0 or quantite_actuelle < 0):
                """"
                i have added this condition because if the user manually changes the 
                quantities on the product details in (Products) tab or deletes product 
                when there are purchases/sales things will get ruined here
                """
                update_query = f"UPDATE Products SET total_depense=?, quantite_actuelle=?, quantite_achetee_totale=?, benefices=?  WHERE nom_du_produit = ? AND categorie = ?"
                self.sqlite.db.insert_data(update_query, (total_depense, quantite_actuelle, quantite_achetee_totale, benefices, product_name, category))

        elif self.sqlite_table_name == "Sales":
            fetch_query = f"SELECT total_gagne, quantite_actuelle, quantite_vendue_totale, benefices FROM Products WHERE nom_du_produit = ? AND categorie = ?"
            data_fetched = self.sqlite.db.fetch_data(fetch_query, (product_name, category))

            total_gagne = float(data_fetched[0])
            quantite_actuelle = int(data_fetched[1])
            quantite_vendue_totale = int(data_fetched[2])
            benefices = float(data_fetched[3])

            total_gagne -= price
            quantite_actuelle += amount
            quantite_vendue_totale -= amount
            benefices -= price

            total_gagne = round(total_gagne, 3)
            benefices = round(benefices, 3)

            if not (quantite_vendue_totale < 0 or quantite_actuelle < 0):
                """"
                i have added this condition because if the user manually changes the 
                quantities on the product details in (Products) tab things will get ruined here
                """
                update_query = f"UPDATE Products SET total_gagne=?, quantite_actuelle=?, quantite_vendue_totale=?, benefices=?  WHERE nom_du_produit = ? AND categorie = ?"
                self.sqlite.db.insert_data(update_query, (total_gagne, quantite_actuelle, quantite_vendue_totale, benefices, product_name, category))
        
        self.mw.fill_product_data_to_table()
                


        

    def selection_changed(self):
        selected_items = self.tableWidget.selectedItems()
        self.selection_enabled = bool(selected_items)
    
    def on_table_item_clicked(self, item):
        self.current_row_count = item.row()

    def previous(self):
        if self.current_row_count <= 0:
            self.current_row_count = self.tableWidget.rowCount()

        self.current_row_count -= 1
        self.tableWidget.selectRow(self.current_row_count)


    def next(self):
        if self.current_row_count >= self.tableWidget.rowCount()-1:
            self.current_row_count = -1
        self.current_row_count += 1
        self.tableWidget.selectRow(self.current_row_count)
