from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select

def test_pronadji_gume():
    chrome_options = webdriver.ChromeOptions()
    chrome_service = webdriver.chrome.service.Service("chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    wait = WebDriverWait(driver, timeout=60)

    try:
        driver.get("https://www.ekupi.ba/")
        driver.maximize_window()

        gume_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Gume')]"))
        )
        gume_button.click()

        brand_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "brand"))
        )
        select = Select(brand_select)
        select.select_by_value("Barum")
        sezona_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SezonaGuma"))
        )
        select = Select(sezona_select)
        select.select_by_value("Zimska")

        pronadji_gume_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and text()='Pronađi gume']"))
        )

        driver.execute_script("arguments[0].scrollIntoView();", pronadji_gume_button)
        time.sleep(2)
        pronadji_gume_button.click()
        time.sleep(5)
        list_of_find_text_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'pagination-bar-results')))
        list_of_text = list_of_find_text_element.text
        assert list_of_text == "1 pronađenih proizvoda"
    finally:
        driver.quit()