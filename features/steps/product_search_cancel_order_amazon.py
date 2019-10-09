from selenium.webdriver.common.by import By
from behave import then
from time import sleep

link_find = (By.XPATH, "//div[@class='a-search a-span12']/input[@id='helpsearch']")
search_click = (By.XPATH, "//div[@class='a-column a-span2 a-span-last']/span[@id='helpSearchSubmit']")
word_found = (By.XPATH, "//div[@class='help-content']/h1")


@then( 'Input {search_word} into search field' )
def input_search(context, search_word):
    search = context.driver.find_element( *link_find )
    search.clear()
    search.send_keys( search_word )
    sleep( 4 )


@then( 'Click on search icon' )
def click_search_icon(context):
    context.driver.find_element( *search_click ).click()
    sleep( 1 )


@then( 'Product results {search_word} are shown' )
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element( *word_found ).text
    assert search_word in results_msg
#"Expected word '{}' in message, but got '{}'".format( search_word, results_msg )
