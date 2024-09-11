from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:

    link = "https://store.steampowered.com/"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку "войти"
    button = browser.find_element(By.XPATH, "//*[@id='global_action_menu']//a[text()='войти']")
    button.click()

    time.sleep(3)

    # Уникальные локаторы для обязательных полей регистрации
    input1 = browser.find_element(By.XPATH, "//div[div[contains(text(), 'Войти, используя имя аккаунта')]]//input[@type='text']")
    input1.send_keys("kyxec")

    input2 = browser.find_element(By.XPATH, "//div[div[contains(text(), 'Пароль')]]//input[@type='password']")
    input2.send_keys("12345")

    # Нажимаем кнопку "Войти"
    login_button = browser.find_element(By.XPATH, "//button[@type='submit' and text()='Войти']")
    login_button.click()

finally:
    
    time.sleep(3)
    browser.quit()
