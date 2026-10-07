from selenium.webdriver.common.by import By
from pages.the_internet.base import Base
from selenium.webdriver.support import expected_conditions as EC


class JS_alerts(Base):
    def __init__(self, driver):
        super().__init__(driver)

        self.alert_button = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
        self.confirm_button = (
            By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
        self.prompt_button = (By.CSS_SELECTOR, "button[onclick='jsPrompt()']")

        self.result = (By.CSS_SELECTOR, "p#result")

    def click_alert(self):
        self.wait.until(
            EC.element_to_be_clickable(self.alert_button)
        ).click()

    def click_confirm(self):
        self.driver.find_element(*self.confirm_button).click()

    def click_prompt(self):
        self.driver.find_element(*self.prompt_button).click()

    def get_result(self):
        return self.driver.find_element(*self.result).text
