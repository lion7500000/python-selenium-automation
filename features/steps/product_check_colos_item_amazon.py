from selenium.webdriver.common.by import By
from behave import given, when, then

color_item = (By.CSS_SELECTOR,"div#variation_color_name img.imgSwatch")
selected_color = (By.CSS_SELECTOR,"span.selection")

@then ('verify colors in item')
def verify_colors_item(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']
    colors_item = context.driver.find_elements(*color_item)

    for color in colors_item:
        color.click()
        actual_color = context.driver.find_element(*selected_color).text
        assert actual_color == expected_colors[colors_item.index(color)] ,f'Expected {expected_colors[colors_item.index(color)]}, but got {actual_color}'
