import time
import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

@pytest.fixture(scope="class")
def setup():
    driver=webdriver.Chrome()
    driver.get("https://facebook.com")
    driver.maximize_window()
    yield driver
    driver.quit()