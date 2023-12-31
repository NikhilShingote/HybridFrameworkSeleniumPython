import time

import pytest
import string
import random

from selenium.webdriver.common.by import By

from PageObjects.LoginPage import Loginpage
from PageObjects.Addcustomerpage import AddCustomer
from Utilities.read_properties import ReadConfig
from Utilities.customLogger import LogGen

class Test_003_AddCustomer:
    baseurl = ReadConfig.getApplicationurl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*************** Test 003 Add Customer **************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.logger.info("**************** Login Successfull *******************")

        self.logger.info("**************** Starting add customer test *******************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("********* Providing on customerinfo ************")
        time.sleep(2)
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("7/05/1985")  # Format: D/MM/YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()

        self.logger.info("******** Saving Customer Info ***********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** Add Customer Test Passed ********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.info("********** Add Customer Test Failed ***************")
            assert  True == False

        self.driver.close()
        self.logger.info("********************** Ending Add Customer Test **********************")
def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

