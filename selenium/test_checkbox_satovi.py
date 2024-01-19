from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_checkbox_satovi():
    chrome_options = webdriver.ChromeOptions()
    chrome_service = webdriver.chrome.service.Service("chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    wait = WebDriverWait(driver, timeout=60)
    try:
        driver.get("https://www.ekupi.ba/")
        driver.maximize_window()

        sport_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sport')]"))
        )
        action = ActionChains(driver)
        action.move_to_element(sport_button).perform()
        dropdown_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sportski pametni satovi')]"))
        )
        dropdown_link.click()

        checkbox = driver.find_element(By.XPATH, "//span[@class='facet__list__mark']")
        checkbox.click()
       
        checkbox_click_text_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='facet__name js-facet-name']")))
        checkbox_click_text = checkbox_click_text_element.text
        assert checkbox_click_text == "Aktivni filteri"
    finally:
        driver.quit()





