import random
import time

from purchase_bot_helpers import random_typing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


def login_to_amazon(username: str, password: str):
    # Set Chrome options and service
    options = Options()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # Path to Chrome on your machine
    service = Service(ChromeDriverManager().install())

    # Initialize the Chrome driver with options and service
    driver = webdriver.Chrome(service=service, options=options)
    print("WebDriver initiated.")

    # Open the login page
    driver.get(
        "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    )
    print("Login page loaded.")

    # Wait for the page to load
    time.sleep(random.uniform(1, 3))

    # Input the email or phone number
    try:
        email_input: WebElement = driver.find_element(
            By.CSS_SELECTOR, "input[type='email']"
        )
        print("Email input field found.")
        random_typing(email_input, username)
        random_typing(email_input, Keys.RETURN)
        print("Username entered.")
    except Exception as e:
        print(f"Failed to find or interact with the email input: {e}")

    # Wait for the next page (password page)
    time.sleep(random.uniform(1, 3))

    try:
        # Input the password
        password_input: WebElement = driver.find_element(
            By.CSS_SELECTOR, "input[type='password']"
        )
        print("Password input field found.")
        random_typing(password_input, password)
        random_typing(password_input, Keys.RETURN)
        print("Password entered.")
    except Exception as e:
        print(f"Failed to find or interact with the password input: {e}")

    # Wait for possible CAPTCHA or further actions
    time.sleep(5)
    print("Waiting for any post-login processes to complete.")

    # Assume now logged in and do other actions, e.g., navigate to a product page
    # ...

    # Close the browser when all tasks are completed
    # driver.quit()


if __name__ == "__main__":
    login_to_amazon("your_username_here", "your_password_here")
    test = "test"
