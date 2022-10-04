import pandas as pd
import string


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            # print(i)
            num += roman[s[i]]
            i += 1
    return num


# read an excel file and convert
# into a dataframe object
def get_data():
    df = pd.read_excel("DIS Edge Data.xlsx", "Subjects Data");
    # df.parse("Subjects Data")
    # show the dataframe
    # print(df.get("Subject Name"))
    subject = df.get("Subject Name").values.tolist()
    class_list = df.get("Class").values.tolist()
    section = df.get("Section").values.tolist()
    teacher_name = df.get("Teacher name").values.tolist()
    teacher_email = df.get("Teacher Email ID").values.tolist()
    subject_type = df.get("Subject Type").values.tolist()
    teacher_list = []
    Class = []
    for i in range(0, len(class_list)):
        if class_list[i] != "KG" and class_list[i] != "NURSERY":
            # print(class_list[i])
            Class.append(romanToInt(class_list[i]))
        else:
            Class.append(class_list[i])

        section[i] = section[i][1:-1]
    # print(len(subject))
    return Class, teacher_list, section, subject, subject_type,teacher_name,teacher_email

def get_student_data():
    df = pd.read_excel("DISE_Student_Data.xlsx")
    first_name = df.get("First Name").values.tolist()
    middle_name = df.get("Middle Name").values.tolist()
    last_name = df.get("Last Name").values.tolist()
    dob = df.get("Date of Birth").values.tolist()
    reg_no = df.get("Registration Number").values.tolist()
    father_name = df.get("Father Name").values.tolist()
    mother_name = df.get("Mother Name").values.tolist()
    ph_no = df.get("Phone Number").values.tolist()
    address = df.get("Address").values.tolist()
    gender = df.get("Gender").values.tolist()
    session = df.get("Session").values.tolist()
    Class = df.get("Class").values.tolist()
    section = df.get("Section").values.tolist()
    roll_no = df.get("Roll Number").values.tolist()
    return first_name,middle_name,last_name,dob,reg_no,father_name,mother_name,ph_no,address,gender,session,Class,section,roll_no