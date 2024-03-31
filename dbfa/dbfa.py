# Database for the poor
import csv
import configparser
import os

CONFIG_FILE = 'dbfa_config.ini'
DEFAULT_CONFIG = """
[database]
directory = ./db/
"""

def create_if_not_exists(filename, path, contents):
    try:
        with open(path + filename) as f:
            return
    except IOError:
        with open(path + filename, 'w') as f:
            f.write(contents)

def initialize():
    """
    Initializes the dbfa by checking if it has been initialized before and creating necessary files and directories.
    
    Returns:
        A tuple containing a boolean indicating whether the initialization was successful and a string message.
    """
    try:
        create_if_not_exists('.dbfa_initialized', './', '')
        config = configparser.ConfigParser()
        create_if_not_exists(CONFIG_FILE, './', DEFAULT_CONFIG)
        config.read(CONFIG_FILE)
        os.makedirs(config['database']['directory'], exist_ok=True)
        return True, 'dbfa initialized'
    except Exception as e:
        return False, f'dfba initialization failed with error: {e}'

def create_db(database, table):
    """
    Creates a new database file with the specified database name and writes the given table to it.

    Parameters:
        database (str): The name of the database.
        table (list): The table to be written to the database file.

    Returns:
        list: The table that was written to the database file.
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    with open(os.path.join(config['database']['directory'], database), 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(table)
        return table

def delete_db(database):
    """
    Deletes a database file from the specified directory.

    Parameters:
        database (str): The name of the database file to be deleted.

    Returns:
        tuple: A tuple containing a boolean indicating the success of the deletion and the name of the deleted database file.
            - If the deletion is successful, the boolean value is True and the name of the deleted database file is returned.
            - If the deletion fails because the file is not found, the boolean value is False and the name of the deleted database file is returned.
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    try:
        os.remove(os.path.join(config['database']['directory'], database))
        return True, database
    except FileNotFoundError:
        return False, database

def query_db(database, query, column=0):
    """
    Query a database for a specific entry based on a given query and optional column index.

    Parameters:
    - database (str): the name of the database to query
    - query (str): the value to search for in the specified column
    - column (int): the index of the column to search the query in (default is 0)

    Returns:
    - list: The entry that matches the query in the specified column, or None if not found.
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    try:
        with open(os.path.join(config['database']['directory'], database), newline='', encoding='utf-8') as csvfile:
            entries = list(csv.reader(csvfile, delimiter='|'))
            for entry in entries:
                if entry[column] == query:
                    return entry
    except FileNotFoundError:
        pass

def add_entry(database, entry):
    """
    Add an entry to the specified database.

    Parameters:
    - database (str): the name of the database
    - entry (list): the entry to add to the database

    Returns:
    - list: The added entry
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    try:
        with open(os.path.join(config['database']['directory'], database), 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            writer.writerow(entry)
            return entry
    except FileNotFoundError:
        pass

def update_entry(database, old_entry, new_entry):
    """
    Update an entry in the specified database.

    Parameters:
    - database (str): the name of the database to update the entry in
    - old_entry (list): the entry to be replaced
    - new_entry (list): the new entry to replace the old one

    Returns:
    - list: The new_entry if the update is successful
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    try:
        with open(os.path.join(config['database']['directory'], database), 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            new_db = []
            for row in reader:
                if row == old_entry:
                    new_db.append(new_entry)
                else:
                    new_db.append(row)

        with open(os.path.join(config['database']['directory'], database), 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            writer.writerows(new_db)

        return new_entry
    except FileNotFoundError:
        pass

def remove_entry(database, entry):
    """
    Removes an entry from a specified database.

    Parameters:
        database (str): The name of the database from which the entry should be removed.
        entry (list): The entry to be removed from the database.

    Returns:
        list: The removed entry from the database.
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    try:
        with open(os.path.join(config['database']['directory'], database), 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            new_db = []
            for row in reader:
                if row != entry:
                    new_db.append(row)

        with open(os.path.join(config['database']['directory'], database), 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            writer.writerows(new_db)

        return entry
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    init = initialize()
    if init[0]:
        print(init[1])
    else:
        print(init[1])