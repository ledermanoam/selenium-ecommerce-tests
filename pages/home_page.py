from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    IPHONE_LINK = (By.CSS_SELECTOR, "a[href='/product/693fdac4122c8cfc8cfdbf0c']")

    def open_iphone(self):
        # wait until the link exists in the page
        iphone = self.wait.until(
            EC.presence_of_element_located(self.IPHONE_LINK)
        )

        # scroll to it (important for React pages)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", iphone)

        # click using JavaScript (very reliable)
        self.driver.execute_script("arguments[0].click();", iphone)
