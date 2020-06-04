from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

porsche = 'https://www.porsche.com/specials/panamera-exclusive/'
region_choise = (By.CSS_SELECTOR, "div#s2id_autogen1 span.select2-arrow")
country_choise = (By.CSS_SELECTOR, "div#s2id_autogen3 span.select2-arrow ")
north_America = (By.CSS_SELECTOR,"ul.select2-results div")

def test_porsche_serch ():
    driver = webdriver.Chrome()

    # open the url
    driver.maximize_window()
    driver.get(porsche)

    #choes region
    region = driver.find_element(*region_choise)
    region.click()
    #action = ActionChains( driver )
    region_select = driver.find_elements( *north_America )

    #action.move_to_element(region_select).perform()
    region_select[0].click()
    sleep (5)

    #choise country
    #country = driver.find_element(*country_choise)
    #country.click()
    #sleep(5)