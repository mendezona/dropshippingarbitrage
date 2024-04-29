import random
import time

from selenium.webdriver.remote.webelement import WebElement


def random_typing(element: WebElement, text):
    for character in text:
        element.send_keys(character)
        time.sleep(random.uniform(0.1, 3))
