import string
import time

from selenium.webdriver.support.select import Select

from read_csv import get_data
from Utils import get_driver
from Constants import ADD_SUBJECT_BUTTON, SESSION_SELECT_XPATH, SUBJECT_NAME_XPATH, CLASS_SELECT_XPATH, \
    SUBJECT_TYPE_XPATH, TEACHER_XPATH


def aleart(driver):
    try:
        driver.switch_to.alert
        return True
    except Exception:
        return False


def click(driver):
    try:
        driver.execute_script("document.getElementsByClassName('primary-cta w-100')[0].click()")
        return True
    except Exception:
        return False


def subjectType(driver):
    try:
        Select(driver.find_element("xpath", SUBJECT_TYPE_XPATH))
        return True
    except Exception:
        return False


def select_teacher(driver):
    try:
        Select(driver.find_element("xpath", TEACHER_XPATH))
        return True
    except Exception:
        return False


def isClickAble(driver):
    try:
        driver.find_element('xpath', ADD_SUBJECT_BUTTON)
        return True
    except Exception:
        return False


def canSeletectSession(driver):
    try:
        driver.find_element('xpath', SESSION_SELECT_XPATH)
        return True
    except Exception:
        return False


def canEnterSubject(driver):
    try:
        driver.find_element('xpath', SUBJECT_NAME_XPATH)
        return True
    except Exception:
        return False


def selectSubject(driver):
    try:
        Select(driver.find_element("xpath", CLASS_SELECT_XPATH))
        return True
    except Exception:
        return False


Class, teacher_list, section, subject, subject_type, teacher_name, teacher_email = get_data()
driver = get_driver()
is_new_page = True
for i in range(0, len(Class)):
    if Class[i] == "LKG" or Class[i] == "NURSERY" or i == 0:
        continue
    if is_new_page:
        while not isClickAble(driver):
            pass
        driver.find_element('xpath', ADD_SUBJECT_BUTTON).click()
    while not canSeletectSession(driver):
        pass
    session = Select(driver.find_element('xpath', SESSION_SELECT_XPATH))
    session.select_by_value("22-23")
    while not canEnterSubject(driver):
        pass
    subject_name = driver.find_element('xpath', SUBJECT_NAME_XPATH)
    subject_name.clear()
    subject_name.send_keys(subject[i])
    while not selectSubject(driver):
        pass
    class_select = Select(driver.find_element("xpath", CLASS_SELECT_XPATH))
    class_select.select_by_visible_text(str(Class[i]) + " " + section[i])
    while not select_teacher(driver):
        pass
    teacher_select = Select(driver.find_element("xpath", TEACHER_XPATH))
    time.sleep(2)
    try:
        name = string.capwords(teacher_name[i]) + " " + "(" + teacher_email[i] + ")"
        teacher_select.select_by_visible_text(name)
        print(teacher_name[i])
    except Exception:
        try:
            name = teacher_name[i].upper() + " " + "(" + teacher_email[i] + ")"
            teacher_select.select_by_visible_text(name)
            print(teacher_name[i])
        except Exception:
            pass
    while not subjectType(driver):
        pass
    type_select = Select(driver.find_element("xpath", SUBJECT_TYPE_XPATH))

    type_select.select_by_visible_text(subject_type[i])

    while not click(driver):
        pass
    while not aleart(driver):
        pass
    a = driver.switch_to.alert
    text = a.text
    a = a.accept()

    if text == "Subject already Exists":
        is_new_page = False
    else:
        is_new_page = True
        print(i)
        print(subject[i])
        print(text)
