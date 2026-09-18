from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_invalid_login_shows_error(driver):
    driver.get('https://www.automationexercise.com')
    HomePage(driver).go_to_login()
    LoginPage(driver).login('test@example.com', 'wrongpassword')
    
    assert 'incorrect' in driver.page_source.lower()