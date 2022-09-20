class pageObjects():
    url1 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    # Login Page
    UserName = ".//input[@name='username']"
    PassWord = ".//input[@name='password']"
    Login_button = "//button[@type='submit']"

    #Add button
    add_button="//button[@type='button'] [@class='oxd-button oxd-button--medium oxd-button--secondary']"

    #Input to Add employee
    firstname=".//input[@name='firstName']"
    middlename=".//input[@name='middleName']"
    lastname=".//input[@name='lastName']"
    save_button="//button[@type='submit'][@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    #Admin page in the left panel
    Admin_tab="//a[@class='oxd-main-menu-item'][@href='/web/index.php/admin/viewAdminModule']"
    #Add button in Admin page
    Admin_Add_button="//button[@type='button'][@class='oxd-button oxd-button--medium oxd-button--secondary']"

    #Add user elements
    Employee_name = "//input[@placeholder='Type for hints...']"
    Userrole_Select = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i"
    Userrole_admin = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]"
    Main_status = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]"
    Main_username = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input"
    Admin_Password = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"
    Admin_Confirm_Password ="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input"
    Admin_save_button = "//button[@type='submit'][text() = ' Save ']"
    username_dropdown = "//form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/span"
    status_enabled = "//form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/span"
    add_user_save_button = "//button[@type='submit'][text() = ' Save ']"
    admin_search_username= "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.oxd-table-filter > div.oxd-table-filter-area > form > div.oxd-form-row > div > div:nth-child(1) > div > div:nth-child(2) > input"
    admin_search_button = "//button[@type='submit']"
    username_from_table = "//div/div[2]/div[3]/div/div[2]/div/div/div[2]/div"
    main_user_dropdown = "//span[@class='oxd-userdropdown-tab']"
    logout = "//a[contains(., 'Logout')]"