""" A simple csv database file manager, using python's csv, configparser, and os module. """
import csv
import os

class DBFA():
    """ A simple csv database file manager. """
    def __init__(self, data_path='./'):
        """ Initialize DBFA. """
        self.data_path = data_path

    def create(self, table, fields):
        """ Create a new table. """
        try:
            data_path = self.data_path

            with open(os.path.join(data_path, table), 'x', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter='|')
                writer.writerow(fields)
            return True, table, fields
        except FileExistsError:
            return False, table, fields

    def delete(self, table):
        """ Delete a table. """
        try:
            os.remove(os.path.join(self.data_path, table))
            return True, table
        except FileNotFoundError:
            return False, table

    def query(self, table, query, column=0):
        """ Query a table. """
        try:
            table_path = os.path.join(self.data_path, table)
            with open(table_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter='|')
                for row in reader:
                    if query == row[column]:
                        return True, table, row
            return False
        except FileNotFoundError:
            return False

    def insert_entry(self, table, entry):
        """ Insert an entry into a table. """
        try:
            table_path = os.path.join(self.data_path, table)
            with open(table_path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter='|')
                writer.writerow(entry)
            return True, table, entry
        except FileNotFoundError:
            return False

    def update_entry(self, table, old_entry, new_entry):
        """ Update an entry in a table. """
        try:
            table_path = os.path.join(self.data_path, table)
            with open(table_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter='|')
                new_db = []
                for row in reader:
                    if row == old_entry:
                        new_db.append(new_entry)
                    else:
                        new_db.append(row)

            with open(table_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter='|')
                writer.writerows(new_db)
            return True, table, new_entry
        except FileNotFoundError:
            return False

    def delete_entry(self, table, entry):
        """ Delete an entry from a table. """
        try:
            table_path = os.path.join(self.data_path, table)
            with open(table_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter='|')
                with open(table_path, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter='|')
                    for row in reader:
                        if row != entry:
                            writer.writerow(row)
            return True
        except FileNotFoundError:
            return False

    def list_tables(self):
        """ List all tables. """
        try:
            return os.listdir(self.data_path)
        except FileNotFoundError:
            return False

    def all_entries(self, table):
        """ List all entries in a table. """
        try:
            table_path = os.path.join(self.data_path, table)
            with open(table_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter='|')
                return list(reader)
        except FileNotFoundError:
            return False
