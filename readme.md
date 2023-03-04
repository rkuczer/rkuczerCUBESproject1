Ryan Kuczer
COMP 490

Imports: From requests.auth import HTTPBasicAuth, import sys, import requests, from typing import Tuple. In tests.py I import the functions from main.py and from pytestqt.qtbot import QtBot. 
In view.py I import from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QCheckBox, QGroupBox and from functools import partial.

An API key is to be imported, a subdomain and form hash variables are needed to be changed to your own form's in the main.py file, the api key is not committed to the project on GitHub.

TO RUN: First run Main.py to create the database and wufoo entries. Then run view.py to show the GUI that handles everything else.

The project gets info from my wufoo form and saves it to a sqlite table that is a part of a database.
There is two tests implemented the first checks if the correct number of data entries are returned from the wufoo api.
The second checks the database and table creation functions in main.py as well as the function that inserts the data into
the database, currently the test function only works if there are multiple entries being entered into the database but still correctly
checks for a test entry.

After receiving the data from the wufoo response the program now creates a GUI window where the user can view data for the following entries.
There is a button that creates a button for each entry and once selected the user can view all the entry's info for the user.
It includes names, their collaboration level, etc. in the form of QLabel's, QCheckBoxes, QvBoxLayouts, etc.
There are also 4 tests that check the functionality of the QLabel's presenting the correct info, the QCheckboxes
and test if there is entries in the database as well.

Currently, the database layout is made up of 4 tables. Entries which has the primary key of entryId that stores the wufoo response from the API for form responses.
The second table records stores the name, email, title and department of each faculty member adding their record.
The third table entry records stores the entryID with the email of the faculty that claimed the porject and a boolean isClaimed that denotes the entry id is claimed.
The fourth table entry_records links the bsu_email with the entry id.

Currently, no missing components are in Sprint 1 Project 4.

Wufoo form location: https://rkuczer.wufoo.com/forms/zqleboe1115c3h/

