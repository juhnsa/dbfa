*There is an English section for dbfa in this README. [View](#databases-for-the-poor-dbfa-english)*

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
![pylint workflow](https://github.com/juhnsa/dbfa/actions/workflows/pylint.yml/badge.svg)

# Datenbanken für Arme (dbfa)

dbfa ist ein einfaches Datenbanksystem, das ausschließlich aus Python-Bibliotheken besteht.

Die Datenbanken sind in CSV-Dateien gespeichert und bestehen aus einer Tabelle pro Datei.

## Installation

Mit `setuptools` das Paket installieren:

```python3
python setup.py install
```

und dann im Projekt mit

```
from dbfa import dbfa

print(str(dbfa.initialize()))
```

initialisieren.

## Funktionen

- Eine Datenbank erstellen, durchsuchen und löschen
- Einträge in Tabelle hinzufügen, ändern und löschen
- Nur eine Tabelle pro Datenbank (kann in der Zukunft geändert werden)

# Databases for the poor (dbfa) ENGLISH

dbfa is a simple database system consisting solely of Python libraries.

The databases are stored in CSV files and consist of one table per file.

## Installation

Install the package with `setuptools`

```python3
python setup.py install
```

and initialize in the project with

```
from dbfa import dbfa

print(str(dbfa.initialize()))
```

## Functionality

- Create, query and delete a database
- Add, update and delete entries
- Note: Only one table per database (this may be changed in the future)