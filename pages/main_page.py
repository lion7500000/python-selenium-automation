from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):
    order_icon = (By.ID,'nav-orders')
    card_icon = (By.ID, "nav-cart")
    hamburger_menu =(By.ID, 'nav-hamburger-menu')
    music_menu = (By.XPATH, "//ul[contains(@class,'hmenu-visible')]//div[contains(text(),'Amazon Music')]")
    search_icon = (By.CSS_SELECTOR, "input#twotabsearchtextbox")
    btn_search = (By.CSS_SELECTOR, "input.nav-input[type='submit']")

    def open_page(self,url=''):
        self.driver.get(self.base_url+url)

    def click_order_icon (self):
        self.click(*self.order_icon)

    def click_cart_icon(self):
        self.click(*self.card_icon)

    def click_hamburger_menu(self):
        self.click(*self.hamburger_menu)
        self.wait_for_element_appear( *self.music_menu )
        #sleep( 4 )

    def search_product(self,text):
        self.input_text(text,*self.search_icon)

    def click_search_product(self):
        self.click(*self.btn_search )
        #sleep(5)



