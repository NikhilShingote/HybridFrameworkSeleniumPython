import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import Loginpage
from Utilities.read_properties import ReadConfig
from Utilities.customLogger import LogGen


class Testcase:
    base_url = ReadConfig.getApplicationurl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepage_title(self, setup):

        self.logger.info("************************** Test Case 001 Login ***************************")
        self.logger.info("************************** Verify Homepage Title ***************************")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("************************** Title Test is Passed ***************************")
            assert True
        else:
            self.driver.close()
            self.logger.error("************************** Title Test is Failed ***************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************************** Verify Login Test ***************************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
