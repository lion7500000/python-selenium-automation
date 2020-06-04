from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

Login_btn = (By.XPATH, "//a[text()='Login']")
attainia = 'https://www.attainia.com/'
Username = (By.ID,'signin_username')
user_txt = 'Lion75'
Password = (By.ID,'signin_password')
pass_txt = '12345'
Sing_in_btn = (By.XPATH,'//input[@type="image"]')


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#driver.wait = WebDriverWait(driver, 10)

#open site
driver.maximize_window()
driver.get(attainia)

#push the btn
login = driver.find_element(*Login_btn).click()
#enter username
username_fild = driver.find_element(*Username)
username_fild.clear()
username_fild.send_keys(user_txt)

#enter password
password_fild = driver.find_element(*Password)
password_fild.clear()
password_fild.send_keys(pass_txt)
#push sing-in btn
Sing_In = driver.find_element(*Sing_in_btn).click()
original_window = driver.current_window_handle
print(original_window)
curent_url = driver.current_url.text
print (curent_url)

