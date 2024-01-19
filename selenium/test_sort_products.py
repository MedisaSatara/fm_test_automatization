from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
def test_sort_products():
    chrome_options = webdriver.ChromeOptions()
    chrome_service = webdriver.chrome.service.Service("chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    wait=WebDriverWait(driver,timeout=60)
    driver.get("https://www.ekupi.ba/")

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "js-site-search-input"))
    )
    search_query = "laptopi"
    search_input.send_keys(search_query)

    search_button = driver.find_element(By.CLASS_NAME, "js_search_button")
    search_button.click()

    sort_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sortOptions1"))
    )
    sort_dropdown.click()

    sort_select = Select(driver.find_element(By.ID, "sortOptions1"))
    sort_select.select_by_visible_text("Najviše ocjene")

    sort_text_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'name')))
    sort_text = sort_text_element.text
    assert sort_text == "Laptop HP 17-cp0103nm, 8D020EA, 17,3 FHD IPS, AMD Ryzen 7 5700U, 16GB DDR4, 512GB PCIe NVMe SSD, AMD Radeon Graphics, FreeDOS"

    driver.quit()