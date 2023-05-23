import time

from selenium.webdriver.common.by import By


class AddCustomer:
    linkCustomers_mainMenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    linkCustomers_subMenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btn_addNew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    text_email_xpath = "//*[@id='Email']"
    text_Paasword_xpath = "//*[@id='Password']"
    text_FirstName_xpath = "//*[@id='FirstName']"
    text_LastName_xpath = "//*[@id='LastName']"
    radioBtn_MaleGender_id = "Gender_Male"
    radioBtn_FemaleGender_id = "Gender_Female"
    text_dob_xpath = "//*[@id='DateOfBirth']"
    text_companyName_xpath = "//*[@id='Company']"
    lstBox_customerRole_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div/input"
    lstItem_Administrators_xpath = "//*[@id='1be304ee-3bfe-4978-b516-18963ce845e0']"
    lstItem_Guests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstItem_Registered_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    lstItem_Vendors_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    drop_ManagerOfVendor_xpath = "//*[@id='VendorId']"
    text_AdminComment_xpath = "//*[@id='AdminComment']"
    btn_Save_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, "self.linkCustomers_mainMenu_xpath").click()

    def clickOnCustomersSubMenu(self):
        self.driver.find_element(By.XPATH, "self.linkCustomers_subMenu_xpath").click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, "self.btn_addNew_xpath").click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, "self.text_email_xpath").send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, "self.text_Paasword_xpath").send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, "self.text_FirstName_xpath").send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, "self.text_LastName_xpath").send_keys(lname)

    def setcustomerRoles(self, role):
        self.driver.find_element(By.XPATH, "self.lstBox_customerRole_xpath").click()
        time.sleep(4)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, "self.lstItem_Registered_xpath")
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, "self.lstItem_Administrators_xpath")
        elif role == 'Guests':
            # here user can be Registered or Guests only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "self.lstBox_customerRole_xpath").click()  # this is wrong code plz improve this code # this code for removing register option so just click on cross btn on register and inspect.
            self.listitem = self.driver.find_element(By.XPATH, "self.lstItem_Guests_xpath")
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, "self.lstItem_Registered_xpath")
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, "self.lstItem_Vendors_xpath")
        else:
            self.listitem = self.driver.find_element(By.XPATH, "self.lstItem_Guests_xpath")
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, "self.drop_ManagerOfVendor_xpath"))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, "self.radioBtn_MaleGender_id").click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, "self.radioBtn_FemaleGender_id").click()
        else:
            self.driver.find_element(By.ID, "self.radioBtn_MaleGender_id").click()

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, "self.text_dob_xpath").send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, "self.text_companyName_xpath").send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, "self.text_AdminComment_xpath").send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, "self.btn_Save_xpath").click()





































