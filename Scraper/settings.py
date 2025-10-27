from pathlib import Path
import json


Base_URL = "https://t.coros.com"
Login_URL = f"{Base_URL}/login?lastUrl=%2Fadmin%2Fviews%2Fdash-board"


#Selenium parameters
Selenium_driver = "Firefox"
TIMEOUT = 10
HEADLESS = False

#Credentials
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
DOCS_DIR = ROOT_DIR / "Docs"
archivo = DOCS_DIR / "PSW.json"
print(archivo)

with open(archivo, "r", encoding="utf-8") as file:
    data = json.load(file)


print(data)
# {'User': 'Jorge', 'Edad': 28, 'Ciudad': 'Madrid'}

print(data["User"])
# Jorge


