from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select for dropdown handling
import unittest
import csv

# Name, Age, Grade, Parent Name, Email, Phone

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_name_field(self):
        driver = self.driver

        valid_data = {
            "age": "10",
            "grade": "3",
            "parent_name": "Jane Doe",
            "email": "johndoe@example.com",
            "phone": "1234567890"
        }


        name_cases = [
            ["John Doe", True],
            ["", False],
            ["A" * 200, False],
            ["J", False],
        ]


        for name_case in name_cases:
            # flag to test unexpected outcome
            bug = False

            # adding input for reporting purpose
            csv_write_in = [name_case[0]]

            # navigate to register page
            self.driver.get("http://localhost:5000/register")

            
            # fill in valid data
            for valid_field, valid_value in valid_data.items():
                field_to_fill = driver.find_element(By.ID, valid_field)
                field_to_fill.send_keys(valid_value)

            # fill in name field
            name_field = driver.find_element(By.ID, "name")
            name_field.send_keys(name_case[0])

            # click the submit button
            submit_button = driver.find_element(By.CLASS_NAME, "btn")
            submit_button.click()

            try:
                # handle alert case
                alert = driver.switch_to.alert
                alert_message = alert.text
                alert.accept() # dismiss the alert

                # add to csv for reporting
                csv_write_in.append("Fail")
                csv_write_in.append(alert_message)

                # flag if unexpected outcome occured
                if name_case[1] == True: bug = True
            except:
                try:
                    # check if form submittion was valid
                    self.assertFalse(name_field.get_attribute("validity.valid"))
                    validation_message = name_field.get_attribute("validationMessage")
                    
                    # add to csv for reporting
                    csv_write_in.append("Fail")
                    csv_write_in.append(validation_message)
                    
                    # flag if unexpected outcome occured
                    if name_case[1] == True: bug = True

                except:
                    # if test was successful add for reporting
                    csv_write_in.append("Success")

                    # flag if unexpected outcome occured
                    if name_case[1] == False: bug = True

            # open the csv for writing
            with open('test_registration_name.csv', 'a', newline='') as name_file:
                writer = csv.writer(name_file)
                writer.writerow(csv_write_in)
            
            # add to bug csv if unexpected outcome
            if bug == True:
                with open('test_registration_bugs.csv', 'a', newline='') as bug_file:
                    csv_write_in.insert(0, 'name')
                    csv_write_in.insert(1, name_case[1])
                    writer = csv.writer(bug_file)
                    writer.writerow(csv_write_in)
            
    def test_age_field(self):
        driver = self.driver

        valid_data = {
            "name": "John Doe",
            "grade": "3",
            "parent_name": "Jane Doe",
            "email": "johndoe@example.com",
            "phone": "1234567890"
        }

        age_cases = [
            ["1", False],
            ["2", False],
            ["3", True],
            ["79", True],
            ["80", True],
            ["81", False],
            ["", False],
            ["abc", False]
        ]

        for age_case in age_cases:
            # flag to test unexpected outcome
            bug = False
            
            # adding input for reporting purpose
            csv_write_in = [age_case[0]]

            # navigate to register page
            self.driver.get("http://localhost:5000/register")

            # fill in valid data
            for valid_field, valid_value in valid_data.items():
                field_to_fill = driver.find_element(By.ID, valid_field)
                field_to_fill.send_keys(valid_value)

            # fill in age field
            age_field = driver.find_element(By.ID, "age")
            age_field.send_keys(age_case[0])

            # click the submit button
            submit_button = driver.find_element(By.CLASS_NAME, "btn")
            submit_button.click()

            try:
                # handle alert case
                alert = driver.switch_to.alert
                alert_message = alert.text
                alert.accept() # dismiss the alert

                # add to csv for reporting
                csv_write_in.append("Fail")
                csv_write_in.append(alert_message)
                
                # flag if unexpected outcome occured
                if age_case[1] == True: bug = True

            except:
                try:
                    # check if form submittion was valid
                    self.assertFalse(age_field.get_attribute("validity.valid"))
                    validation_message = age_field.get_attribute("validationMessage")

                    # add to csv for reporting
                    csv_write_in.append("Fail")
                    csv_write_in.append(validation_message)

                    # flag if unexpected outcome occured
                    if age_case[1] == True: bug = True

                except:
                    # if test was successful add for reporting
                    csv_write_in.append("Success")

                    # flag if unexpected outcome occured
                    if age_case[1] == False: bug = True

            # open the csv for writing
            with open('test_registration_age.csv', 'a', newline='') as age_file:
                writer = csv.writer(age_file)
                writer.writerow(csv_write_in)

            # add to bug csv if unexpected outcome
            if bug == True:
                with open('test_registration_bugs.csv', 'a', newline='') as bug_file:
                    csv_write_in.insert(0, 'age')
                    csv_write_in.insert(1, age_case[1])
                    writer = csv.writer(bug_file)
                    writer.writerow(csv_write_in)
    
    def test_parent_name_field(self):
        driver = self.driver

        valid_data = {
            "name": "John Doe",
            "age": "10",
            "grade": "3",
            "email": "johndoe@example.com",
            "phone": "1234567890"
        }

        parent_name_cases = [
            ["Jane Doe", True],
            ["", False],
            ["A" * 200, False],
            ["J", False]
        ]

        for parent_name_case in parent_name_cases:
            # flag to test unexpected outcome
            bug = False

            # adding input for reporting purpose
            csv_write_in = [parent_name_case[0]]

            # navigate to register page
            self.driver.get("http://localhost:5000/register")

            # fill in valid data
            for valid_field, valid_value in valid_data.items():
                field_to_fill = driver.find_element(By.ID, valid_field)
                field_to_fill.send_keys(valid_value)

            # fill in parent name field
            parent_name_field = driver.find_element(By.ID, "parent_name")
            parent_name_field.send_keys(parent_name_case[0])

            # click the submit button
            submit_button = driver.find_element(By.CLASS_NAME, "btn")
            submit_button.click()

            try:
                # handle alert case
                alert = driver.switch_to.alert
                alert_message = alert.text
                alert.accept()  # dismiss alert

                # add to csv for reporting
                csv_write_in.append("Fail")
                csv_write_in.append(alert_message)

                # flag if unexpected outcome occured
                if parent_name_case[1] == True: bug = True

            except:
                try:
                    # check if form submmittion was valid
                    self.assertFalse(parent_name_field.get_attribute("validity.valid"))
                    validation_message = parent_name_field.get_attribute("validationMessage")

                    # add to csv for reporting
                    csv_write_in.append("Fail")
                    csv_write_in.append(validation_message)

                    # flag if unexpected outcome occured
                    if parent_name_case[1] == True: bug = True

                except:
                    # if test was successful add for reporting
                    csv_write_in.append("Success")

                    # flag if unexpected outcome occured
                    if parent_name_case[1] == False: bug = True

            # open csv for writing
            with open('test_registration_parent_name.csv', 'a', newline='') as parent_name_file:
                writer = csv.writer(parent_name_file)
                writer.writerow(csv_write_in)

            # add to bug csv if unexpected outcome
            if bug == True:
                with open('test_registration_bugs.csv', 'a', newline='') as bug_file:
                    csv_write_in.insert(0, 'parent name')
                    csv_write_in.insert(1, parent_name_case[1])
                    writer = csv.writer(bug_file)
                    writer.writerow(csv_write_in)

    def test_email_field(self):
        driver = self.driver

        valid_data = {
            "name": "John Doe",
            "age": "10",
            "grade": "3",
            "parent_name": "Jane Doe",
            "phone": "1234567890"
        }

        email_cases = [
            ["johndoe@example.com", True],
            ["", False],
            ["invalid-email", False],
            ["johndoe@com", False],
            ["johndoe@.com", False],
            ["@example.com", False]
        ]

        for email_case in email_cases:
            # flag to test unexpected outcome
            bug = False

            # adding input for reporting purpose
            csv_write_in = [email_case[0]]

            # navigate to register page
            self.driver.get("http://localhost:5000/register")

            # fill in valid data
            for valid_field, valid_value in valid_data.items():
                field_to_fill = driver.find_element(By.ID, valid_field)
                field_to_fill.send_keys(valid_value)

            # fill in email field
            email_field = driver.find_element(By.ID, "email")
            email_field.send_keys(email_case[0])

            # click the submit
            submit_button = driver.find_element(By.CLASS_NAME, "btn")
            submit_button.click()

            try:
                # handle alert case
                alert = driver.switch_to.alert
                alert_message = alert.text
                alert.accept()  # dismiss alert

                # add to csv for reporting
                csv_write_in.append("Fail")
                csv_write_in.append(alert_message)

                # flag if unexpected outcome occured
                if email_case[1] == True: bug = True

            except:
                try:
                    # check if form submittion was valid
                    self.assertFalse(email_field.get_attribute("validity.valid"))
                    validation_message = email_field.get_attribute("validationMessage")

                    # add to csv for reporting
                    csv_write_in.append("Fail")
                    csv_write_in.append(validation_message)

                    # flag if unexpected outcome occured
                    if email_case[1] == True: bug = True

                except:
                    # if test was successful add for reporting
                    csv_write_in.append("Success")

                    # flag if unexpected outcome occured
                    if email_case[1] == False: bug = True

            # open the csv for writing
            with open('test_registration_email.csv', 'a', newline='') as email_file:
                writer = csv.writer(email_file)
                writer.writerow(csv_write_in)

            # add to bug csv if unexpected outcome
            if bug == True:
                with open('test_registration_bugs.csv', 'a', newline='') as bug_file:
                    csv_write_in.insert(0, 'email')
                    csv_write_in.insert(1, email_case[1])
                    writer = csv.writer(bug_file)
                    writer.writerow(csv_write_in)
    
    def test_phone_field(self):
        driver = self.driver

        valid_data = {
            "name": "John Doe",
            "age": "10",
            "grade": "3",
            "parent_name": "Jane Doe",
            "email": "johndoe@example.com"
        }

        phone_cases = [
            ["1234567890", True],
            ["", False],
            ["123", False],
            ["abcdefghij", False],
            ["123-456-7890", True],
            ["123.456.7890", True],
            ["(123) 456-7890", True]
        ]

        for phone_case in phone_cases:
            # flag to test unexpected outcome
            bug = False

            # adding input for reporting purpose
            csv_write_in = [phone_case[0]]

            # navigate to register page
            self.driver.get("http://localhost:5000/register")

            # fill in valid data
            for valid_field, valid_value in valid_data.items():
                field_to_fill = driver.find_element(By.ID, valid_field)
                field_to_fill.send_keys(valid_value)

            # fill in phone field
            phone_field = driver.find_element(By.ID, "phone")
            phone_field.send_keys(phone_case[0])

            # click submit button
            submit_button = driver.find_element(By.CLASS_NAME, "btn")
            submit_button.click()

            try:
                # handle alert case
                alert = driver.switch_to.alert
                alert_message = alert.text
                alert.accept()  # dismiss alert

                # add to csv for reporting
                csv_write_in.append("Fail")
                csv_write_in.append(alert_message)

                # flag if unexpected outcome occured
                if phone_case[1] == True: bug = True

            except:
                try:
                    # check if form submittion was valid
                    self.assertFalse(phone_field.get_attribute("validity.valid"))
                    validation_message = phone_field.get_attribute("validationMessage")

                    # add to csv for reporting
                    csv_write_in.append("Fail")
                    csv_write_in.append(validation_message)

                    # flag if unexpected outcome occured
                    if phone_case[1] == True: bug = True

                except:
                    # if test was successful add for reporting
                    csv_write_in.append("Success")

                    # flag if unexpected outcome occured
                    if phone_case[1] == False: bug = True

            # open csv for writing
            with open('test_registration_phone.csv', 'a', newline='') as phone_file:
                writer = csv.writer(phone_file)
                writer.writerow(csv_write_in)

            # add to bug csv if unexpected outcome
            if bug == True:
                with open('test_registration_bugs.csv', 'a', newline='') as bug_file:
                    csv_write_in.insert(0, 'phone number')
                    csv_write_in.insert(1, phone_case[1])
                    writer = csv.writer(bug_file)
                    writer.writerow(csv_write_in)

    def test_grade_field(self):
        driver = self.driver

        valid_data = {
            "name": "John Doe",
            "age": "10",
            "parent_name": "Jane Doe",
            "email": "johndoe@example.com",
            "phone": "1234567890"
        }

        grade_cases = [
            ["Kindergarten", True],
            ["1", True],
            ["2", True],
            ["3", True],
            ["4", True],
            ["5", True],
            ["6", True],
            ["7", True],
            ["8", True],
            ["", False],
            ["9", False],
            ["InvalidGrade", False]
        ]

        for grade_case in grade_cases:
            # flag to test unexpected outcome
            bug = False

            # adding input for reporting purpose
            csv_write_in = [grade_case[0]]

            # navigate to register page
            self.driver.get("http://localhost:5000/register")

            # fill in valid data
            for valid_field, valid_value in valid_data.items():
                field_to_fill = driver.find_element(By.ID, valid_field)
                field_to_fill.send_keys(valid_value)

            # fill in grade field
            grade_field = driver.find_element(By.ID, "grade")
            grade_field.send_keys(grade_case[0])

            # click submit button
            submit_button = driver.find_element(By.CLASS_NAME, "btn")
            submit_button.click()

            try:
                # handle alert case
                alert = driver.switch_to.alert
                alert_message = alert.text
                alert.accept()  # dismis alert

                # add to csv for reporting
                csv_write_in.append("Fail")
                csv_write_in.append(alert_message)

                # flag if unexpected outcome occured
                if grade_case[1] == True: bug = True

            except:
                try:
                    # check if form submittion was valid
                    self.assertFalse(grade_field.get_attribute("validity.valid"))
                    validation_message = grade_field.get_attribute("validationMessage")

                    # add to csv for reporting
                    csv_write_in.append("Fail")
                    csv_write_in.append(validation_message)

                    # flag if unexpected outcome occured
                    if grade_case[1] == True: bug = True

                except:
                    # if test was successful add for reporting
                    csv_write_in.append("Success")

                    # flag if unexpected outcome occured
                    if grade_case[1] == False: bug = True

            # open csv for writing
            with open('test_registration_grade.csv', 'a', newline='') as grade_file:
                writer = csv.writer(grade_file)
                writer.writerow(csv_write_in)

            # add to bug csv if unexpected outcome
            if bug == True:
                with open('test_registration_bugs.csv', 'a', newline='') as bug_file:
                    csv_write_in.insert(0, 'grade')
                    csv_write_in.insert(1, grade_case[1])
                    writer = csv.writer(bug_file)
                    writer.writerow(csv_write_in)

        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
