from selenium.common.exceptions import WebDriverException
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


add_cart = (By.CSS_SELECTOR, "input#add-to-cart-button")
cart1 = (By.ID, "nav-cart")
#cart2 = (By.XPATH, "//span[@id='attach-sidesheet-view-cart-button-announce']")
cart = (By.CSS_SELECTOR, "form#attach-view-cart-button-form ")
continue_icon = (By.CSS_SELECTOR, "span.a-button-inner button#attachSiNoCoverage-announce")
item_search = (By.XPATH,"//img[contains(@alt,'Simple Mobile - Apple iPhone 11 Pro (64GB) - Midnight Green')]")
check_item = (By.CSS_SELECTOR, "span#a-autoid-0-announce")

@allure.feature('Verify shopping cart')
@allure.story('Check items in shopping cart')
#blocker, critical, normal, miner, trivial
@allure.severity('critical')
@then('Click on  item')
def click_search_icon(context):
    with allure.step('Click on  item and screenshot'):
        allure.attach(context.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    context.driver.find_element(*item_search).click()
    sleep(1)


@then('Add to cart')
def click_search_icon(context):
    context.driver.find_element(*add_cart).click()
    #sleep(1)
    try:
        context.driver.find_element( *continue_icon ).click()
        #sleep(1)
    except WebDriverException:
        print( 'No continue button' )


@then('Click on cart icon btn' )
def click_card_icon(context):
    try:
        context.driver.find_element( *cart1 ).click()
        #sleep(4)
    except WebDriverException:
        context.driver.find_element( *cart ).click()
        #sleep (4)


#    context.driver.find_element(*cart1).click()
#    sleep(1)

@then('Verify shopping cart has {search_word} item')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*check_item).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)