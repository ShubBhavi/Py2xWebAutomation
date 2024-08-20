import time

from selenium import webdriver
import pytest
from Tests.Pageobjects.loginPage import LoginPage
from Tests.Pageobjects.DashboardPage import DashboardPage
from dotenv import load_dotenv


@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver

@pytest.mark.negative
def test_vwo_login_neg(setup):
    driver=setup
    login_page=LoginPage(driver)
    login_page.login_to_vwo(user="admin",pwd="admin")
    time.sleep(5)
    error_msg=login_page.err_msg_text()
    assert error_msg=="Your email, password, IP address or location did not match"
    print(error_msg)

@pytest.mark.positive
def test_vwo_login(setup):
    driver=setup
    driver.get("https://app.vwo.com")
    login_page=LoginPage(driver)
    login_page.login_to_vwo(user="yzbdueuxgt@txcct.com",pwd="Shubham@1980")
    time.sleep(10)

    assert "Dashboard" in driver.title
    time.sleep(6)

