from selenium.webdriver.common.by import By
from behave import then, when


@when ('Select Books department')
def select_department(context):
    context.app.menu_page.select_books_department()

@when ('Select Amazon Fresh department')
def select_department(context):
    context.app.menu_page.select_amazon_fresh_department()

@when ('Search for {text}')
def input_search_text_in_select_departmen(context,text):
    context.app.menu_page.input_search_text_in_select_departmen(text)

@when( 'Search product {text}' )
def input_search_text_in_select_departmen(context, text):
    context.app.menu_page.input_search_text_in_select_departmen( text )

@then ('{departmen} department is selected')
def verify_select_departmen(context,departmen):
    context.app.menu_page.verify_select_departmen(departmen)

@then ('{departmen} department is selected in departmen')
def verify_select_departmen(context,departmen):
    context.app.menu_page.verify_select_departmen(departmen)

