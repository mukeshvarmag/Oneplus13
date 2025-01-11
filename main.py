from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

# Function to load cookies from a file
def load_cookies(driver, path):
    with open(path, "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)





def reuse_cookies_and_access_site():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Path to ChromeDriver executable (update with your actual path)
    driver_path = r"C:\WebDrivers\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Step 1: Navigate to the product page
        url = "https://www.oneplus.in/product/launch/13/oneplus-bonus-drop/"
        driver.get(url)

        # Load cookies into the browser session
        cookie_file = "oneplus_cookies.pkl"
        load_cookies(driver, cookie_file)

        # Revisit the URL with cookies applied
        driver.get(url)
        print("Cookies applied. Logged in and redirected to the page.")

        # Step 3: Click on "Buy now" button
        buy_now_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Buy now']/ancestor::button"))
        )
        buy_now_button.click()
        print("'Buy now' button clicked successfully!")

        # Step 4: Click on "Check out" button
        check_out_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Check out']"))
        )
        check_out_button.click()
        print("'Check out' button clicked successfully!")

        # Step 5: Agree to terms and conditions by checking the checkbox
        agree_checkbox = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "agreeToPolicyAndTerms"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", agree_checkbox)  # Scroll into view if needed
        driver.execute_script("arguments[0].click();", agree_checkbox)  # Click using JavaScript
        print("Checkbox clicked successfully!")

        # Step 6: Click on "Place Order" button
        place_order_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "btn-falcon-place-order"))
        )
        place_order_button.click()
        print("'Place Order' button clicked successfully!")

        time.sleep(3)

        pay_now_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Pay now')]"))
        )
        pay_now_button.click()
        print("'Pay now' button clicked successfully!")

        # Step 8: Select UPI as payment method
        upi_option = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@testid='nvb_upi']//article[contains(text(), 'UPI')]"))
        )

        upi_option.click()

        print("UPI payment option selected successfully!")

        # Step 9: Fill in the UPI ID (e.g., mukeshvarma.g1@ybl)
        upi_input_field = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username@bankname']"))
        )

        upi_input_field.send_keys("mukeshvarma.g1@ybl")

        print("UPI ID entered successfully!")

        # Step 10: Click on "Verify and Pay" button
        # verify_and_pay_button = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '[testid="btn_pay"]'))
        # )
        #
        # verify_and_pay_button.click()
        #
        # print("'Verify and Pay' button clicked successfully!")

        # Wait for confirmation page or further actions (adjust time if needed)
        time.sleep(60)

    finally:
        driver.quit()

if __name__ == "__main__":
    # Step 2: Reuse saved cookies to skip login (run this afterward)
    reuse_cookies_and_access_site()
