from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MenuPage(Page):

    music_menu = (By.XPATH, "//ul[contains(@class,'hmenu-visible')]//div[contains(text(),'Amazon Music')]")
    #music_menu_item_results = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def click_amazon_music_menu (self):
        #self.click(*self.music_menu)
        self.wait_for_element_click(*self.music_menu)
        sleep(1)

