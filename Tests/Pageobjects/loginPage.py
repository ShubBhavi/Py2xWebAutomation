from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage():

    def __init__(self,driver):
        self.driver=driver

    #paggelocator and page actions
    username=(By.XPATH,"//input[@id='login-username']")
    password=(By.XPATH,"//input[@id='login-password']")
    login_button=(By.XPATH,"//button[@id='js-login-btn']")
    error_message=(By.XPATH,"//div[@id='js-notification-box-msg']")


    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)


    # Page Actions

    def login_to_vwo(self,user,pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_login_button().click()

    def err_msg_text(self):
        return self.get_error_message().text
