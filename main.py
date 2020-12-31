"""
Daily Symptom Tracking
Auto-Submission
"""
from time import sleep
from selenium import webdriver
import pickle
import json
from random import uniform


class User:
    def __init__ (self, username,password, phone):
        self.username = username
        self.password = password
        self.phone = phone

def login(username, password, phone):
    driver = webdriver.Chrome()
    driver.get(
        'https://rtforms.umbc.edu/rt_authenticated/legal/COVID_Contact_and_Symptoms.php')
    userfield = driver.find_element_by_id('username')
    pfield = driver.find_element_by_id('password')
    login_button = driver.find_element_by_id('submitButton')
    userfield.send_keys(username)
    pfield.send_keys(password)
    login_button.click()
    sleep(10)
    SymptomTrack(driver)

def SymptomTrack(driver, phone):
    driver.get(
        'https://rtforms.umbc.edu/rt_authenticated/legal/COVID_Contact_and_Symptoms.php')
    phone = driver.find_element_by_id('reporterPhone')
    temp = driver.find_element_by_id('temperature')
    none = driver.find_element_by_id('symptoms_none')
    phone.send_keys(str(phone))
    temp.send_keys(str(round(uniform(97.0, 98.9),1)))
    none.click()


def load_user():
    with open('config.json', 'rb') as f:
        return pickle.load(f)


if __name__ == "__main__":
    user = load_user()
    login(user.username, user.password, user.phone)
    SymptomTrack()


