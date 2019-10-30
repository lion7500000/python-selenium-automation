from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#locators
from selenium.webdriver.support.wait import WebDriverWait

Best_Sellers = (By.CSS_SELECTOR,"a[href*='bestsellers']")
top_menu = (By.XPATH,"//*[@id='zg_tabs']//li")
expected_page = (By.XPATH, "//*[@id='zg_banner_text_wrapper']")

@then ('click to Best Sellers menu')
def open_best_sellers_menu(context):
    menu = context.driver.find_element(*Best_Sellers)
    menu.click()

@then ('verify that new page opens')
def open_new_pages(context):
    expected_text= ['Amazon Best Sellers','Amazon Hot New Releases','Amazon Movers & Shakers','Amazon Most Wished For','Amazon Gift Ideas']
    best_sellers_menu = context.driver.find_elements(*top_menu)
    #print('\nbest_sellers_menu\n',best_sellers_menu )

    for x in range(len(best_sellers_menu)):
            best_sellers_menu = context.driver.find_elements( *top_menu )
            best_sellers_menu[x].click()
            actual_text = context.driver.find_element(*expected_page).text
            #print( '\nactual_text\n', actual_text )
            assert actual_text == expected_text[x],f'Expected {expected_text[x]}, but got {actual_text}'
