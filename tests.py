import sys
import pytest
from pytestqt.qtbot import QtBot

from main import get_wufoo_data, open_db, setup_db, close_db, insert_db
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, \
    QComboBox, QVBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QTextEdit, QCheckBox, QGroupBox
from PySide6.QtGui import QCloseEvent, Qt, QFont
from functools import partial
from view import run, MainWindow


def test_first_name_label(qtbot: QtBot):
    conn = sqlite3.connect('demo_db.sqlite')
    c = conn.cursor()
    c.execute('SELECT * FROM entries')
    data = c.fetchone()
    first_name = data[1]

    window = MainWindow()
    qtbot.addWidget(window)

    entry_button = window.entry_list.itemWidget(window.entry_list.item(0))
    qtbot.mouseClick(entry_button, Qt.LeftButton)

    # Check if the first name label updates correctly
    assert window.first_name.text() == f"First Name: {first_name}"


def test_last_name_label(qtbot: QtBot):
    conn = sqlite3.connect('demo_db.sqlite')
    c = conn.cursor()
    c.execute('SELECT * FROM entries')
    data = c.fetchone()
    last_name = data[2]

    window = MainWindow()
    qtbot.addWidget(window)

    entry_button = window.entry_list.itemWidget(window.entry_list.item(0))
    qtbot.mouseClick(entry_button, Qt.LeftButton)

    # Check if the first name label updates correctly
    assert window.last_name.text() == f"Last Name: {last_name}"


def test_org_name_label(qtbot: QtBot):
    conn = sqlite3.connect('demo_db.sqlite')
    c = conn.cursor()
    c.execute('SELECT * FROM entries')
    data = c.fetchone()
    org_name = data[4]

    window = MainWindow()
    qtbot.addWidget(window)

    entry_button = window.entry_list.itemWidget(window.entry_list.item(0))
    qtbot.mouseClick(entry_button, Qt.LeftButton)

    # Check if the first name label updates correctly
    assert window.org.text() == f"Organization: {org_name}"


def test_data_num():
    response = get_wufoo_data()
    data1 = response['Entries']
    assert len(data1) >= 10, f"Expected 10 entries, but got {len(data1)}"
    return data1


def test_db():
    conn, cursor = open_db("test_db.sqlite")
    print(type(conn))
    response = get_wufoo_data()
    data1 = response['Entries']
    setup_db(cursor)
    insert_db(cursor, data1)
    cursor.execute("SELECT * FROM entries LIMIT 1")
    result = cursor.fetchone()
    assert result is not None, "No entry found in the first row of the table"
    close_db(conn)


if __name__ == '__main__':
    test_data_num()
