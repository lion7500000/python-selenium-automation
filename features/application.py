from pages.main_page import MainPage
from pages.search_results_page import SearchResults
from pages.menu_page import MenuPage
from pages.product_page import Product
from pages.side_menu import SideMenu
from pages.main_page_ebay import Main_page_ebay
from pages.search_ebay_page import SearchResults2

class Application:

    def __init__(self,driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.menu_page = MenuPage(self.driver)
        self.product_page = Product(self.driver)
        self.side_menu = SideMenu(self.driver)
        self.main_page_ebay = Main_page_ebay(self.driver)
        self.search_ebay_page = SearchResults2(self.driver)
