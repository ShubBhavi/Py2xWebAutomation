from selenium import webdriver
from behave import given,when,then
from selenium.webdriver.common.by import By

@given('open the app.vwo.com')
def step1(context):
    context.driver=webdriver.Chrome()
    context.driver.get("https://app.vwo.com")

@when('I enter the {username} and {password}')
def step2(context,username,password):
    search_box = context.driver.find_element(By.XPATH, "//input[@id='login-username']")
    search_box.send_keys(username)
    search_box2 = context.driver.find_element(By.XPATH, "//input[@id='login-password']")
    search_box2.send_keys(password)
    submit_box = context.driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    submit_box.click()

@then('I get the {message}')
def step3(context,message):
    error_message=context.driver.find_element(By.XPATH,"//div[@id='js-notification-box-msg']").text
    print(error_message)
    # assert message in error_message
