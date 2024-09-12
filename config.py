# config.py

URL = "https://store.steampowered.com/"
LOGIN_BUTTON_XPATH = "//*[@id='global_action_menu']//a[text()='войти']"
USERNAME_INPUT_XPATH = "//div[div[contains(text(), 'Войти, используя имя аккаунта')]]//input[@type='text']"
PASSWORD_INPUT_XPATH = "//div[div[contains(text(), 'Пароль')]]//input[@type='password']"
SUBMIT_BUTTON_XPATH = "//button[@type='submit' and text()='Войти']"
ERROR_MESSAGE_XPATH = "//*[@id='responsive_page_template_content']//div[contains(text(), 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова')]"
TIMEOUT = 10
