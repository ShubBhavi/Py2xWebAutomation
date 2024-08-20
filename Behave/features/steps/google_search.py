from selenium import webdriver
from behave import given,when,then
from selenium.webdriver.common.by import By

@given('I am on the google search page')
def step_impl(context):
    context.driver=webdriver.Chrome()
    context.driver.get("https://google.com")
@when('I search for the "{search_term}"')
def step_impl(context,search_term):
    search_box=context.driver.find_element(By.NAME,"q")
    search_box.send_keys(search_term)
    search_box.submit()

@then('I should see the "{expected_term}" as a result')
def step_impl(context,expected_term):
    assert expected_term in context.driver.page_source
    context.driver.quit()