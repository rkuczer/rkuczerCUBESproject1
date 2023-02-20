import sys
import pytest
from main import get_wufoo_data, open_db, setup_db, close_db, insert_db
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, \
    QComboBox, QVBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QTextEdit, QCheckBox, QGroupBox
from PySide6.QtGui import QCloseEvent, Qt, QFont
from functools import partial
from view import run, MainWindow

conn, cursor = open_db("test_db.sqlite")
print(type(conn))


@pytest.fixture
def app(qtbot):
    test_app = QApplication([])
    window = MainWindow()
    qtbot.addWidget(window)
    return test_app


def test_first_name_label(app, qtbot):
    conn, cursor = open_db("test_db.sqlite")
    cursor.execute("SELECT * FROM entries")
    data1 = cursor.fetchall()
    test_entry = (1, "James")
    # find the "first_name" QLabel in the window
    first_name_label = app.activeWindow().findChild(QLabel, "first_name")
    # call the on_entry_button_clicked function with the test entry
    app.activeWindow().on_entry_button_clicked(test_entry)
    # check that the text of the "first_name" QLabel has been updated to "First Name: Alice"
    assert first_name_label.text() == "First Name: James"

    # Set up test data
    #entry_id = 1
    #expected_first_name = "James"
    # Find the button and click it
    #button = ex.findChild(QPushButton, f"button_{entry_id}")
    #button.click()

    # Find the first name label and check its text
    #first_name_label = ex.findChild(QLabel, "first_name")
    #assert first_name_label.text() == expected_first_name


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
