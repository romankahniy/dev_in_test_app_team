from appium.webdriver import WebElement
from selenium.common.exceptions import NoSuchElementException


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by: str, locator: str) -> WebElement | None:
        self.driver.implicitly_wait(10)
        try:
            return self.driver.find_element(by=by, value=locator)
        except NoSuchElementException:
            return None

    def click_element(self, by: str, locator: str) -> None:
        self.find_element(by=by, locator=locator).click()

    def insert_value_to_field(self, by: str, locator: str, value: str) -> None:
        self.find_element(by=by, locator=locator).send_keys(value)
