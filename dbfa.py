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
    try:
        create_if_not_exists('.dbfa_initialized', './', '')
        config = configparser.ConfigParser()
        create_if_not_exists(CONFIG_FILE, './', DEFAULT_CONFIG)
        config.read(CONFIG_FILE)
        os.makedirs(config['database']['directory'], exist_ok=True)
        return True, 'dbfa initialized'
    except Exception as e:
        return False, e

def create_db(database, table):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    with open(os.path.join(config['database']['directory'], database), 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(table)
        return table

def delete_db(database):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    try:
        os.remove(os.path.join(config['database']['directory'], database))
        return True, database
    except FileNotFoundError:
        return False, database

def query_db(database, query, column=0):
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