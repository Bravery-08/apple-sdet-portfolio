from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_product_shows_in_cart(driver):
    driver.get('https://www.automationexercise.com')
    HomePage(driver).go_to_products()

    product_page = ProductPage(driver)
    product_page.search('shirt')
    product_page.add_to_cart()
    product_page.continue_shopping()
    product_page.view_cart()

    assert CartPage(driver).find_product().is_displayed()
