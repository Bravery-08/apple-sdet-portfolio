from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver=driver
        self.signup_login_link=(By.LINK_TEXT, "Signup / Login")
        self.products_link=(By.CSS_SELECTOR, "a[href='/products']")
    
    def go_to_login(self):
        self.driver.find_element(*self.signup_login_link).click()
        
    def go_to_products(self):
        self.driver.find_element(*self.products_link).click()