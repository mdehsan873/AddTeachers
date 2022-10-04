import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Constants import DRIVERPATH, WEBURL, USERNAME_XPATH, PASSWORD_XPATH, USERNAME, PASSWORD, LOGIN_BUTTON_XPATH, \
    ADD_TEACHER_BUTTON_XPATH, TEACHER_ADHAR_XPATH, TEACHER_EMAIL_XPATH, TEACHER_GENDER_XPATH, TEACHER_NAME_XPATH, \
    TEACHER_PHONE_XPATH, TEACHER_ADDRESS_XPATH, MALE_FEMALE_XPATH, SAVE_BUTTON, ADD_TEACHER_FRAME


def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    driver = webdriver.Chrome(DRIVERPATH,chrome_options=options)
    driver.get(WEBURL)
    time.sleep(5)
    username = driver.find_element('xpath', USERNAME_XPATH)
    password = driver.find_element('xpath', PASSWORD_XPATH)
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    login = driver.find_element('xpath', LOGIN_BUTTON_XPATH)
    login.click()
    time.sleep(5)
    return driver