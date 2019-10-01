from selenium import webdriver
from time import sleep


amazon = 'https://www.amazon.com'
link_prime = "//a[@id='nav-link-prime']/span[@class='nav-line-2 ']"
link_try_prime = "//div[@class='prime-button-try']"
url_prime = 'https://www.amazon.com/amazonprime'


def test_amazon_search():
    driver = webdriver.Chrome()


    #open the url
    driver.get(amazon)
    sleep(1)


    prime_link = driver.find_element_by_xpath(link_prime)
    prime_link.click()
    sleep(1)
    try_link = driver.find_element_by_xpath(link_try_prime)
    try_link.click()
    sleep(3)


    assert url_prime in driver.current_url


    driver.quit()