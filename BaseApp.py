from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait
import logging


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            ES.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def get_element_property(self, locator, property_element):
        element = self.find_element(locator)
        return element.value_of_css_property(property_element)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def filling_field(self, word, locator):
        logging.info(f'Send "{word}" to element {locator[1]}')
        field = self.find_element(locator)
        field.clear()
        field.send_keys(word)

    def click_button(self, msg, locator):
        logging.info(f'Click button - "{msg}"')
        self.find_element(locator).click()
