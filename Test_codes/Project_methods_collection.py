import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.webdriver.common.by import By
from Testdata.Login_data import data
from Testdata.pageObjects import pageObjects


user_name = data().username
pass_word = data().password
Firstname = data().firstname
Middlename = data().middlename
Lastname = data().lastname
main_username = data().Main_username
User_password = data().user_password

Username = pageObjects().UserName
Password = pageObjects().PassWord
LoginButton = pageObjects().Login_button
addButton = pageObjects().add_button
first_name = pageObjects().firstname
middle_name = pageObjects().middlename
last_name = pageObjects().lastname
save_button = pageObjects().save_button
admin_tab = pageObjects().Admin_tab
admin_add_button = pageObjects().Admin_Add_button
userrole_select = pageObjects().Userrole_Select
userrole_admin = pageObjects().Userrole_admin
Main_username = pageObjects().Main_username
employee_name = pageObjects().Employee_name
main_status = pageObjects().Main_status
admin_password = pageObjects().Admin_Password
admin_confirm_password = pageObjects().Admin_Confirm_Password
# admin_save_button = pageObjects().Admin_save_button
Username_dropdown = pageObjects().username_dropdown
Status_enabled = pageObjects().status_enabled
Add_user_save_button = pageObjects().add_user_save_button
Admin_search_username = pageObjects().admin_search_username
Admin_search_button = pageObjects().admin_search_button
Username_from_table = pageObjects().username_from_table
Main_user_dropdown = pageObjects().main_user_dropdown
Logout = pageObjects().logout

driver = webdriver.Firefox()


class Project:
    def __init__(self):
        self.driver = None

    def launch(self, url):
        # getting input from the Login data file
        # launch url
        try:
            driver.get(url)
            # time.sleep(5)
            print("URL is launched Successfully")
        except NSEE:
            print("Error in launching URL")
            driver.quit()

    def login(self):

        try:
            driver.find_element(by=By.XPATH, value=Username).send_keys(user_name)
            driver.find_element(by=By.XPATH, value=Password).send_keys(pass_word)
            # click on Login
            driver.find_element(by=By.XPATH, value=LoginButton).click()
            print("Login Successful")
        except NSEE:
            print("Error in Login page")
            driver.quit()

    def PIM_click_add_button(self):
        # navigate to PIM page
        driver.implicitly_wait(10)
        try:
            driver.find_element(by=By.XPATH, value="//a[@href='/web/index.php/pim/viewPimModule']").click()
            # clicking the Add button
            driver.find_element(by=By.XPATH, value=addButton).click()
            print("Add Employee page opened")
        except NSEE:
            print("Error in Clicking Add button")

    def PIM_Add_Employee(self):
        # Provide inputs to create employee
        # input details
        try:
            driver.find_element(by=By.XPATH, value=first_name).send_keys(Firstname)
            driver.find_element(by=By.XPATH, value=middle_name).send_keys(Middlename)
            driver.find_element(by=By.XPATH, value=last_name).send_keys(Lastname)
            driver.implicitly_wait(5)
            # click on save button
            driver.find_element(by=By.XPATH, value=save_button).click()
            driver.implicitly_wait(5)
            # self.driver.save_screenshot("add employee success")
            print("Add Employee Successful")
        except NSEE:
            print("Error in Adding Employee")

    def navigate_to_admin(self):
        # Navigate to Admin section using left side panel
        try:
            driver.find_element(by=By.XPATH, value=admin_tab).click()
            driver.implicitly_wait(5)
            print("Navigated to Admin Page")
        except NSEE:
            print("Error in navigating to Admin page")

    def Add_button_Admin(self):
        # click on add button in the Admin page
        try:
            driver.find_element(by=By.XPATH, value=admin_add_button).click()
            driver.implicitly_wait(5)
            print("Add button in Admin page is clicked successfully")
        except NSEE:
            print("Error in clicking Add button in Admin page")

    def add_new_user(self):
        # Add a new user by using above created employee name by keeping the status as enabled
        # Click on Add button
        try:
            driver.find_element(by=By.XPATH, value=userrole_select).click()
            driver.find_element(by=By.XPATH, value=userrole_admin).click()
            # action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).perform()
            driver.find_element(by=By.XPATH, value=employee_name).send_keys(Firstname)
            time.sleep(5)
            driver.find_element(by=By.XPATH, value=Username_dropdown).click()
            # action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).perform()
            driver.find_element(by=By.XPATH, value=main_status).click()
            driver.find_element(by=By.XPATH, value=Status_enabled).click()
            # action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).perform()
            driver.find_element(by=By.XPATH, value=Main_username).send_keys(main_username)
            driver.find_element(by=By.XPATH, value=admin_password).send_keys(User_password)
            driver.find_element(by=By.XPATH, value=admin_confirm_password).send_keys(User_password)
            time.sleep(5)
            driver.find_element(by=By.XPATH, value=Add_user_save_button).click()
            # self.driver.save_screenshot("Add userrole successful")
            print("User role added successfully")
        except NSEE:
            print("Error in adding new userrole and status in admin page")

    def search_user(self):
        # Search the given Username in add new user function
        try:
            driver.find_element(by=By.CSS_SELECTOR, value=Admin_search_username).send_keys(main_username)
            driver.find_element(by=By.XPATH, value=Admin_search_button).click()
            print("Search performed successfully")
        except NSEE:
            print("Error in Searching the Created user")

    def verify_created_user(self):
        # Verify the created user is displayed while Searching
        text = driver.find_element(by=By.XPATH, value=Username_from_table).text
        print("Username is table after searching is " + text)
        if text == main_username:
            print("User created and verified")
        else:
            print("User not verified")

    def logout(self):
        # Logout from the page
        try:
            driver.find_element(by=By.XPATH, value=Main_user_dropdown).click()
            driver.find_element(by=By.XPATH, value=Logout).click()
            print("Logged out")
        except NSEE:
            print("Error in logging out")

    def login_with_created_user(self):
        # Login with the newly created user
        try:
            driver.find_element(by=By.XPATH, value=Username).send_keys(main_username)
            driver.find_element(by=By.XPATH, value=Password).send_keys(User_password)
            # click on Login
            driver.find_element(by=By.XPATH, value=LoginButton).click()
            print("Login with new added user is successful")
        except NSEE:
            print("Newly created user in not getting logged in")

