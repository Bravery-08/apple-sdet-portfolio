from pages.home_page import HomePage
from pages.product_page import ProductPage
from selenium.common.exceptions import NoSuchElementException
import pytest

def test_search_shows_products(driver):
    driver.get('https://www.automationexercise.com')
    HomePage(driver).go_to_products()
    product_page=ProductPage(driver)
    product_page.search('shirt')
    product=product_page.find_product()
    
    assert product.is_displayed()
    
def test_search_doesnt_show_products(driver):
    driver.get('https://www.automationexercise.com')
    HomePage(driver).go_to_products()
    product_page=ProductPage(driver)
    product_page.search('nosuchproduct')
    
    with pytest.raises(NoSuchElementException):
        product_page.find_product() 