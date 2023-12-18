from selenium.webdriver.common.by import By


class SearchCustomer:
    txt_email_search_id = "SearchEmail"
    txt_firstname_id = "SearchFirstName"
    txt_lastname_id = "SearchLastName"
    btn_search_id = "search-customers"
    table_xpath = "//table[@id='customers-grid']"
    search_table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_col_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_search_id).clear()
        self.driver.find_element(By.ID, self.txt_email_search_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txt_firstname_id).clear()
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txt_lastname_id).clear()
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def getNoOfRows(self):
        print("This are the number of rows: ", len(self.driver.find_elements(By.XPATH, self.table_rows_xpath)))
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getNoofColumns(self):
        print(len(self.driver.find_elements(By.XPATH, self.table_col_xpath)))
        return len(self.driver.find_elements(By.XPATH, self.table_col_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        '''for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text'''
        email_id = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr/td[2]").text
        if email_id == email:
            flag = True

        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
            break
        return flag
