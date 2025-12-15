from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def product_in_cart(self, product_name):
        cart_items_text = self.driver.find_element(By.TAG_NAME, "body").text
        return product_name in cart_items_text
