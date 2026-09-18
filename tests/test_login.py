from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage

driver = webdriver.Chrome()
driver.get('https://www.automationexercise.com')

home = HomePage(driver)
home.go_to_login()

login = LoginPage(driver)
login.login('test@example.com', 'wrongpassword')

driver.quit()