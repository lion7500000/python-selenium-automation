from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


amazon = 'https://www.amazon.com'
link_prime = (By.XPATH,"//a[@id='nav-link-prime']/span[@class='nav-line-2 ']")
link_try_prime = (By.XPATH,"//div[@class='prime-button-try']")
url_prime = 'https://www.amazon.com/amazonprime'


def test_amazon_search():
    driver = webdriver.Chrome()


    #open the url
    driver.get(amazon)
    sleep(1)


    prime_link = driver.find_element(*link_prime)
    prime_link.click()
    sleep(1)
    try_link = driver.find_element(*link_try_prime)
    try_link.click()
    sleep(3)


    assert url_prime in driver.current_url


    driver.quit()