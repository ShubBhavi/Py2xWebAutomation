from selenium.webdriver.common.by import By
from selenium import webdriver


class Login_Facebook():

    def __init__(self,driver):
        self.driver=driver

    username=(By.XPATH,"//input[@id='email']")
    password=(By.XPATH,"//input[@id='pass']")
    login=(By.NAME,"login")
    verification=(By.XPATH,"//span[contains(text(),'Shubham') and contains(text(),'ನಿಮ್ಮ')]")


    def get_email(self):
        return self.driver.find_element(*Login_Facebook.username)

    def get_password(self):
        return self.driver.find_element(*Login_Facebook.password)

    def get_login_button(self):
        return self.driver.find_element(*Login_Facebook.login)

    def verification_name(self):
        return self.driver.find_element(*Login_Facebook.verification)



    def login_to_facbook(self,user,pwd):
        self.get_email().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_login_button().click()


    def verify(self):
        return self.verification_name().text


