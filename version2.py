from seleniumbase import BaseCase
import time

class MyTestClass(BaseCase):
    def test_login(self):
        # Открываем страницу
        self.open("https://store.steampowered.com/")
        
        # Нажимаем на кнопку "войти"
        self.click("//*[@id='global_action_menu']//a[text()='войти']")
        time.sleep(3)

        # Уникальные локаторы для обязательных полей регистрации
        self.type("//div[div[contains(text(), 'Войти, используя имя аккаунта')]]//input[@type='text']", "kyxec")
        self.type("//div[div[contains(text(), 'Пароль')]]//input[@type='password']", "12345")
        time.sleep(3)

        # Нажимаем кнопку "Войти"
        self.click("//button[@type='submit' and text()='Войти']")
        time.sleep(3)

# запуск pytest main.py