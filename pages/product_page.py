from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.ID, "search_product")
        self.search_button = (By.ID, "submit_search")
        self.product = (By.CLASS_NAME, "product-image-wrapper")
        self.add_to_cart_button=(By.CSS_SELECTOR, "a.btn.btn-default.add-to-cart[data-product-id='2']")
        self.continue_button=(By.XPATH, "//button[text()='Continue Shopping']")
        self.view_cart_button=(By.CSS_SELECTOR, "a[href='/view_cart']")

    def search(self, string):
        self.driver.find_element(*self.search_bar).send_keys(string)
        self.driver.find_element(*self.search_button).click()

    def find_product(self):
        return self.driver.find_element(*self.product)

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        
    def continue_shopping(self):
        self.driver.find_element(*self.continue_button).click()
        
    def view_cart(self):
        self.driver.find_element(*self.view_cart_button).click()