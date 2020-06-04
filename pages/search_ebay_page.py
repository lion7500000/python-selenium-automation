from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResults2(Page):

    search_text= (By.XPATH,"//h1[@class='srp-controls__count-heading']/span[2]")

    def verify_EBAY_serch_product(self, test):
        self.verify_text(test, *self.search_text)