
# Add Customer Page
from selenium.webdriver.common.by import By


class SearchCustomer:
    txt_searchEmail_id = "SearchEmail"
    txt_FirstName_id = "SearchFirstName"
    txt_LastName_id = "SearchLastName"
    btn_Search_id = "search-customers"

    tabl_SearchResult_xpath = "//*[@id='customers-grid_wrapper']/div[1]/div/div/div[1]/div/table"
    tabl_xpath = "//*[@id='customers-grid_wrapper']/div[2]"
    tabl_Rows_xpath = "//*[@id='customers-grid']/tbody/tr"
    tabl_Columns_xpath = "//*[@id='customers-grid']/tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, "self.txt_searchEmail_id").clear()
        self.driver.find_element(By.ID, "self.txt_searchEmail_id").send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, "self.txt_FirstName_id").clear()
        self.driver.find_element(By.ID, "self.txt_FirstName_id").send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, "self.txt_LastName_id").clear()
        self.driver.find_element(By.ID, "self.txt_LastName_id").send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, "self.btn_Search_id").click()

    def getNoOfRows(self):
        return len(self.driver.find_element(By.XPATH, "self.tabl_Rows_xpath"))

    def getNoOfColumns(self):
        return len(self.driver.find_element(By.XPATH, "self.tabl_Columns_xpath"))

    def searchCustomerByEmail(self, email):  # This method return as true or false means when we pass email that time record will present in the table so it return true otherwise false
        flag = False
        for r in range(1, self.getNoOfRows()+1): # so here i am counting no of rows bcz i need to check record in every rows wherever exctly is present.
            table = self.driver.find_element(By.XPATH, "self.tabl_xpath")
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
            return flag

    def searchCustomerByName(self, Name):  # This method return as true or false means when we pass email that time record will present in the table so it return true otherwise false
        flag = False   # here we just create variable and whoes value taking as False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, "self.tabl_xpath")
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text  # this is for name element present in third columns and we pass row as argument in loop means record(name)
            if name == Name:
                flag = True
                break
            return flag


















