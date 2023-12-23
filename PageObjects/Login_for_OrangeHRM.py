from selenium.webdriver.common.by import By


class LoginHRM:
    txt_username = "username"
    txt_password = "password"
    btn_login_xpath = "//button[@type='submit']"
    profile_dropdown_xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    btn_Logout_xpath = "//a[@href='/web/index.php/auth/logout']"

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        self.driver.find_element(By.NAME, self.txt_username).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.NAME, self.txt_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def clickProfile(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_Logout_xpath).click()
