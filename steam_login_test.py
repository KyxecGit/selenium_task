import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from faker import Faker
from config import *

@pytest.fixture
def browser():
    #Фикстура для создания браузера и перехода на сайт
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()

def click_element(browser, xpath):
    #Ожидает, пока элемент станет кликабельным, и нажимает на него
    WebDriverWait(browser, TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, xpath))).click()

def enter_text(browser, xpath, text):
    #Ожидает видимость элемента и вводит текст в поле ввода
    WebDriverWait(browser, TIMEOUT).until(
        EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(text)

def test_login(browser):
    """Тестовый сценарий для проверки входа в систему с использованием случайных данных"""

    # Создаем экземпляр Faker для генерации случайных данных
    fake = Faker()
    username = fake.user_name() 
    password = fake.password()  

    # Нажимаем на кнопку "Войти"
    click_element(browser, LOGIN_BUTTON_XPATH)

    # Вводим случайные данные в поле имени пользователя
    enter_text(browser, USERNAME_INPUT_XPATH, username)

    # Вводим случайные данные в поле пароля
    enter_text(browser, PASSWORD_INPUT_XPATH, password)

    # Нажимаем кнопку "Войти"
    click_element(browser, SUBMIT_BUTTON_XPATH)

    # Проверяем наличие сообщения об ошибке
    try:
        error_element = WebDriverWait(browser, TIMEOUT).until(
            EC.visibility_of_element_located((By.XPATH, ERROR_MESSAGE_XPATH)))
        assert "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова" in error_element.text, "Сообщение об ошибке не соответствует ожидаемому."
    except TimeoutException:
        # Если сообщение об ошибке не появилось, тест считается неудачным
        assert False, "Не удалось найти сообщение об ошибке после неудачной попытки входа."
