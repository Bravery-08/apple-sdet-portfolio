from selenium.webdriver.common.by import By
from functools import wraps
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


def retry_on_popup(max_retries=2):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(self, *args, **kwargs)
                except (NoSuchElementException, ElementClickInterceptedException, TimeoutException):
                    if attempt == max_retries-1:
                        raise
                    self.remove_popup()

        return wrapper
    return decorator


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)
        self.popup_close = (By.CLASS_NAME, "continue-prompt-text")

    def remove_popup(self):
        iframes = self.driver.find_elements(
            By.CSS_SELECTOR, 'iframe[title="Advertisement"]')

        for iframe in iframes:
            if iframe.is_displayed():
                try:
                    self.driver.switch_to.frame(iframe)

                    close_button = self.driver.find_element(*self.popup_close)
                    close_button.click()
                except:
                    pass
                finally:
                    self.driver.switch_to.default_content()
