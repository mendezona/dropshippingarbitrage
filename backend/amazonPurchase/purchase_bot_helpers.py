import base64
import platform
import random
import time

import requests
from purchase_bot_constants import TWOCAPTCHA_API_KEY
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from twocaptcha import TwoCaptcha


def random_typing(element: WebElement, text):
    """
    Simulates randomised time between key presses

    :param element: The WebElement to interact with
    :param text: The text to input into the WebElement
    """
    for character in text:
        element.send_keys(character)
        time.sleep(random.uniform(0.5, 1.5))


def find_and_solve_captcha(driver, substring="captcha"):
    """
    Find a form element whose action attribute contains a specific substring,
    case agonistically

    :param driver: The Selenium WebDriver instance
    :param substring: Substring to search for in the action attribute of form
    elements
    """
    # Normalize the substring to lowercase for case-insensitive comparison
    normalized_substring: str = substring.lower()
    # XPath expression using translate() for case-insensitive search
    xpath_expression: str = (
        f"//form[contains(translate(@action, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{normalized_substring}')]"  # noqa E501
    )

    try:
        # Find if recaptcha exists
        form_element = driver.find_element(By.XPATH, xpath_expression)
        print(
            "Form found with action containing 'captcha', case-insensitively."
        )

        if form_element:
            print("Begin to solve recaptcha.")

            # Find image and send it to recaptcha service
            image_element = driver.find_element(By.TAG_NAME, "img")
            image_url = image_element.get_attribute("src")
            solver = TwoCaptcha(TWOCAPTCHA_API_KEY)
            result = solver.normal(encode_image_url_to_base64(image_url))
            print("Recaptcha result:", result)

            # Submit recaptcha result
            inputs = driver.find_elements(By.TAG_NAME, "input")
            for input_field in inputs:
                if "captcha" in input_field.get_attribute("id").lower():
                    print("Found the captcha input field.")
                    # Text to be sent to the captcha input field
                    input_text = result["code"]
                    # Type the text into the captcha field
                    random_typing(input_field, input_text)
                    random_typing(input_field, Keys.RETURN)

    except Exception as e:
        print("No recaptcha found", e)


def encode_image_url_to_base64(image_url: str) -> str:
    """
    Fetch an image from a URL and encode it to a base64 string

    :param image_url The URL of the image to be encoded
    """
    response: requests.Response = requests.get(image_url)
    response.raise_for_status()
    base64_encoded_data: bytes = base64.b64encode(response.content)
    base64_message: str = base64_encoded_data.decode("utf-8")
    return base64_message


def get_chrome_binary():
    # Detect the operating system
    os_name = platform.system().lower()
    if os_name == "darwin":  # macOS
        return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    elif os_name == "windows":  # Windows
        return "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    else:
        raise EnvironmentError("Unsupported operating system")
