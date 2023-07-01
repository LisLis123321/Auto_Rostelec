import pytest
from selenium import webdriver


# Фикстуры инициализации и закрытия браузера
@pytest.fixture()
def google_chrome_browser():
    print("Start GoogleChrome browser")
    driver = webdriver.Chrome()
    driver.implicitly_wait(7)
    yield driver
    print("Quit GoogleChrome browser")
    driver.quit()
