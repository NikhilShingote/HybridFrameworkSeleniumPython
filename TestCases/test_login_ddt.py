import time

import pytest

from PageObjects.LoginPage import Loginpage
from Utilities.read_properties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_002_DDT_Login:
    base_url = ReadConfig.getApplicationurl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************************** Login 002 DDT Test ***************************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Loginpage(self.driver)
        # we have to get username and password from excel file here
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

        # Empty list variable
        list_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(3)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** Passed *******")
                    self.lp.clicklogout()
                    list_status.append("Pass")
                    
                elif self.exp == "Fail":
                    self.logger.info("***** Failed *******")
                    self.lp.clicklogout()
                    list_status.append("Fail")

            if act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** Failed *******")
                    self.lp.clicklogout()

                elif self.exp == "Fail":
                    self.logger.info("***** Passed *******")
                    list_status.append("Pass")
        if "Fail" not in list_status:
            self.logger.info("***** Login DDT test Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT test Failed *****")
            self.driver.close()
            assert False