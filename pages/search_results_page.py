from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResults(Page):

    sign_in_page = (By.XPATH, "//h1[@class='a-spacing-small']")
    card_empty = (By.CSS_SELECTOR, 'h1.sc-empty-cart-header')
    music_menu_item_results = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def verify_sigh_in_page(self,expected_text):
        self.verify_text (expected_text,*self.sign_in_page)

    def verify_card_empty(self, expected_text):
        self.verify_text(expected_text, *self.card_empty)

    def verify_amound_items(self,expected_items:int):
        self.verify_len_items(expected_items,*self.music_menu_item_results)