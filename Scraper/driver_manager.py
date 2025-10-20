from Scraper.login import logging
from datetime import datetime
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService




def create_drivers (headless=False):
    try:
        logging.info("Creating drivers")
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")

        # ⚙️ Configurar preferencias de descarga
        options.set_preference("browser.download.folderList", 2)  # 2 = ruta personalizada
        options.set_preference("browser.download.dir", str(activity_folder()))
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "application/zip,application/gpx+xml,text/csv,application/octet-stream,application/vnd.google-earth.kml+xml"
        )
        options.set_preference("pdfjs.disabled", True)  # Desactiva visor de PDF integrado

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        return driver

    except:
        logging.error("Driver could not be created")


def activity_folder():
    timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.dirname(BASE_DIR)
    LOG_DIR = os.path.join(ROOT_DIR, f"Activities/{timestamp}")
    os.makedirs(LOG_DIR, exist_ok=True)

    return LOG_DIR
