import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


amazon = 'https://www.amazon.com'
#link_help = (By.XPATH,"//div[@id='nav-xshop']/a[@tabindex='54']")
link_help= (By.CSS_SELECTOR,"a[href*='nav_cs_customerservice']")
link_find = (By.XPATH,"//div[@class='a-search a-span12']/input[@id='helpsearch']")
search_word = 'cancel order'
search_click = (By.XPATH,"//div[@class='a-column a-span2 a-span-last']/span[@id='helpSearchSubmit']")
word_found = (By.XPATH,"//div[@class='help-content']/h1")
search_word2 = "Cancel Items or Orders"
#blocker critical normal minor trivial
@allure.feature('Open Amazon')
@allure.story('search and check Cancel Items or Orders ')
@allure.severity('critical')
def test_amazon_search():
    driver= webdriver.Chrome()

    # open the url
    driver.maximize_window()
    driver.get( amazon )
    sleep(1)
    with allure.step('open the url'):
         allure.attach(driver.get_screenshot_as_png(), name='Screenshot',attachment_type=AttachmentType.PNG)
    help_link = driver.find_element(*link_help )
    help_link.click()
    sleep(1)

    # serch word
    find_link = driver.find_element(*link_find )
    find_link.click()
    find_link.send_keys( search_word )
    sleep(4)

    # click search
    cliack_search = driver.find_element(*search_click )
    cliack_search.click()

    assert isinstance( driver.find_element(*word_found).text,object)
    assert search_word2 in driver.find_element(*word_found).text


    driver.quit()
