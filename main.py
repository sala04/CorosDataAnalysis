import logging
from Logger_setup import setup_log
from Scraper.main_scraper import scraper

def main():

    setup_log()
    scraper()

if __name__ == "__main__":
    main()











'''
with open('Docs/bcn_julia', 'r') as archivo:
    bps = [int(linea.strip()) for linea in archivo]

Total = len(bps)

for numero in bps:
    result = clasificar_zona(numero,28)

visual_zone(result)

# Ejemplo de uso
fcm = 27  # Frecuencia cardíaca máxima
fc_actual = 155  # Frecuencia actual'''

#zona = clasificar_zona(fc_actual, fcm)
#print(f"Estás en: {zona}")