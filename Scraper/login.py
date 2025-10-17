import logging
from Scraper.settings import Login_URL
from Scraper.settings import username
from Scraper.settings import password
from selenium.webdriver.common.by import By


def login(driver):
    try:
        driver.get(Login_URL)

        original_window = driver.current_window_handle
        assert len(driver.window_handles) == 1

        # User/Email
        login_user = driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
        login_user.click()
        login_user.send_keys(username)

        # Password
        login_pass = driver.find_element(By.XPATH,'//input[@placeholder="Por favor introduzca una contraseña con 6-20 caracteres"]')
        login_pass.click()
        login_pass.send_keys(password)

        # Accept user terms
        Terms = driver.find_element(By.XPATH, '(//div[@class="arco-checkbox-icon"])[2]')
        Terms.click()

        # Log in button
        login_btn = driver.find_element(By.XPATH, "//button[contains(normalize-space(), 'Iniciar sesión')]")
        login_btn.click()

        if login_btn.click():
            logging.INFO("Loged in")

        return original_window

    except:
        logging.error("Unable to log in")
