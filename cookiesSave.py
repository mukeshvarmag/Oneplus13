from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle


# Function to save cookies to a file
def save_cookies(driver, path):
    with open(path, "wb") as file:
        pickle.dump(driver.get_cookies(), file)

# Automate login and save cookies
def automate_login_and_save_cookies():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Path to ChromeDriver executable
    driver_path = r"C:\WebDrivers\chromedriver-win64\chromedriver.exe"  # Replace with your actual path

    # Initialize WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the OnePlus website
        driver.get("https://www.oneplus.in/")
        time.sleep(10)

        # Wait for the "Sign In" button and click it
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-info > a"))
        ).click()

        # Switch to the login iframe
        WebDriverWait(driver, 60).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name^='heytap_popper_login']"))
        )

        # Click on "Sign in with third-party"
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='third_party_icon']"))
        ).click()

        # Fill in the email field
        email_field = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Email']"))
        )
        email_field.click()
        email_field.send_keys("mukeshvarma.g@gmail.com")

        # Click "Sign in with password" link
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign in with password"))
        ).click()

        # Fill in the password field
        password_field = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Password required']"))
        )
        password_field.click()
        password_field.send_keys("Goneplus@18")

        # Wait for login to complete (adjust time if needed)
        time.sleep(45)

        # Save cookies after successful login
        save_cookies(driver, "oneplus_cookies.pkl")
        print("Cookies saved successfully!")

    finally:
        driver.quit()

if __name__ == "__main__":
    # Step 1: Automate login and save cookies (run this once)
    automate_login_and_save_cookies()

