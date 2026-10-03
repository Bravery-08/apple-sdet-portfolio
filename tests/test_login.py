from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_invalid_login_shows_error(driver):
    driver.get('https://www.automationexercise.com')
    HomePage(driver).go_to_login()
    LoginPage(driver).login('test@example.com', 'wrongpassword')

    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'p[style="color: red;"]'))
    )

    assert 'incorrect' in error.text.lower()
