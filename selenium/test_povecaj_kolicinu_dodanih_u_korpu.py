from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
def test_povecaj_kolicinu_dodanih_u_korpu():
    chrome_options = webdriver.ChromeOptions()
    chrome_service = webdriver.chrome.service.Service("chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    wait = WebDriverWait(driver, timeout=60)
    try:
        driver.get("https://www.ekupi.ba/")
        driver.maximize_window()
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "js-site-search-input"))
        )
        search_query = "laptop"
        search_input.send_keys(search_query)
        search_button = driver.find_element(By.CLASS_NAME, "js_search_button")
        search_button.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".thumb"))
        )
        product_link = driver.find_element(By.CSS_SELECTOR, ".thumb")
        product_link.click()
        btn= btn = driver.find_element(By.CSS_SELECTOR,'.btn.btn-default.js-qty-selector-plus')
        driver.execute_script("arguments[0].scrollIntoView();", btn)
        time.sleep(2)
        btn.click()
        time.sleep(5)
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='addToCartButton']"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
        time.sleep(2)
        add_to_cart_button.click()
        time.sleep(2)
        link_xpath = "//a[@class='btn btn-primary btn--continue-shopping']"
        linka = driver.find_element(By.XPATH,link_xpath)
        linka.click()
        time.sleep(2)
        increase_text_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'item__info')))
        increase_text = increase_text_element.text
        assert increase_text == "ARTIKL"
    finally:
        driver.quit()