from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

deals_under_25 = (By.CSS_SELECTOR, "a[aria-label*='deals under $25']")
todays_deals = (By.CSS_SELECTOR, "h1 div.gbh1-bold")
add_to_card = (By.XPATH,"//span[@class='a-button-inner']/button[@type='button' and contains(text(),'Add to Cart')]")
card = (By.CSS_SELECTOR,"span.nav-cart-count")

@when('Store original windows')
def store_current_windows(context):
    context.original_window= context.driver.current_window_handle
    context.old_windows= context.driver.window_handles
    #print('\noriginal_window\n', context.original_window)
    #print('\nold_windows\n',context.old_windows)

@when('Click to open Deals under $25')
def click_to_open_deala_under_25(context):
    context.driver.find_element(*deals_under_25).click()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    #wait new window
    context.driver.wait.until(EC.new_window_is_opened)

    current_window= context.driver.window_handles
    #print('\ncurrent_window\n',current_window)

    new_window = current_window
    for old_window in context.old_windows:
        new_window.remove(old_window)
    #print('\nnew_window\n',new_window)

    context.driver.switch_to_window(new_window[0])

@then ('Search {search_text} are shown')
def todays_deals_present(context,search_text):
    actual_text = context.driver.find_element(*todays_deals).text
    assert search_text == actual_text, "Expected word '{}' in message, but got '{}'".format( search_text, actual_text )

@then('steps to put any product into a cart')
def put_product_to_card(context):
    context.driver.find_element(*add_to_card).click()
    #sleep(7)
@then('User can close new window and switch back to original')
def close_and_switch_window_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)

@then('Add a step to refresh the page')
def refresh_page(context):
    context.driver.refresh()

@then('Add a step to verify cart has {search_number} item')
def verify_cart(context,search_number):
    serch_result = context.driver.find_element(*card).text
    assert search_number in serch_result, "Expected item '{}' in message, but got '{}'".format( search_number, serch_result )


