import warnings
from requests import RequestsDependencyWarning
warnings.filterwarnings("ignore", category=RequestsDependencyWarning)

from selenium import webdriver
import time

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

# ===== Test Data =====
BASE_URL = "http://localhost:3000"
EMAIL = "ledermannoam18@gmail.com"
PASSWORD = "123"
PRODUCT_NAME = "iPhone"

# ===== Start Browser (Selenium Manager) =====
driver = webdriver.Chrome()     # ✅ FIX: no webdriver-manager
driver.maximize_window()
driver.implicitly_wait(5)

# ===== 1) Login =====
login_page = LoginPage(driver)
login_page.open()
login_page.login(EMAIL, PASSWORD)

# ===== 2) Open Home Page =====
driver.get(BASE_URL)

# ===== 3) Open iPhone Product =====
home = HomePage(driver)
home.open_iphone()

# ===== 4) Add To Cart =====
product = ProductPage(driver)
product.add_to_cart()

# ===== 5) Verify Product In Cart =====
cart = CartPage(driver)

if cart.product_in_cart(PRODUCT_NAME):
    print("✅ TEST PASSED: iPhone found in cart")
else:
    print("❌ TEST FAILED: iPhone NOT found in cart")

time.sleep(3)
driver.quit()

