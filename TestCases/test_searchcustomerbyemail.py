from selenium.webdriver.common.by import By
import pytest
import time
from PageObjects.LoginPage import Loginpage
from PageObjects.Addcustomerpage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.read_properties import ReadConfig
from Utilities.customLogger import LogGen


class Test_004_Search_Customer_By_Email:
    baseurl = ReadConfig.getApplicationurl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("*************** Test 004 Search Customer **************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.logger.info("**************** Login Successfull *******************")

        self.logger.info("**************** Starting Search Customer test *******************")
        time.sleep(2)
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.search_cust = SearchCustomer(self.driver)
        self.search_cust.setEmail("james_pan@nopCommerce.com")
        self.search_cust.clickSearch()
        time.sleep(2)

        status = self.search_cust.searchCustomerByEmail("james_pan@nopCommerce.com")
        assert True == status
        self.logger.info("**************** TC Starting Search Customer test Finished *******************")
        self.driver.close()
