from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Main_page_ebay(Page):

    search_icon = (By.CSS_SELECTOR, "input#gh-ac")
    search_btn = (By.CSS_SELECTOR, "input#gh-btn")

    def open_page2(self, url=''):
        self.driver.get(self.base_url1 + url)

    def input_text_search (self, text):
        self.input_text(text, *self.search_icon)

    def click_serch_btn(self):
        self.click(*self.search_btn)
