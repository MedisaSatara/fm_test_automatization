import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_service = webdriver.chrome.service.Service("chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
wait=WebDriverWait(driver,timeout=60)

def test_search():
    driver.get("https://www.ekupi.ba/") 

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "js-site-search-input"))
    )

    search_query = "laptopi"
    search_input.send_keys(search_query)

    search_button = driver.find_element(By.CLASS_NAME, "js_search_button")
    search_button.click()
    time.sleep(2)
    search_text_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'active')))
    search_text = search_text_element.text
    assert search_text == "Laptopi"

    driver.quit()