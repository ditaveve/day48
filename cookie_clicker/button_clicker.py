from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#driver.quit()

class ButtonClicker:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://ozh.github.io/cookieclicker/")

        language_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]'))
        )
        language_button.click()
        self.cookie_button = self.driver.find_element(By.ID, value="bigCookie")


    def click_cookie(self):
        self.cookie_button.click()