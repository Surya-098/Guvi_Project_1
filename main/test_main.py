import time
from Test_codes.Project_methods_collection import Project
from Testdata.pageObjects import pageObjects

url = pageObjects().url1
p = Project()



def test_1():
    # Step 1:Navigate to “https://opensource-demo.orangehrmlive.com/”
    p.launch(url)
    time.sleep(3)


def test_2():
    # Step 2:Login with below creds:Username - Admin,Password - admin123
    p.login()
    time.sleep(3)


def test_3():
    # Step 3:Navigate to PIM and create a new employee
    p.PIM_click_add_button()
    time.sleep(3)
    p.PIM_Add_Employee()
    time.sleep(5)


def test_4():
    # Step 4:Navigate to Admin section using left side panel
    p.navigate_to_admin()
    time.sleep(5)


def test_5():
    # Step 5:Add a new user by using above created employee name by keeping the status as enabled
    p.Add_button_Admin()
    time.sleep(5)
    p.add_new_user()
    time.sleep(10)


def test_6():
    # Step 6:Once the user is created search for the user in admin section
    p.search_user()
    time.sleep(5)


def test_7():
    # Step 7:Verify the user is created
    p.verify_created_user()
    time.sleep(5)


def test_8():
    # Step 8:Log out from application
    p.logout()
    time.sleep(5)


def test_9():
    # Step 9:Re Login to application using the above created user
    p.login_with_created_user()
