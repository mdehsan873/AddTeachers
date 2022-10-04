import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Constants import DRIVERPATH, WEBURL, USERNAME_XPATH, PASSWORD_XPATH, USERNAME, PASSWORD, LOGIN_BUTTON_XPATH, \
    ADD_TEACHER_BUTTON_XPATH, TEACHER_ADHAR_XPATH, TEACHER_EMAIL_XPATH, TEACHER_GENDER_XPATH, TEACHER_NAME_XPATH, \
    TEACHER_PHONE_XPATH, TEACHER_ADDRESS_XPATH, MALE_FEMALE_XPATH, SAVE_BUTTON, ADD_TEACHER_FRAME

driver = webdriver.Chrome(DRIVERPATH)
driver.get(WEBURL)
time.sleep(5)
username = driver.find_element('xpath', USERNAME_XPATH)
password = driver.find_element('xpath', PASSWORD_XPATH)
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
login = driver.find_element('xpath', LOGIN_BUTTON_XPATH)
login.click()
time.sleep(10)
# add_teacher_button = driver.find_element('xpath', ADD_TEACHER_BUTTON_XPATH)
# add_teacher_button.click()
teacher_name = ['ehsawn', 'asad']
teacher__phone_no = ['9120512345', '12345678908']
email = ['reacher1@gmail.com', 'teahcer2@gmail.com']
address = ['ghar1', 'ghar2']
gender = ['Male', 'Female']
adhar_no = ['123416739012', '876543219876']


for i in range(0, len(teacher_name)):
    add_teacher_button = driver.find_element('xpath', ADD_TEACHER_BUTTON_XPATH)
    add_teacher_button.click()
    # time.sleep(2)
    # frame = driver.find_element("xpath",ADD_TEACHER_FRAME)
    # driver.switch_to.frame(frame)
    teacher_name_field = driver.find_element('xpath', TEACHER_NAME_XPATH)
    teacher_email_field = driver.find_element('xpath', TEACHER_EMAIL_XPATH)
    teacher_phone_field = driver.find_element('xpath', TEACHER_PHONE_XPATH)
    teacher_adhar_field = driver.find_element('xpath', TEACHER_ADHAR_XPATH)
    teacher_address_field = driver.find_element('xpath', TEACHER_ADDRESS_XPATH)
    teacher_gender_field = Select(driver.find_element('xpath', TEACHER_GENDER_XPATH))
    teacher_name_field.send_keys(teacher_name[i])
    teacher_address_field.send_keys(address[i])
    teacher_phone_field.send_keys(teacher__phone_no[i])
    teacher_email_field.send_keys(email[i])
    teacher_adhar_field.send_keys(adhar_no[i])
    teacher_gender_field.select_by_visible_text(gender[i])
    driver.execute_script("document.getElementsByClassName('primary-cta w-100')[0].click()")
    time.sleep(5)
    a =driver.switch_to.alert.accept()
    time.sleep(5)
