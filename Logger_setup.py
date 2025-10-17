import logging
import os

def setup_log():
    # Save logs route
    BASE_DIR = os.path.dirname(os.path.abspath('Logs/'))
    LOG_DIR = os.path.join(BASE_DIR, "Logs")
    os.makedirs(LOG_DIR, exist_ok=True) #Create a new folder if it doesn't exist

    LOG_FILE = os.path.join(LOG_DIR, "scraper.log")

    # Open file in write mode (w)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("Strating scraper...\n")
        f.write("Downloading main page...\n")
        f.write("Scraping completed succesfully.\n")

    print(f"Archivo creado en: {LOG_FILE}")


    #Logging config
    logging.basicConfig(
        level=logging.INFO,  # Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),  # FILE
            logging.StreamHandler()  # Consol
        ],
        force=True

    )
    logging.info("Logger inicializado en %s", LOG_FILE)

    #return LOG_FILE