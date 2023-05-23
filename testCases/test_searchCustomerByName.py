import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_searchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsereMail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("********** searchCustomerByName_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** starting search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersSubMenu()

        self.logger.info("********** searching Customer By First Name **********")

        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("john")
        searchcust.setLastName("kevin")
        searchcust.clickSearch()
        time.sleep(3)

        status = searchcust.searchCustomerByName("john kevin")
        assert True == status

        self.logger.info("********** Test_searchCustomerByName_005 is Finished **********")
        self.driver.close()















