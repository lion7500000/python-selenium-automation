from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



parasoft = 'https://www.parasoft.com/'
company_btn = (By.XPATH, "//ul[@class='menu menu-level-0']/li[4]/a[@class='company menu-item-categorized']")
leadership_btn=(By.XPATH,"//ul[@class='menu menu-level-3']/li[3]/a[contains(@href,'leadership')]")

def test_parasoft_search():
    driver= webdriver.Chrome()

    # open the url
    driver.maximize_window()
    driver.get(parasoft)
    sleep(15)
    # muve to company
    action = ActionChains( driver )
    firstLevelMenu = driver.find_element (*company_btn)
    action.move_to_element( firstLevelMenu ).perform()
    sleep(10)
    #click on leadrship
    open_leadrship = driver.find_element(*leadership_btn)
    open_leadrship.click()
