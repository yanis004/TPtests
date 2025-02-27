import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fixture pour configurer et fermer le navigateur
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_facebook_signup(driver):
    """Test de création de compte sur Facebook"""

    driver.get("https://www.facebook.com/")
    assert "Facebook" in driver.title  

   
    try:
        creer_compte_btn = driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']")
        driver.execute_script("arguments[0].scrollIntoView();", creer_compte_btn)
        creer_compte_btn.click()
        time.sleep(2)  

        # Remplir le formulaire
        driver.find_element(By.NAME, "firstname").send_keys("Reda")
        driver.find_element(By.NAME, "lastname").send_keys("Khouya")
        driver.find_element(By.NAME, "reg_email__").send_keys("reda.khouya@gmail.com")
        driver.find_element(By.NAME, "reg_passwd__").send_keys("MotDePasse123!")
        driver.find_element(By.ID, "day").send_keys("27")
        driver.find_element(By.ID, "month").send_keys("fév")
        driver.find_element(By.ID, "year").send_keys("1999")

        # Cliquez sur le genre 
        sexe = driver.find_element(By.XPATH, "//input[@value='2']")
        driver.execute_script("arguments[0].click();", sexe)

        # Soumettre le formulaire
        submit_btn = driver.find_element(By.NAME, "websubmit")
        driver.execute_script("arguments[0].click();", submit_btn)
        time.sleep(2)

    
        driver.save_screenshot("apres_soumission.png")

    except Exception as e:
        print(f"Erreur pendant le test : {e}")
