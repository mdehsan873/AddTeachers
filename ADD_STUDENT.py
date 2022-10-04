import time

from selenium.webdriver.support.select import Select

from read_csv import get_student_data
from Utils import get_driver
from Constants import ADD_STUDENT_HOME_BUTTON_XPATH, FIRST_NAME_XPATH, LAST_NAME_XPATH, GENDER_DROPDOWN_XPATH, \
    FATHER_NAME_XPATH, MOTHER_NAME_XPATH, PHONE_NUMBER_XPATH, REGISTRATION_XPATH, ROLL_NO_XPATH, SESSION_XPATH, \
    CLASS_XPATH


def get_fist_element(driver):
    try:
        driver.find_element("xpath", FIRST_NAME_XPATH)
        return True
    except Exception:
        return False


def last_fist_element(driver):
    try:
        driver.find_element("xpath", LAST_NAME_XPATH)
        return True
    except Exception:
        return False


def get_session(driver):
    try:
        Select(driver.find_element("xpath", SESSION_XPATH)).select_by_visible_text("22-23")
        return True
    except Exception:
        return False


def get_father_name(driver):
    try:
        driver.find_element("xpath", FATHER_NAME_XPATH).clear()
        return True
    except Exception:
        return False


def get_mother_name(driver):
    try:
        driver.find_element("xpath", MOTHER_NAME_XPATH)
        return True
    except Exception:
        return False


def get_gender(driver):
    try:
        driver.find_element("xpath", GENDER_DROPDOWN_XPATH)
        return True
    except Exception:
        return False


def get_ph(driver):
    try:
        driver.find_element("xpath", PHONE_NUMBER_XPATH)
        return True
    except Exception:
        return False


def get_reg(driver):
    try:
        driver.find_element("xpath", PHONE_NUMBER_XPATH)
        return True
    except Exception:
        return False


def get_roll(driver):
    try:
        driver.find_element("xpath", ROLL_NO_XPATH)
        return True
    except Exception:
        return False


def get_class(driver):
    try:
        driver.find_element("xpath", CLASS_XPATH)
        return True
    except Exception:
        return False


def click(driver):
    try:
        driver.execute_script("document.getElementsByClassName('primary-cta w-100')[0].click()")
        return True
    except Exception:
        return False


def get_add_student(driver):
    try:
        driver.find_element('xpath', ADD_STUDENT_HOME_BUTTON_XPATH)
        return True
    except Exception:
        return False


def aleart(driver):
    try:
        driver.switch_to.alert
        return True
    except Exception:
        return False


gender_dict = {"M": "Male", "F": "Female"}
first_name, middle_name, last_name, dob, reg_no, father_name, mother_name, ph_no, address, gender, session, Class, section, roll_no = get_student_data()
driver = get_driver()
print("logged in")
for i in range(171, len(first_name)):
    while not get_add_student(driver):
        pass
    add_student = driver.find_element('xpath', ADD_STUDENT_HOME_BUTTON_XPATH)
    add_student.click()

    while not get_fist_element(driver):
        pass
    driver.find_element("xpath", FIRST_NAME_XPATH).send_keys(first_name[i])
    while not last_fist_element(driver):
        pass
    driver.find_element("xpath", LAST_NAME_XPATH).send_keys(last_name[i])
    while not get_session(driver):
        pass
    Select(driver.find_element("xpath", SESSION_XPATH)).select_by_visible_text("22-23")
    while not get_father_name(driver):
        pass
    driver.find_element("xpath", FATHER_NAME_XPATH).send_keys(father_name[i])
    while not get_mother_name(driver):
        pass
    driver.find_element("xpath", MOTHER_NAME_XPATH).send_keys(mother_name[i])
    while not get_gender(driver):
        pass
    Select(driver.find_element("xpath", GENDER_DROPDOWN_XPATH)).select_by_visible_text(gender_dict.get(gender[i]))
    while not get_ph(driver):
        pass
    driver.find_element("xpath", PHONE_NUMBER_XPATH).send_keys(ph_no[i])
    while not get_reg(driver):
        pass
    driver.find_element("xpath", REGISTRATION_XPATH).send_keys(reg_no[i])
    while not get_roll(driver):
        pass
    driver.find_element("xpath", ROLL_NO_XPATH).send_keys(roll_no[i])
    while not get_class(driver):
        pass
    Select(driver.find_element("xpath", CLASS_XPATH)).select_by_visible_text(str(Class[i]) + " " + section[i])
    while not click(driver):
        pass
    while not aleart(driver):
        pass
    a = driver.switch_to.alert.accept()
    time.sleep(3)
    print(first_name[i]+" "+str(i))
