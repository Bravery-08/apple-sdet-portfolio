from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signupform_page import SignupformPage

def test_select_works(driver):
    driver.get('https://www.automationexercise.com')
    
    HomePage(driver).go_to_login()
    LoginPage(driver).signup('Shaurya','shaurya3247@gmail.com')
    
    signup=SignupformPage(driver)
    signup.select_country('Canada')
    
    assert signup.get_country()=='Canada'