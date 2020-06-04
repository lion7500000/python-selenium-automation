from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Product(Page):

    sales_deals_btn = (By.CSS_SELECTOR, "a[href*='fashion-sale']")
    deals_selection = (By.CSS_SELECTOR,"img[src*='fall3_women']")
    btn_add_to_card = (By.ID, 'add-to-cart-button')
    menu_add_to_card = (By.ID, 'a-popover-content-1')

    color_item = (By.CSS_SELECTOR, "div#variation_color_name img.imgSwatch")
    selected_color = (By.CSS_SELECTOR, "span.selection")
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']

    def open_product(self,product_id):
        #open https://www.amazon.com/gp/product/B074TBCSC8
        self.open_page(f'dp/product/{product_id}')

    def open_amazon_page(self,product_id ):
        # open ('https://www.amazon.com/gp/product/B07BKFFFXL/?th=1')
        self.open_page( f'dp/product/{product_id}' )

    def hover_sales_deals(self):
        sale_button = self.find_element(*self.sales_deals_btn)
        self.actions.move_to_element(sale_button).perform()

    def hover_cart_btn( self ):
        sale_button = self.find_element( *self.btn_add_to_card )
        self.actions.move_to_element( sale_button ).perform()

    def verify_deals (self):
        self.wait_for_element_appear(*self.deals_selection)

    def verify_menu_add_card_btn( self ):
        self.wait_for_element_appear( *self.menu_add_to_card )

    def verify_colors_item(self):
        colors_item = self.find_elements( *self.color_item )

        for color in colors_item:
            color.click()
            actual_color = self.find_element( *self.selected_color ).text
            assert actual_color == self.expected_colors[colors_item.index(color )], f'Expected {self.expected_colors[colors_item.index( color )]}, but got {actual_color}'


