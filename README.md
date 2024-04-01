# dbfa.py - Einfache CSV-Datenbank-Verwaltung

dbfa.py ist eine einfache CSV-Datenbank-Verwaltung. Es verwaltet CSV-Dateien
als Tabellen und erlaubt das Einfügen, Lesen, Aktualisieren und Löschen von
Datensätzen.


## Installation

### 1. Neuesten Release herunterladen

### 2. Mit pip installieren

```
pip install dbfa-1.x.x-py3-none-any.whl
```

### 3. Im Projekt benutzen

```python
from dbfa import dbfa
DATA_DIR = './db' # Das Verzeichnis für die Tabellen

db = dbfa.DBFA(DATA_DIR)
db.create('test.csv', ['hello','world']) # Tabelle erstellen
```