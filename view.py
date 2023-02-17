import json
import sqlite3
import sys
import PySide6
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, \
    QComboBox, QVBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QTextEdit, QCheckBox, QGroupBox
from PySide6.QtGui import QCloseEvent, Qt, QFont
from main import get_wufoo_data
from functools import partial


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('demo_db.sqlite')
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        self.setWindowTitle("CUBES Project List")
        self.setGeometry(100, 100, 800, 500)

        self.entry_list = QListWidget(self)
        self.entry_list.setGeometry(20, 20, 300, 440)

        self.checkBoxNames = ["Course Project", "Guest Speaker", "Site Visit", "Job Shadow", "Career Panel"]
        self.x = 0
        self.field_checkboxes = []
        for i in range(8, 13):
            checkbox = QCheckBox(self)
            checkbox.setText(self.checkBoxNames[self.x])
            checkbox.setChecked(False)
            checkbox.setEnabled(False)  # Disable initially
            self.field_checkboxes.append(checkbox)
            self.x=self.x+1

        checkbox_layout = QVBoxLayout()
        for checkbox in self.field_checkboxes:
            checkbox_layout.addWidget(checkbox)

        self.field_group = QGroupBox(self)
        self.field_group.setTitle("Collaborative Opportunities")
        self.field_group.setLayout(checkbox_layout)
        self.field_group.setGeometry(350, 130, 400, 150)

        self.field_group2 = QGroupBox(self)
        self.field_group2.setTitle("Collaborative Time Period")
        self.field_group2.setGeometry(350, 300, 400, 150)

        self.first_name = QLabel(self)
        self.first_name.setGeometry(350, 0, 100, 50)
        self.first_name.setText("First Name:")
        self.first_name.setWordWrap(True)

        self.last_name = QLabel(self)
        self.last_name.setGeometry(550, 0, 100, 50)
        self.last_name.setText("Last Name:")
        self.last_name.setWordWrap(True)
        self.org = QLabel(self)
        self.org.setGeometry(350, 75, 110, 50)
        self.org.setText("Organization:")
        self.org.setWordWrap(True)
        self.title = QLabel(self)
        self.title.setGeometry(550, 75, 100, 50)
        self.title.setText("Title:")
        self.title.setWordWrap(True)

        btn_quit = QPushButton('Force Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(700, 470)

        self.cursor.execute("SELECT * FROM entries")
        data1 = self.cursor.fetchall()

        for entry in data1:
            org_name = entry[4]
            entry_button = QPushButton(org_name, self)
            entry_id = entry[0]

            button_text = org_name

            # Check if any of the fields 123-127 have a value, and add to button text if true
            field_values = [entry[i] for i in range(8, 12)]
            field_values = [value for value in field_values if value]  # Remove empty values
            if field_values:
                field_values_str = ', '.join(field_values)
                if org_name:
                    button_text += ', ' + field_values_str
                else:
                    button_text += field_values_str
            entry_button.setText(button_text)

            item = QListWidgetItem(self.entry_list)
            item.setSizeHint(entry_button.sizeHint())
            self.entry_list.addItem(item)
            self.entry_list.setItemWidget(item, entry_button)
            entry_button.clicked.connect(partial(self.on_entry_button_clicked, entry))
        self.show()

    def on_entry_button_clicked(self, entry):
        first_name = entry[1]
        self.first_name.setText("First Name: {}".format(first_name))
        last_name = entry[2]
        self.last_name.setText("Last Name: {}".format(last_name))
        org_name = entry[4]
        self.org.setText("Organization: {}".format(org_name))
        title = entry[3]
        self.title.setText("Title: {}".format(title))

        for i in range(8, 13):
            field_value = entry[i]
            checkbox = self.field_checkboxes[i - 8]
            if field_value:
                checkbox.setChecked(True)
                checkbox.setEnabled(True)
            else:
                checkbox.setChecked(False)
                checkbox.setEnabled(False)



    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def run():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()
