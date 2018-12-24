#!/usr/bin/env python3

from getpass import getpass
import hashlib
from db import add_data, auth, friendList
from datetime import datetime

class NewUser():
    def __init__(self):
        self.getData()
        self.putData()

    def getData(self):
        encrypt = hashlib.sha256()
        self.username = input("Enter Username : ")
        encrypt.update(getpass("Enter Password : ").encode())
        self.password = encrypt.hexdigest()
        self.cont_num = input("Enter Contact number : ")
        self.sig = self.username + self.cont_num
        self.time = datetime.now()
    
    def putData(self):
        add_data(self.username, self.password, self.cont_num, self.sig, self.time)


class Login():
    def __init__(self):
        self.getData()
        self.authenticate()

    def getData(self):
        encrypt = hashlib.sha256()
        self.sig= input("Enter Signature : ")
        encrypt.update(getpass("Enter Password : ").encode())
        self.password = encrypt.hexdigest()

    def authenticate(self):
        ch = auth(self.sig, self.password)
        if ch == 0:
            print("Welcome  " + self.sig)
        else:
            print("Signature or Password Invalid")
    
    def userSelect(self):
        print("\nList of contacts :\n")
        self.frnd_list = friendList(self.sig)
        for i, frnd in enumerate(self.frnd_list):
            print("{0}.{1}".format(i+1, frnd))
        chat_choice = int(input("\nPlease enter with whom you want to chat : "))
        return(self.sig, self.frnd_list[chat_choice - 1])


if __name__ == '__main__':
    NewUser()
