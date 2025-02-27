from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def attendre_et_fermer_cookies(driver):
    """Ferme automatiquement la pop-up cookies dès qu'elle apparaît."""
    try:
        reject_cookies_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Refuser les cookies optionnels')]")
        reject_cookies_button.click()
        print(" Bouton 'Refuser les cookies optionnels' cliqué.")
        time.sleep(3)
    except Exception as e:
        print(f" Aucun pop-up de cookies détecté. Erreur: {e}")

def creer_compte_facebook():
    #  Options pour contourner les blocages
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Démarrer WebDriver avec les options
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.facebook.com/")
        wait = WebDriverWait(driver, 20)

        attendre_et_fermer_cookies(driver)

        creer_compte_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='open-registration-form-button']")))
        driver.execute_script("arguments[0].scrollIntoView();", creer_compte_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", creer_compte_btn)  
        print("✅ Bouton 'Créer un compte' cliqué !")

        wait.until(EC.presence_of_element_located((By.NAME, "firstname")))

        driver.find_element(By.NAME, "firstname").send_keys("Reda")
        driver.find_element(By.NAME, "lastname").send_keys("Khouya")
        driver.find_element(By.NAME, "reg_email__").send_keys("mohamed.elkadiri@ecoles-epsi.net")
        driver.find_element(By.NAME, "reg_passwd__").send_keys("MotDePasse123!")

        driver.find_element(By.ID, "day").send_keys("27")
        driver.find_element(By.ID, "month").send_keys("fév")
        driver.find_element(By.ID, "year").send_keys("1999")

        sexe = driver.find_element(By.XPATH, "//input[@value='2']")
        driver.execute_script("arguments[0].click();", sexe)
        print("Genre sélectionné !")

        submit_btn = wait.until(EC.element_to_be_clickable((By.NAME, "websubmit")))
        driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", submit_btn)
        print("Formulaire soumis !")

        try:
            confirmation_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Nous avons envoyé un e-mail')]")))
            print("Page de confirmation email détectée !")
        except:
            print(" Erreur : La page de confirmation email n'a pas été détectée.")

        # Capture d'écran après la soumission
        driver.save_screenshot("apres_soumission.png")

        # Pause pour voir le résultat
        time.sleep(10)

    finally:
        driver.quit()

if __name__ == "__main__":
    creer_compte_facebook()
