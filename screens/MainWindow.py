__author__ = 'Arjen'
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Set up Main window
        self.setWindowTitle("alchtest")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # Input panel on the left hand side of the screen
        self.input_panel = QWidget()
        self.input_panel.setFixedWidth(200)
        self.main_layout.addWidget(self.input_panel)
        self.input_layout = QVBoxLayout()
        self.input_panel.setLayout(self.input_layout)

        self.input_layout.addWidget(QLabel('Name:'))
        self.name_input = QLineEdit()
        self.input_layout.addWidget(self.name_input)

        self.input_layout.addWidget(QLabel('Address:'))
        self.address_input = QLineEdit()
        self.input_layout.addWidget(self.address_input)

        self.input_submit = QPushButton('Add')
        self.input_layout.addWidget(self.input_submit)

        self.input_layout.addStretch()

        # Table widget in the centre of the screen
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["id", "name", "text"])
        self.table.verticalHeader().hide()
        self.main_layout.addWidget(self.table)

        # Tools panels on the right hand side of the screen
        self.tools_panel = QWidget()
        self.tools_panel.setFixedWidth(100)
        self.main_layout.addWidget(self.tools_panel)
        self.tools_layout = QVBoxLayout()
        self.tools_panel.setLayout(self.tools_layout)

        self.tools_layout.addWidget(QLabel('Tools:'))
        self.tools_delete = QPushButton('Delete')
        self.tools_layout.addWidget(self.tools_delete)
        self.tools_layout.addStretch()

        # Connect local signals to slots
        self.input_submit.clicked.connect(self.submit_input)
        self.tools_delete.clicked.connect(self.delete_selected)

    signal_new_user = pyqtSignal(str, str)
    signal_delete_user = pyqtSignal(int)
    signal_request_table = pyqtSignal()

    cell_by_id = {}

    def submit_input(self):
        name = self.name_input.text()
        address = self.address_input.text()
        self.signal_new_user.emit(name, address)

    def delete_selected(self):
        cells = self.table.selectedItems()
        rows = []
        for c in cells:
            rows.append(c.row())
        rows = set(rows)
        users = []
        for r in rows:
            user_id = int(self.table.item(r, 0).text())
            users.append(user_id)
        for u in users:
            self.signal_delete_user.emit(u)

    def remove_row(self, user_id):
        cell = self.cell_by_id[user_id]
        row = self.table.row(cell)
        self.table.removeRow(row)
        self.table.resizeColumnsToContents()

    def clear_table(self):
            self.table.clear()

    def insert_row(self, user_id, user_name, text):
        row = self.table.rowCount()
        self.table.insertRow(row)
        cell = TableCell(str(user_id))
        self.cell_by_id[user_id] = cell
        self.table.setItem(row, 0, cell)
        self.table.setItem(row, 1, TableCell(user_name))
        self.table.setItem(row, 2, TableCell(text))
        self.table.resizeColumnsToContents()

class TableCell(QTableWidgetItem):
    def __init__(self, data):
        super(TableCell, self).__init__(data)
        self.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
