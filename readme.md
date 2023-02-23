Ryan Kuczer
COMP 490

Imports: From requests.auth import HTTPBasicAuth, import sys, import requests, from typing import Tuple. In tests.py I import the functions from main.py and from pytestqt.qtbot import QtBot. In view.py I import from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QCheckBox, QGroupBox and from functools import partial.

An API key is to be imported, a subdomain and form hash variables are needed to be changed to your own form's in the main.py file, the api key is not committed to the project on github.

TO RUN: Run view.py.

The project gets info from my wufoo form and saves it to a sqllite table that is a part of a database.
There is two tests implemented the first checks if the correct number of data entries are returned from the wufoo api.
The second checks the database and table creation functions in main.py as well as the function that inserts the data into
the database, currently the test function only works if there are multiple entries being entered into the database but still correctly
checks for a test entry.

After receiving the data from the wufoo response the program now creates a GUI window where the user can view data for the following entries.
There is a buttot that creates a button for each entry and once selected the user can view all the entry's info for the user.
It includes names, their collaboration level, etc. in the form of QLabel's, QCheckBoxes, QvBoxLayouts, etc.
There are also 4 tests that check the functionality of the QLabel's presenting the correct info, the QCheckboxes
and test if there is entries in the database as well.

Currently, the database layout is a single table named 'entries' with each field in the json response as its own column. 

Currently, no missing components are in Sprint 1 Project 3.

Wufoo form location: https://rkuczer.wufoo.com/forms/zqleboe1115c3h/

