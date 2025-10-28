import logging
import fnmatch
from pathlib import Path
from Scraper.settings import TIMEOUT
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def file_type(driver, file): #Downlowd the activity file
    # Download file
    wait_down = WebDriverWait(driver, TIMEOUT)
    download = wait_down.until(
    EC.element_to_be_clickable((By.XPATH, f"(//div[contains(@class, 'export-activity__file-type-icon')])[{file}]")))
    download.click()
    logging.info("Downloading File")
