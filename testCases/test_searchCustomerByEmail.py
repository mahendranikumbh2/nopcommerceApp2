import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_searchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsereMail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********** searchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** starting search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersSubMenu()

        self.logger.info("********** searching Customer By emailID **********")

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("kiyjcycyhjc676008@gmail.com")
        searchcust.clickSearch()
        time.sleep(3)

        status = searchcust.searchCustomerByEmail("kiyjcycyhjc676008@gmail.com")
        assert True == status

        self.logger.info("********** Test_searchCustomerByEmail_004 is Finished **********")
        self.driver.close()















