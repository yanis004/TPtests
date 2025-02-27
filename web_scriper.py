from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.cdiscount.com/"


driver.get(url)


time.sleep(5)


try:
    bloc_annonces = driver.find_element(By.CLASS_NAME, "c-carousel__list")
    annonces = bloc_annonces.find_elements(By.TAG_NAME, "li")
    print(f"Nombre de produits trouvés: {len(annonces)}")


    for annonce in annonces: 
        try:
            titre = annonce.find_element(By.CSS_SELECTOR, ".u-line-clamp--2").text 
        except:
            titre = "Titre non trouvé"

        try:
            prix = annonce.find_element(By.CLASS_NAME, "prix").text
        except:
            prix = "Prix non trouvé"

        try:
            url = annonce.find_element(By.TAG_NAME, "a").get_attribute("href") 
        except:
            url = "URL non trouvée"

        print(f"Titre: {titre}\nPrix: {prix}\nURL: {url}\n{'-'*50}")

except Exception as e:
    print(f"Erreur lors de la récupération des produits: {str(e)}")


driver.quit()