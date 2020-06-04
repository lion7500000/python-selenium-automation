from behave import given,then, when
from selenium.webdriver.common.by import By

@given ('Open Ebay page')
def open_ebay_page(context):
    context.app.main_page_ebay.open_page2()

@when ('Input {text} in Ebay_search field and click')
def input_text_search (context,text):
    context.app.main_page_ebay.input_text_search(text)

@when ('click on Ebay_search field')
def click_serch_btn(context):
    context.app.main_page_ebay.click_serch_btn()

@then ('Verify {text} is present on the page')
def verify_EBAY_serch_product(context,text):
    context.app.search_ebay_page.verify_EBAY_serch_product(text)