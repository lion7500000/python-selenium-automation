from selenium.webdriver.support.select import Select
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SideMenu(Page):

    music_menu = (By.XPATH, "//ul[contains(@class,'hmenu-visible')]//div[contains(text(),'Amazon Music')]")
    music_menu_item_results = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def click_amazon_music_menu (self):
        #self.click(*self.music_menu)
        self.wait_for_element_click(*self.music_menu)
        sleep(1)

    def verify_amound_items(self,expected_items:int):
        self.verify_len_items(expected_items,*self.music_menu_item_results)