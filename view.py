import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, \
    QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QCheckBox, QGroupBox
from functools import partial
from main import get_wufoo_data, insert_db, close_db


class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('demo_db.sqlite')
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        self.setWindowTitle("CUBES Project Main Window")
        self.setGeometry(100, 100, 300, 300)

        chooseDataVis = QPushButton("Data Visualization", self)
        chooseDataVis.setGeometry(0, 0, 150, 300)
        chooseDataVis.clicked.connect(self.dataVis_clicked)
        chooseDataVis.clicked.connect(self.close)

        chooseAlterData = QPushButton("Update Database", self)
        chooseAlterData.setGeometry(150, 0, 150, 300)
        chooseAlterData.clicked.connect(self.updateDataBase)

    def updateDataBase(self):
        apiResponse = get_wufoo_data()
        wufooData = apiResponse['Entries']

        self.conn = sqlite3.connect('demo_db.sqlite')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT COUNT(*) FROM entries")
        tableRows = self.cursor.fetchone()[0]

        if tableRows < len(wufooData):
            insert_db(self.cursor, wufooData)
            print("New Entries detected and inserted.")
        else:
            print("No new entries detected.")
        close_db(self.conn)

    def dataVis_clicked(self):
        ex = MainWindow()
        ex.show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('demo_db.sqlite')
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        self.setWindowTitle("CUBES Project List")
        self.setGeometry(100, 100, 800, 650)

        self.entry_list = QListWidget(self)
        self.entry_list.setGeometry(10, 20, 320, 440)

        self.checkBoxNames = ["Course Project", "Guest Speaker", "Site Visit", "Job Shadow", "Career Panel"]
        self.x = 0
        self.field_checkboxes = []
        for i in range(8, 13):
            checkbox = QCheckBox(self)
            checkbox.setText(self.checkBoxNames[self.x])
            checkbox.setChecked(False)
            checkbox.setEnabled(False)  # Disable initially
            self.field_checkboxes.append(checkbox)
            self.x = self.x + 1

        checkbox_layout = QVBoxLayout()
        for checkbox in self.field_checkboxes:
            checkbox_layout.addWidget(checkbox)

        self.field_group = QGroupBox(self)
        self.field_group.setTitle("Collaborative Opportunities")
        self.field_group.setLayout(checkbox_layout)
        self.field_group.setGeometry(350, 130, 400, 150)

        self.checkBoxNames2 = ["Summer 2022", "Fall 2022", "Spring 2023", "Summer 2023", "Other"]
        self.y = 0
        self.field_checkboxes2 = []
        for i in range(13, 18):
            checkbox2 = QCheckBox(self)
            checkbox2.setText(self.checkBoxNames2[self.y])
            checkbox2.setChecked(False)
            checkbox2.setEnabled(False)  # Disable initially
            self.field_checkboxes2.append(checkbox2)
            self.y = self.y + 1

        checkbox_layout2 = QVBoxLayout()
        for checkbox2 in self.field_checkboxes2:
            checkbox_layout2.addWidget(checkbox2)

        self.field_group2 = QGroupBox(self)
        self.field_group2.setTitle("Collaborative Time Period")
        self.field_group2.setLayout(checkbox_layout2)
        self.field_group2.setGeometry(350, 300, 400, 150)

        self.first_name = QLabel(self)
        self.first_name.setGeometry(350, 0, 150, 50)
        self.first_name.setText("First Name:")
        self.first_name.setWordWrap(True)

        self.last_name = QLabel(self)
        self.last_name.setGeometry(550, 0, 150, 50)
        self.last_name.setText("Last Name:")
        self.last_name.setWordWrap(True)

        self.org = QLabel(self)
        self.org.setGeometry(350, 75, 200, 50)
        self.org.setText("Organization:")
        self.org.setWordWrap(True)

        self.title = QLabel(self)
        self.title.setGeometry(550, 75, 150, 50)
        self.title.setText("Title:")
        self.title.setWordWrap(True)

        self.phone_num = QLabel(self)
        self.phone_num.setGeometry(350, 450, 200, 50)
        self.phone_num.setText("Phone Number:")
        self.phone_num.setWordWrap(True)

        self.school_id = QLabel(self)
        self.school_id.setGeometry(550, 450, 150, 50)
        self.school_id.setText("School ID:")
        self.school_id.setWordWrap(True)

        self.agreement = QLabel(self)
        self.agreement.setGeometry(350, 500, 400, 50)
        self.agreement.setText("Does BSU have their Permission:")
        self.agreement.setWordWrap(True)

        self.claimButton = QPushButton(self)
        self.claimButton.setText("Claim Project")
        self.claimButton.setGeometry(350, 550, 100, 50)

        self.cursor.execute("SELECT * FROM entries")
        data1 = self.cursor.fetchall()

        for entry in data1:
            org_name = entry[4]
            entry_button = QPushButton(org_name, self)
            button_text = org_name

            # Check if any of the fields 123-127 have a value, and add to button text if true
            field_values = [entry[i] for i in range(8, 13)]
            field_values = [value for value in field_values if value]  # Remove empty values
            if field_values:
                field_values_str = ': '.join(field_values)
                if org_name:
                    button_text += ': ' + field_values_str
                else:
                    button_text += field_values_str
            entry_button.setText(button_text)

            item = QListWidgetItem(self.entry_list)
            item.setSizeHint(entry_button.sizeHint())
            self.entry_list.addItem(item)
            self.entry_list.setItemWidget(item, entry_button)
            entry_button.clicked.connect(partial(self.on_entry_button_clicked, entry))

    def on_entry_button_clicked(self, entry):
        first_name = entry[1]
        self.first_name.setText("First Name: {}".format(first_name))
        last_name = entry[2]
        self.last_name.setText("Last Name: {}".format(last_name))
        org_name = entry[4]
        self.org.setText("Organization: {}".format(org_name))
        title = entry[3]
        self.title.setText("Title: {}".format(title))
        phone_num = entry[5]
        self.phone_num.setText("Phone Number: {}".format(phone_num))
        school_id = entry[6]
        self.school_id.setText("School ID: {}".format(school_id))
        agreement = entry[18]
        self.agreement.setText("Does BSU have their Permission: {}".format(agreement))

        for i in range(8, 13):
            field_value = entry[i]
            checkbox = self.field_checkboxes[i - 8]
            if field_value:
                checkbox.setChecked(True)
                checkbox.setEnabled(True)
            else:
                checkbox.setChecked(False)
                checkbox.setEnabled(False)

        for i in range(13, 18):
            field_value2 = entry[i]
            checkbox2 = self.field_checkboxes2[i - 13]  # subtract 5 to get the correct index
            if field_value2:
                checkbox2.setChecked(True)
                checkbox2.setEnabled(True)
            else:
                checkbox2.setChecked(False)
                checkbox2.setEnabled(False)


def run():
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    firstWin = FirstWindow()
    firstWin.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()
