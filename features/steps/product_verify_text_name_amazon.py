from selenium.webdriver.common.by import By
from behave import given, when, then


selected_products = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li/div/div[not(@class='a-section a-padding-extra-large a-text-center')]")


@then( 'verify {search_word} in products' )
def verify_text_products(context,search_word):
    elements = context.driver.find_elements(*selected_products)

    for element in elements:
        assert search_word in element.text,f'Expected {search_word}, but got {element.text}'
