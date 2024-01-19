import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def test_correct_login():
    chrome_options=webdriver.ChromeOptions()
    chrome_service= Service("chromedriver.exe")
    driver=webdriver.Chrome(service=chrome_service,options=chrome_options)
    wait=WebDriverWait(driver,timeout=60)
    driver.get("https://www.ekupi.ba/")
    time.sleep(3)
    login_link=driver.find_element(By.CLASS_NAME, 'login_link')
    login_link.click()
    time.sleep(3)
    mail_field=driver.find_element(By.ID,"j_username")
    mail_field.click()
    mail_field.clear()
    mail_field.send_keys("tt6271962@gmail.com")
    lozinka_field=driver.find_element(By.ID,"j_password")
    lozinka_field.click()
    lozinka_field.clear()
    lozinka_field.send_keys("testtest123.")
    time.sleep(3)
    login_link=driver.find_element(By.ID,"submit")
    login_link.click()
    welcome_text_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logged_in')))
    welcome_text = welcome_text_element.text
    assert welcome_text == "Dobrodošli imeime"
    driver.quit()