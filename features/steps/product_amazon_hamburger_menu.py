from selenium.webdriver.common.by import By
from behave import then

music_menu_item_results = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")


@then('Click on Amazon Music menu items')
def click_music_menu(context):
    context.app.side_menu.click_amazon_music_menu()


@then ('{amound} menu items are present')
def verify_amound_of_items(context,amound):
    context.app.side_menu.verify_amound_items(amound)
    #actual_items = len(context.driver.find_elements(*music_menu_item_results))
    #print (actual_items)