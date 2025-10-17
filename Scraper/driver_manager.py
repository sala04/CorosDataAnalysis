from Scraper.login import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


def create_drivers (headless=False):
    try:
        logging.info("Creating drivers")
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        return driver

    except:
        logging.error("Driver could not be created")


