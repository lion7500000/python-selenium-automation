from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

word_found= (By.CSS_SELECTOR,"h1.sc-empty-cart-header")

@then ('verifies that {search_word} is present')
def verify_card_empty(context, search_word):
    result_card = context.driver.find_element( *word_found ).text
    assert search_word in result_card
    #context.app.search_results_page.verify_card_empty(search_word)

