import time
import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os


load_dotenv()

@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")

    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")

    request.cls.driver=driver
    request.cls.username=username
    request.cls.password=password

    yield driver
    driver.quit()

