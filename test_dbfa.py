""" Test for dbfa. """
import pytest
from dbfa import dbfa

@pytest.fixture(name="db")
def db_init(tmpdir):
    """ Fixture for db. """
    tmpdir = tmpdir.mkdir("test_dbfa_data")
    return dbfa.DBFA(tmpdir)

def test_create(db):
    """ Test for create. """
    assert db.create('test.csv', ['id', 'data'])[0] is True

def test_delete(db):
    """ Test for delete. """
    db.create('test.csv', ['id', 'data'])
    assert db.delete('test.csv')[0] is True

def test_query(db):
    """ Test for query. """
    db.create('test.csv', ['id', 'data'])
    assert db.query('test.csv', 'id', 0)[0] is True

def test_insert_entry(db):
    """ Test for insert_entry. """
    db.create('test.csv', ['id', 'data'])
    assert db.insert_entry('test.csv', ['1', '2'])[0] is True

def test_update_entry(db):
    """ Test for update_entry. """
    db.create('test.csv', ['id', 'data'])
    assert db.update_entry('test.csv', ['1', '2'], ['2', '3'])[0] is True

def test_delete_entry(db):
    """ Test for delete_entry. """
    db.create('test.csv', ['id', 'data'])
    assert db.delete_entry('test.csv', ['1', '2']) is True

def test_list_tables(db):
    """ Test for list_tables. """
    db.create('test.csv', ['id', 'data'])
    assert 'test.csv' in db.list_tables()

def test_all_entries(db):
    """ Test for all_entries. """
    db.create('test.csv', ['id', 'data'])
    assert db.all_entries('test.csv')
