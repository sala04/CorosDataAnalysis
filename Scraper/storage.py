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



"""
def get_latest_file(folder: Union[str, Path],
                    pattern: str = "*",
                    ignore_patterns: Optional[List[str]] = None) -> Optional[Path]:

    folder = Path(folder)
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Carpeta no encontrada: {folder}")

    files = []
    for p in folder.iterdir():
        if not p.is_file():
            continue
        if not fnmatch.fnmatch(p.name, pattern):
            continue
        if ignore_patterns and any(fnmatch.fnmatch(p.name, pat) for pat in ignore_patterns):
            continue
        files.append(p)

    if not files:
        return None

    # Selecciona por tiempo de modificación (más reciente)
    latest = max(files, key=lambda p: p.stat().st_mtime)
    return latest

def modify(file):
    match file:
        case 1: #File .fit
            modify_fit()

        case 2: #File .tcx
            modify_tcx()

        case 3: #File .gpx
            modify_gpx()

        case 4: #File .kml
            modify_klm()

        case 5: #File .csv
            modify_csv()

def modify_fit():
def modify_tcx():
def modify_gpx():
def modify_klm():
def modify_csv():
"""