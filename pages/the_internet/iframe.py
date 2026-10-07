from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.the_internet.base import Base

class Iframe(Base):
    def __init__(self,driver):
        super().__init__(driver)
        
        self.iframe=(By.ID, 'mce_0_ifr')
        self.close=(By.CSS_SELECTOR, "button.tox-notification__dismiss")
        self.message=(By.XPATH, "//body[@id='tinymce']/child::p")
        
    def click_close(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.close)
        ).click()
        
    def get_iframe(self):
        return self.driver.find_element(*self.iframe)
    
    def get_message(self):
        return self.driver.find_element(*self.message).text