"""
Start here to set your config file
"""
import pickle

from main import User


def new_user(username, password, phone):
    with open('config.json', 'wb') as f:
        pickle.dump(User(username, password, phone), f)


if __name__ == "__main__":
    choice = input('New user? (Y/n) ')
    if choice.lower() == 'y':
        username = input('UMBC Username: ')
        password = input('UMBC Password: ')
        phone = input('Phone Number: ')
        new_user(username, password, phone)
