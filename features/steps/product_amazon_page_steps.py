from selenium.webdriver.common.by import By
from behave import given,then, when
@given ('Open Amazon pruduct {product_id}')
def open_product(context,product_id):
    context.app.product_page.open_product(product_id)

@given('Open Amazon clothing page {product_id}')
def open_amazon_page(context, product_id):
    context.app.product_page.open_amazon_page(product_id)

@when ('hovers over Sales and Deals')
def hover_sales_deals(context):
    context.app.product_page.hover_sales_deals()

@when ('hovers over to add_to_card')
def hover_cart_btn(context):
    context.app.product_page.hover_cart_btn()

@then ('verifies that user sees the deals')
def verify_deals(context):
    context.app.product_page.verify_deals()

@then ('verifies that user sees menu')
def verify_menu_add_card_btn(context):
    context.app.product_page.verify_menu_add_card_btn()

@then ('verify colors in item')
def verify_colors_item(context):
    context.app.product_page.verify_colors_item()
