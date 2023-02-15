import sys
import PySide6
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, \
    QComboBox, QVBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem
from PySide6.QtGui import QCloseEvent
from main import get_wufoo_data
from functools import partial


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle("CUBES Project List")
        self.setGeometry(100, 100, 800, 500)

        self.entry_list = QListWidget(self)
        self.entry_list.setGeometry(20, 20, 300, 440)

        btn_quit = QPushButton('Force Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(700, 470)

        data = get_wufoo_data()
        data1 = data['Entries']

        for entry in data1:
            org_site = entry['Field430']
            entry_button = QPushButton(org_site, self)

            entry_id = entry['EntryId']

            entry_button.clicked.connect(partial(self.on_entry_button_clicked, entry_id))

            item = QListWidgetItem(self.entry_list)
            item.setSizeHint(entry_button.sizeHint())
            self.entry_list.addItem(item)
            self.entry_list.setItemWidget(item, entry_button)

        self.show()

    def on_entry_button_clicked(self, entry_id):
        print(f"Entry {entry_id} button clicked")


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