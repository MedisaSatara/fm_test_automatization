from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_registracija():
    chrome_options = webdriver.ChromeOptions()
    chrome_service = webdriver.chrome.service.Service("chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    wait = WebDriverWait(driver, timeout=60)
    try:
        driver.get("https://www.ekupi.ba/")
        driver.maximize_window()
        login_link = driver.find_element(By.CLASS_NAME, 'login_link')
        login_link.click()
        time.sleep(3)
        firstname_field = driver.find_element(By.ID, "register.firstName")
        firstname_field.click()
        firstname_field.clear()
        firstname_field.send_keys("imeime")
        lastname_field = driver.find_element(By.ID, "register.lastName")
        lastname_field.click()
        lastname_field.clear()
        lastname_field.send_keys("prezime")
        mail_field = driver.find_element(By.ID, "register.email")
        mail_field.click()
        mail_field.clear()
        mail_field.send_keys("email.@gmail.com")
        password_field = driver.find_element(By.ID, "password")
        driver.execute_script("arguments[0].scrollIntoView();", password_field)
        time.sleep(2)
        password_field.click()
        time.sleep(3)
        password_field.clear()
        password_field.send_keys("jasamjasam")
        lozinka_field = driver.find_element(By.ID, "register.checkPwd")
        lozinka_field.click()
        lozinka_field.clear()
        lozinka_field.send_keys("jasamjasam")
        checkbox = driver.find_element(By.NAME, "gdprCheck")
        checkbox.click()
        checkbox = driver.find_element(By.NAME, "termsCheck")
        checkbox.click()
        time.sleep(3)
        login_link = driver.find_element(By.ID, "register-submit-btn")
        login_link.click()
        error_mail_text_element = wait.until(EC.visibility_of_element_located((By.ID, 'email.errors')))
        error_mail_text = error_mail_text_element.text
        assert error_mail_text == "Profil sa navedenom email adresom već postoji."
    finally:
        driver.quit()