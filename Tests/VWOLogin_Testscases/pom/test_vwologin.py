import time

from selenium import webdriver
import pytest
from Tests.Pageobjects.loginPage import LoginPage
from Tests.Pageobjects.DashboardPage import DashboardPage
from dotenv import load_dotenv
import os
load_dotenv()
class Test_Login():

    @pytest.mark.negative
    @pytest.mark.usefixtures("setup")
    def test_vwo_login_neg(self,setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.login_to_vwo(user="admin", pwd="admin")
        time.sleep(5)
        error_msg = login_page.err_msg_text()
        assert error_msg == "Your email, password, IP address or location did not match"
        print(error_msg)


    @pytest.mark.positive
    @pytest.mark.usefixtures("setup")
    def test_vwo_login(self,setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.login_to_vwo(user="yzbdueuxgt@txcct.com",pwd="Shubham@1980")
        time.sleep(10)
        assert "Dashboard" in driver.title
        time.sleep(6)
