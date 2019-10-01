from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#amazon = 'https://www.amazon.com'
SEARCH_SUBMIT1 = (By.XPATH, "//a[@id='nav-orders']/span[@class='nav-line-2']")
RESULTS_FOUND_MESSAGE1 = (By.XPATH, "//h1[@class='a-spacing-small']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.maximize_window()
    context.driver.get('https://www.amazon.com')


@then('Click on search item')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT1).click()
    sleep(1)

@then('Product results for {search_word} are it')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE1).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)