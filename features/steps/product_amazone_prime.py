from selenium.webdriver.common.by import By
from behave import then
from time import sleep

Search_boxes = (By.CSS_SELECTOR,"div#primeDetailPage p[class='a-spacing-base a-size-medium a-text-bold'] ")


@then ('Verify {searh_items} boxes in menu')
def verify_box_items(context,searh_items):
    results_boxes = len(context.driver.find_elements(*Search_boxes))
    assert int(searh_items) == results_boxes, "Expected items '{}' in message, but got '{}'".format(searh_items, results_boxes)
