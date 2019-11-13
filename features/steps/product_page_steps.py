from selenium.webdriver.common.by import By
from behave import then, when

@given ('Open Amazon pruduct {product_id}')
def open_product(context,product_id):
    context.app.product_page.open_product(product_id)

@when ('hovers over Sales and Deals')
def hover_sales_deals(context):
    context.app.product_page.hover_sales_deals()

@then ('verifies that user sees the deals')
def verify_deals(context):
    context.app.product_page.verify_deals()

