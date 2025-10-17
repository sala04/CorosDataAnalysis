import logging
from Scraper.settings import TIMEOUT
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def found_activity(driver, original_window):
    try:
        #Activity list
        wait_list = WebDriverWait(driver, TIMEOUT)
        Activity_list = wait_list.until(EC.presence_of_element_located((By.XPATH, '(//div[@class="arco-tabs-tab"])[2]')))
        Activity_list.click()

        #Specific activity
        wait_act = WebDriverWait(driver, TIMEOUT)
        Activity_act = wait_act.until(EC.element_to_be_clickable((By.XPATH, '(//div[@class="block-image activity-image"]/a)[1]')))
        Activity_act.click()

        # Wait for the new window or tab
        wait = WebDriverWait(driver, TIMEOUT)
        wait.until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        #Export data
        wait_export = WebDriverWait(driver, TIMEOUT)
        export_div = wait_export.until(EC.element_to_be_clickable((By.XPATH, '//i[contains(@class, "export-icon") and @title="Export"]')))
        export_div.click()

        #Download file
        wait_down = WebDriverWait(driver,TIMEOUT)
        download = wait_down.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'export-activity__file-type-icon')])[2]")))
        #download = wait_down.until(EC.element_to_be_clickable((By.XPATH, '//div[i[contains(@class, "icontcx")]]')))
        download.click()

        logging.info("Downloading File")

        #if(download.click and wait_quit):
        #   driver.quit()

    except:
        if window_handle != original_window:
            logging.error("The file can not be downloaded")
        else:
            logging.error("No activty found")