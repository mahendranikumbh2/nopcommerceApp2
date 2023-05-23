import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:                                 # this is page object class we have to created for login page
    textbox_username_id = "Email"    # Locator # after got value of username this value(username value) pass in textbox_username_id locator.
    textbox_password_id = "Password"  # Locator
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"   # Locator
    link_logout_linktext = "Logout"    # Locator

    def __init__(self, driver):     # this constructor automatically run when object is created.
        self.driver = driver        # here we just initialized the driver and this self.driver are used to write all action method on this element.

    def setUserName(self, username):     # this is action method for username locator or attribute and here username as parameter which will pass from actual test cases
        self.driver.find_element(By.ID, self.textbox_username_id).clear()  # to access the textbox_username_id locator thats why we write self.driver.find_element this statment
        time.sleep(3)
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        time.sleep(3)
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def ClickLogout(self):   # we write all actions method for every locator
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

