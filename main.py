"""
Daily Symptom Tracking
Auto-Submission
"""

import pickle
from os import chdir
from random import uniform
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bfl import letter


class User:
    def __init__(self, username, password, phone):
        self.username = username
        self.password = password
        self.phone = phone


def login(username, password, phone):
    print('Loading Driver...')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    driver.get(
        'https://rtforms.umbc.edu/rt_authenticated/legal/COVID_Contact_and_Symptoms.php')
    print('Logging in...')
    userfield = driver.find_element_by_id('username')
    pfield = driver.find_element_by_id('password')
    login_button = driver.find_element_by_id('submitButton')
    userfield.send_keys(username)
    pfield.send_keys(password)
    login_button.click()
    sleep(10)
    print('Tracking Symptoms...')
    SymptomTrack(driver, phone)


def randtemp():
    new_temp = round(uniform(97.0, 98.9), 1)
    return str(new_temp)


def SymptomTrack(driver, phone):
    driver.get(
        'https://rtforms.umbc.edu/rt_authenticated/legal/COVID_Contact_and_Symptoms.php')
    try:
        userphone = driver.find_element_by_id('reporterPhone')
    except:
        print("You have already filled out your symptom tracker today.")
    else:
        temp = driver.find_element_by_id('temperature')
        none = driver.find_element_by_id('symptoms_none')
        submit = driver.find_element_by_id('submit')
        userphone.send_keys(str(phone))
        print('Temperature: {}'.format(randtemp()))
        temp.send_keys(randtemp())
        none.click()
        submit.click()
        sleep(10)
        print('Symptom Tracker Completed')


def load_user():
    with open('config.json', 'rb') as f:
        return pickle.load(f)


if __name__ == "__main__":
    chdir('/Users/lukegude/Desktop_2/Development/Python/SymptomTrackerScript')
    try:
        load_user()
    except EOFError:
        print("Run config.py before running this program")
    else:
        print(letter())
        print('Loading User...')
        user = load_user()
        login(user.username, user.password, user.phone)
