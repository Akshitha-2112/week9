from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# --- Setup Chrome options ---
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # hide Chrome logs

driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    # --- Open your web app ---
    driver.get("http://localhost:30698")
    wait = WebDriverWait(driver, 10)

    # --- Fill the registration form ---
    wait.until(EC.presence_of_element_located((By.NAME, "full_name"))).send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("test_user@gmail.com")
    driver.find_element(By.NAME, "username").send_keys("testuser123")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "confirm_password").send_keys("password123")
    driver.find_element(By.NAME, "phone").send_keys("9876543210")
    driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
    driver.find_element(By.NAME, "gender").send_keys("Male")
    driver.find_element(By.NAME, "address").send_keys("Hyderabad, India")

    # --- Wait for submit button and click ---
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    time.sleep(1)

    try:
        submit_btn.click()
    except:
        driver.execute_script("arguments[0].click();", submit_btn)

    time.sleep(3)
    print("[PASS] Test Completed Successfully!")

except Exception as e:
    print("[FAIL] Test failed due to error:", e)

finally:
    driver.quit()
