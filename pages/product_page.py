from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Product(Page):

    sales_deals_btn = (By.CSS_SELECTOR, "a[href*='fashion-sale']")
    deals_selection = (By.CSS_SELECTOR,"img[src*='fall3_women']")

    def open_product(self,product_id):
        #open https://www.amazon.com/gp/product/B074TBCSC8
        self.open_page(f'dp/product/{product_id}')

    def hover_sales_deals(self):
        sale_button = self.find_element(*self.sales_deals_btn)
        self.actions.move_to_element(sale_button).perform()

    def verify_deals (self):
        self.wait_for_element_appear(*self.deals_selection)


