from selenium.webdriver.common.by import By
from selenium import webdriver

class DashboardPage():

    def __init__(self, driver):
        self.driver = driver

    name=(By.XPATH,"//span[@data-qa='lufexuloga']")


    def get_name(self):
        return self.driver.find_element(DashboardPage.name)


    def name_text(self):
        return self.get_name().text


