from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

RESULTS_FOUND_MESSAGE1 = (By.XPATH, "//h1[@class='a-spacing-small']")


@then('Product results for {search_word} are open')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE1).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)