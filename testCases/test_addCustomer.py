import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsereMail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):  # here pass setup to this method so first execute setup method and execute this function one by one

        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("********** Login Successful **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersSubMenu()
        self.addcust.clickOnAddNew()

        self.logger.info("********** providing customer info **********")


        self.email = random_generator() +' '+ "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setcustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Mahendra")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("14/08/1998")  # Format: DD/MM/YYYY
        self.addcust.setCompanyName("BusyQA")
        self.addcust.setAdminContent("This is for testing....")
        self.addcust.clickOnSave()

        self.logger.info("********** Saving customer info **********")


        self.logger.info("********** add customer validation started **********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** add customer Test Passed **********")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_AddCustomer_scr.png")
            self.logger.info("********** add customer Test Failed **********")
            assert True == False


        self.driver.close()
        self.logger.info("********** Ending Test_003_AddCustomer Test **********")

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits): # this is user defined function and this function return some randome data
        return ''.join(random.choice(chars) for x in range(size))





