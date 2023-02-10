import sys
import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QCloseEvent
from main import get_wufoo_data

class ExampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        data = get_wufoo_data()
        data_entries = data['Entries']
        header = ['EntryId', 'first_name', 'last_name', 'job_title', 'org_name', 'phone_num',
        'school_id', 'org_site', 'course', 'speaker', 'siteVisit', 'job_shadow', 'carreer_panel',
        'summer_2022', 'fall_2022', 'spring_2023', 'summer_2023', 'other', 'permission', 'date_created', 'created_by', 'date_update', 'updated_by']
        self.setWindowTitle('Cubes Project List')

        self.setGeometry(100, 100, 800, 600)

        self.table = QTableWidget(self)
        self.table.setRowCount(len(data_entries))
        self.table.setColumnCount(len(data_entries[0]))
        self.table.setHorizontalHeaderLabels(header)
        self.table.resizeColumnsToContents()
        self.table.setGeometry(0, 0, 800, 500)


        for i, entry in enumerate(data_entries):
            for j, val in enumerate(entry):
                item = QTableWidgetItem(val)
                self.table.setItem(i, j, item)

        #exam.setCentralWidget(self.table)

        btn_quit = QPushButton('Force Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(700, 500)

        self.show()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def run():
    app = QApplication(sys.argv)

    ex = ExampleWindow()

    sys.exit(app.exec())


if __name__ == '__main__':
    run()