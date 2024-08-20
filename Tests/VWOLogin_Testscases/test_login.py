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
    return driver


def test_vwo_login(setup):
    driver=setup
    driver.get("https://app.vwo.com")
    login_page=LoginPage(driver)
    login_page.login_to_vwo(user="yzbdueuxgt@txcct.com",pwd="Shubham@1980")
    time.sleep(10)

    assert "Dashboard" in driver.title
    time.sleep(6)

