__author__ = 'Arjen'
from PyQt5.QtCore import QObject, pyqtSignal

from database.objects.sys import User, Address
from database import Session


class UserModel(QObject):
    def __init__(self):
        super(UserModel, self).__init__()

    signal_new_user = pyqtSignal(int, str, str)
    signal_delete_user = pyqtSignal(int)

    def send_user(self, u):
        text = '| %s || %s || %s |' % (u.fullname, u.password, u.addresses)
        self.signal_new_user.emit(u.id, u.name, text)

    def load_all_users(self):
        s = Session()
        for u in s.query(User).all():
            self.send_user(u)
        s.close()

    def add_user(self, name, address):
        if not (name == '' or address == ''):
            s = Session()
            u = User(name=name, fullname='%s test' % name, password='pwtest')
            u.addresses = [Address(email_address=address), ]
            s.add(u)
            s.commit()
            self.send_user(u)
            s.close()

    def delete_user(self, user_id):
        s = Session()
        del_user = s.query(User).filter(User.id == user_id).one()
        s.delete(del_user)
        s.commit()
        self.signal_delete_user.emit(user_id)
        s.close()

