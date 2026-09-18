from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver=driver
        self.login_email=(By.NAME, "email")
        self.login_password=(By.NAME, "password")
        self.login_button=(By.CSS_SELECTOR, "button[data-qa='login-button']")
    
    def login(self, email, password):
        self.driver.find_element(*self.login_email).send_keys(email)
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.login_button).click()