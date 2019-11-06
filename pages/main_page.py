from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):
    order_icon = (By.ID,'nav-orders')
    card_icon = (By.CSS_SELECTOR, "a#nav-cart")
    hamburger_menu =(By.ID, 'nav-hamburger-menu')

    def click_order_icon (self):
        self.click(*self.order_icon)

    def click_card_icon(self):
        self.click(*self.card_icon)

    def click_hamburger_menu(self):
        self.click(*self.hamburger_menu)


