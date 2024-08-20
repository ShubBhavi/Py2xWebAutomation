import time

from selenium import webdriver
import pytest
from test.pageobject.login_facebook import Login_Facebook
from dotenv import load_dotenv
import os
load_dotenv()


class Test_Login_FB():

    @pytest.mark.positive
    @pytest.mark.usefixtures("setup")
    def test_login(self,setup):
        driver=setup
        login_page=Login_Facebook(driver)
        login_page.login_to_facbook(user="",pwd="")
        time.sleep(10)
        name=login_page.verify()
        print(name)

