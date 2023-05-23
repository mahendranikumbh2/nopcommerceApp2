import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:   # this is a one test case
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsereMail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):  # this is a one test method

        self.logger.info("********** Test_001_Login ********** ")
        self.logger.info("********** Verify HomePage Title ********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title  # after launch the application title is capture thats why we write this (act_title = self.driver.title) statment
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** HomePage Title Test is Passed ********** ")

        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** HomePage Title Test is Failed ********** ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):   # this is a second test method
        self.logger.info("********** Verifying Login Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)  # bcz we already closed the application in test_homePageTitle method thats why we write self.driver.get(self.baseURL) this statment
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** Login Test is Passed ********** ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("********** Login Test is Failed ********** ")
            assert False





