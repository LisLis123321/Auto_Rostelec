import os
import time

from locators.AuthorizationPageLocators import AuthorizationPageLocators
from pages.BasePage import BasePage
from settings import base_url


class AuthorizationPage(BasePage):
    """Страница авторизации с web-элементами"""

    def __init__(self, driver):
        super().__init__(driver)
        url = os.getenv(base_url) or 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.tab_email = driver.find_element(*AuthorizationPageLocators.TAB_EMAIL)
        self.tab_phone = driver.find_element(*AuthorizationPageLocators.TAB_PHONE)
        self.tab_login = driver.find_element(*AuthorizationPageLocators.TAB_LOGIN)
        self.tab_personal_account = driver.find_element(*AuthorizationPageLocators.TAB_PERSONAL_ACCOUNT)
        self.username = driver.find_element(*AuthorizationPageLocators.FIELD_USERNAME)
        self.password = driver.find_element(*AuthorizationPageLocators.FIELD_PASS)
        self.forgot_password_button = driver.find_element(*AuthorizationPageLocators.FORGOT_PASSWORD_BUTTON)
        self.btn = driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON)
        self.reg_in = driver.find_element(*AuthorizationPageLocators.REGISTER_BUTTON)
        self.auth_by_vk = driver.find_element(*AuthorizationPageLocators.AUTH_BY_VK)
        self.auth_by_odnoklassniky = driver.find_element(*AuthorizationPageLocators.AUTH_BY_OK)
        self.auth_by_mail = driver.find_element(*AuthorizationPageLocators.AUTH_BY_MAIL)
        self.auth_by_yandex = driver.find_element(*AuthorizationPageLocators.AUTH_BY_YANDEX)

    def tab_email(self):
        """Выбирать вкладку 'Почта'"""
        self.tab_email()

    def tab_phone(self):
        """Выбирать вкладку 'Телефон'"""
        self.tab_phone()

    def tab_login(self):
        """Выбирать вкладку 'Логин'"""
        self.tab_login()

    def tab_ls(self):
        """Выбирать вкладку 'Лицевой счёт'"""
        self.tab_personal_account()

    def set_username(self, value):
        """Ввести адрес электронной почты в поле ввода"""
        self.username.send_keys(value)

    def set_password(self, value):
        """Ввести пароль в поле ввода"""
        self.password.send_keys(value)

    def forgot_password_button(self):
        """Нажать на кнопку 'Забыл пароль'"""
        self.forgot_password_button()
        time.sleep(10)

    def click_on_enter_button(self):
        """Нажать на кнопку 'Войти'"""
        self.btn.click()
        time.sleep(10)

    def click_on_registration_button(self):
        """Нажать на кнопку 'Зарегистрироваться'"""
        self.reg_in.click()

    def authorization_by_vk(self):
        """Нажать на иконку авторизации через 'ВКонтакте'"""
        self.auth_by_vk()
        time.sleep(10)

    def authorization_by_odnoklassniky(self):
        """Нажать на иконку авторизации через 'Одноклассники'"""
        self.auth_by_odnoklassniky()
        time.sleep(10)

    def authorization_by_mail(self):
        """Нажать на иконку авторизации через сервис mail.ru"""
        self.auth_by_mail()
        time.sleep(10)

    def authorization_by_yandex(self):
        """Нажать на иконку авторизации через сервис yandex.ru"""
        self.auth_by_yandex()
        time.sleep(10)
