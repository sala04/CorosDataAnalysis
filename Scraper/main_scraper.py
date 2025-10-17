import logging
from Scraper.fetch import found_activity
from Scraper.driver_manager import create_drivers
from Scraper.login import login

def scraper():

        try:

                driver = create_drivers()
                window = login(driver)
                found_activity(driver, window)

        except:
                logging.error("Scraping failed")


