from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.wait = WebDriverWait(driver,15)

original_window = driver.current_window_handle
old_window = driver.window_handles
driver.find_element().click()
driver.wait.until(EC.new_window_is_opened)
new_window = driver.window_handles[1]
driver.switch_to_window(new_window)
driver.close()
driver.switch_to_window(original_window)


