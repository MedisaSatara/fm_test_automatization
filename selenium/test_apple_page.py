from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_apple_page():
    chrome_options = webdriver.ChromeOptions()
    chrome_service = webdriver.chrome.service.Service("chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    wait = WebDriverWait(driver, timeout=60)
    try:
        driver.get("https://www.ekupi.ba/")
        driver.maximize_window()

        nav_link_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Apple')]"))
        )
        nav_link_button.click()

        button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='button iPhonemob']"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", button_element)
        button_element.click()
        time.sleep(2)

        apple_type_text_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'carousel__item--name')))
        apple_type_text = apple_type_text_element.text
        assert apple_type_text == "Apple iPhone 15 Pro Max mobitel, 8+256 GB, Black Titanium"
        
    finally:
        driver.quit()
