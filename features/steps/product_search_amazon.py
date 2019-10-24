from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#amazon = 'https://www.amazon.com'
SEARCH_SUBMIT1 = (By.XPATH, "//a[@id='nav-orders']/span[@class='nav-line-2']")
SEARCH_SUBMIT2 = (By.CSS_SELECTOR,"div.nav-search-submit")
customer_service = (By.CSS_SELECTOR,"a[href*='nav_cs_customerservice']")
card_icon = (By.CSS_SELECTOR,"a#nav-cart")
SEARCH_INPUT = (By.CSS_SELECTOR,"input#twotabsearchtextbox")


@given('Open Amazon page')
def open_amazon(context):
    #context.driver.maximize_window()
    context.driver.get('https://www.amazon.com')


@given('Open Amazonprime page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')
    #sleep(3)


@given('Open Amazon clothing page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BKFFFXL/?th=1')


@given ('Open Amazon wholefood page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

@when('Click on search item')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT1).click()
    #sleep(1)

@when('Click on Customer Service')
def click_search_icon(context):
    context.driver.find_element(*customer_service).click()
    #sleep(1)

@when('Click on cart icon')
def click_search_icon(context):
    context.driver.find_element(*card_icon).click()
    #sleep(1)

@when('Input {search_word} into amazon_search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    #sleep(4)

@when('Click on search icon_amazom')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT2).click()
    #sleep(1)