from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'
        self.wait = WebDriverWait(self.driver,15)
        self.actions = ActionChains(self.driver)


    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)

    def wait_for_element_click(self,*locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self,*locator):
        self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self,*locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'

    #def verify_found_text(context, search_word, *locator):
    #    actual_word = context.driver.find_element( *locator ).text
    #    assert search_word in actual_word, f'Expected text {search_word}, but got {actual_word}'

    def verify_len_items(self, expected_items, *locator):
        actual_items = len(self.driver.find_elements(*locator))
        assert int(expected_items) == actual_items, f'Expected text {expected_items}, but got {actual_items}'
