from selenium.webdriver.chrome.service import Service

from Utilities.orangehrm_read_properties import ReadConfigHRM
from PageObjects.Login_for_OrangeHRM import LoginHRM
from selenium import webdriver


class Testcase_005:
    OrangeHRM_url = ReadConfigHRM.read_orangehrm_url()
    hrm_username = ReadConfigHRM.getUsername()
    hrm_password = ReadConfigHRM.getPassword()

    def orange_hrm_title(self, setup):

        self.driver = setup
        self.driver.get(self.OrangeHRM_url)
        self.lpa = LoginHRM(self.driver)
        self.lpa.enterUsername(self.hrm_username)
        self.lpa.enterPassword(self.hrm_password)
        self.lpa.clickLogin()

        act_title = self.driver.title
        if act_title == "OrangeHRM":
            self.lpa.clickProfile()
            self.lpa.clickProfile()
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "OrangeHRM_test_login_SS.png")
            self.driver.close()
            assert False
