__author__ = 'Arjen'
import sys
from PyQt5.QtWidgets import QApplication
from database.dbsetup import create
from screens.MainWindow import MainWindow
from models.UserModel import UserModel


if __name__ == '__main__':
    # Setup the db
    create()

    # Init the app and main window
    App = QApplication(sys.argv)
    mi = UserModel()
    mw = MainWindow()

    # Connect interface to the screen
    mi.signal_new_user.connect(mw.insert_row)
    mi.signal_delete_user.connect(mw.remove_row)

    # Connect screen to the interface
    mw.signal_request_table.connect(mi.load_all_users)
    mw.signal_new_user.connect(mi.add_user)
    mw.signal_delete_user.connect(mi.delete_user)

    # Show main window and load data
    mw.show()
    mw.signal_request_table.emit()
    sys.exit(App.exec_())
