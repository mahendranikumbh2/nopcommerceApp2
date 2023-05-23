from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseurl = ReadConfig.getApplicationURL()
    path = ".//testData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********** Test_002_DDT_Login **********")
        self.logger.info("********** Verifying Login DDT test **********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getrowCount(self.path, 'Sheet1')
        print("Number of Rows in a Excel :", self.rows)

        lst_status = []    # This is Empty list variable

        for r in range(2, self.rows+1):   # how many rows we get which is stored in self.rows variable so why we return this variable inside the range function
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("********** Passed **********")
                    self.lp.ClickLogout();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                     self.logger.info("********** Failed **********")
                     self.lp.ClickLogout();
                     lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                   self.logger.info("********** Failed **********")
                   lst_status.append("Fail")
                elif self.exp == "Fail":
                     self.logger.info("********** Passed **********")
                     lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test Failed ****")
            self.driver.close()
            assert False

        self.logger.info("********** End of the Login DDT Test *********")
        self.logger.info("********** Completed Test_002_DDT_Login *********")




