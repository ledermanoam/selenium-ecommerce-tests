import warnings
from requests import RequestsDependencyWarning
warnings.filterwarnings("ignore", category=RequestsDependencyWarning)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

EMAIL = "ledermannoam18@gmail.com"
PASSWORD = "123"
PRODUCT_NAME = "iPhone"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)

# 1) Login
login_page = LoginPage(driver)
login_page.open()
login_page.login(EMAIL, PASSWORD)

# 2) Open home page
driver.get("http://localhost:3000")
home = HomePage(driver)
home.open_iphone()


# 3) Add to cart
product = ProductPage(driver)
product.add_to_cart()

# 4) Verify product in cart
cart = CartPage(driver)

if cart.product_in_cart(PRODUCT_NAME):
    print("✅ TEST PASSED: iPhone found in cart")
else:
    print("❌ TEST FAILED: Canon camera NOT found in cart")

time.sleep(3)
driver.quit()
