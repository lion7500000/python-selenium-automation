from selenium.webdriver.support.select import Select
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MenuPage(Page):

    music_menu = (By.XPATH, "//ul[contains(@class,'hmenu-visible')]//div[contains(text(),'Amazon Music')]")
    #music_menu_item_results = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")
    select_amazon_books_department = (By.CSS_SELECTOR,"select#searchDropdownBox")
    select_departmen_span = (By.CSS_SELECTOR,"span.nav-search-label")
    search_icon = (By.CSS_SELECTOR,"input#twotabsearchtextbox")


    def click_amazon_music_menu (self):
        #self.click(*self.music_menu)
        self.wait_for_element_click(*self.music_menu)
        sleep(1)

    def select_books_department(self):
        select_department_element = self.find_element(*self.select_amazon_books_department)
        select = Select(select_department_element)
        select.select_by_value('search-alias=stripbooks')

    def select_amazon_fresh_department(self):
        select_department_element = self.find_element(*self.select_amazon_books_department)
        select = Select(select_department_element)
        select.select_by_value('search-alias=amazonfresh')

    def verify_select_departmen(self,expected_text):
        self.verify_text(expected_text,*self.select_departmen_span)

    def input_search_text_in_select_departmen(self,text):
        self.input_text(text,*self.search_icon)

