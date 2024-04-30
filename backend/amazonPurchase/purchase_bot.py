import random
import time

from purchase_bot_constants import AMAZON_PASSWORD, AMAZON_USERNAME
from purchase_bot_helpers import (
    find_and_solve_captcha,
    get_chrome_binary,
    random_typing,
)
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
    options.binary_location = get_chrome_binary()
    service = Service(ChromeDriverManager().install())

    # Initialise the Chrome driver with options and service
    driver = webdriver.Chrome(service=service, options=options)
    print("WebDriver initiated.")

    # Open the login page
    driver.get(
        "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"  # noqa E501
    )
    print("Login page loaded.")

    # Wait for the page to load
    time.sleep(random.uniform(1, 5))

    # Wait a moment for any CAPTCHA to possibly appear
    try:
        find_and_solve_captcha(driver)
    except Exception as e:
        print(f"No CAPTCHA found or failed to solve CAPTCHA: {e}")

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

    # Wait a moment for any CAPTCHA to possibly appear
    try:
        find_and_solve_captcha(driver)
    except Exception as e:
        print(f"No CAPTCHA found or failed to solve CAPTCHA: {e}")

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

    # Wait for the next page (password page)
    time.sleep(random.uniform(1, 3))

    # Wait a moment for any CAPTCHA to possibly appear
    try:
        find_and_solve_captcha(driver)
    except Exception as e:
        print(f"No CAPTCHA found or failed to solve CAPTCHA: {e}")

    # INPUT OTP Code
    try:
        inputs = driver.find_elements(By.TAG_NAME, "input")

        # Filter to find input with maxlength of 6
        for input_field in inputs:
            if input_field.get_attribute("maxlength") == "6":
                print("Found an input field with maxlength 6.")
                user_input = input(
                    "Please enter the text you want to type (max 6 characters): "  # noqa E501
                )
                # Type the user's input into the field
                random_typing(input_field, user_input)
                random_typing(password_input, Keys.RETURN)
                print("OTP Code sent")
        else:
            print("No input field with maxlength 6 found.")
    except Exception as e:
        print(f"Failed to find or interact with the password input: {e}")

    # Wait a moment for any CAPTCHA to possibly appear
    try:
        find_and_solve_captcha(driver)
    except Exception as e:
        print(f"No CAPTCHA found or failed to solve CAPTCHA: {e}")

    # TODO: Begin purchase logic here
    time.sleep(120)

    driver.quit()


if __name__ == "__main__":
    login_to_amazon(AMAZON_USERNAME, AMAZON_PASSWORD)
