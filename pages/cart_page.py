from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver=driver
        self.product=(By.ID, "product-2")
        
    def find_product(self):
        return self.driver.find_element(*self.product)