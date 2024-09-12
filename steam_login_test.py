import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

# Константы
URL = "https://store.steampowered.com/"
LOGIN_BUTTON_XPATH = "//*[@id='global_action_menu']//a[text()='войти']"
USERNAME_INPUT_XPATH = "//div[div[contains(text(), 'Войти, используя имя аккаунта')]]//input[@type='text']"
PASSWORD_INPUT_XPATH = "//div[div[contains(text(), 'Пароль')]]//input[@type='password']" 
SUBMIT_BUTTON_XPATH = "//button[@type='submit' and text()='Войти']" 

@pytest.fixture
def browser():
    """Фикстура для создания и завершения работы с браузером."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(browser):
    # Создаем экземпляр Faker для генерации случайных данных
    fake = Faker()
    username = fake.user_name()  # Генерация случайного имени пользователя
    password = fake.password()  # Генерация случайного пароля

    # Открываем URL страницы
    browser.get(URL)

    # Ждем, пока кнопка "войти" станет кликабельной, и нажимаем ее
    WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_XPATH))).click()

    # Ждем, пока поле ввода имени пользователя станет видимым, и вводим имя
    WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, USERNAME_INPUT_XPATH))).send_keys(username)

    # Ждем, пока поле ввода пароля станет видимым, и вводим пароль
    WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, PASSWORD_INPUT_XPATH))).send_keys(password)

    # Ждем, пока кнопка "Войти" станет кликабельной, и нажимаем ее
    WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, SUBMIT_BUTTON_XPATH))).click()
