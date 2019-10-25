from selenium.webdriver.common.by import By
from behave import given, when, then


selected_products = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li/div/div[not(@class='a-section a-padding-extra-large a-text-center')]")


@then( 'Each product has a {search_word} price' )
def verify_text_products(context,search_word):
    product_elements = context.driver.find_elements(*selected_products)

    for product_element in product_elements:
        assert search_word in product_element.text,f'Expected {search_word} to be in element, but got {product_element.text}'
