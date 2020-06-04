from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults( Page ):
    sign_in_page = (By.XPATH, "//h1[@class='a-spacing-small']")
    card_empty = (By.CSS_SELECTOR, 'h1.sc-empty-cart-header')
    music_menu_item_results = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")
    search_word = (By.CSS_SELECTOR, "h1 span.a-text-bold")

    # search_EBAY = (By.XPATH,"//h1[@class='srp-controls__count-heading']/span[2]")

    def verify_sigh_in_page(self, expected_text):
        self.verify_text( expected_text, *self.sign_in_page )

    def verify_card_empty(self, search_word):
        self.verify_found_text( search_word, *self.card_empty )

    def verify_serch_word(self, word):
        self.verify_text( word, *self.card_empty )

    def verify_product_amazon(self, word):
        self.verify_text( word, *self.search_word )

    # def verify_EBAY_serch_product(self, word):
    #    self.verify_text(word, *self.search_EBAY)
