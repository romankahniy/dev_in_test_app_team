import time
import logging

from .page import Page
from selenium.webdriver.common.by import By


logging.basicConfig(
    level=logging.DEBUG,
    filename='logs.log',
    format='%(asctime) - %(module)s - %(levelname)s: %(lineno)d - %(message)s',
    datefmt='%H:%M:%S',
)


class LoginPage(Page):

    def login(self, username: str, password: str) -> bool:
        time.sleep(3)
        logging.info("Click login button")
        self.click_element(By.ID, 'com.ajaxsystems:id/login')
        time.sleep(3)
        logging.info("Insert username")
        self.insert_value_to_field(By.ID, 'com.ajaxsystems:id/login', username)
        time.sleep(3)
        logging.info("Insert password")
        self.insert_value_to_field(By.ID, 'com.ajaxsystems:id/password', password)
        time.sleep(3)
        logging.info("Click submit button")
        self.click_element(By.ID, "com.ajaxsystems:id/next")

        return False if self.find_element(By.ID, "com.ajaxsystems:id/snackbar_text") else True

    def click_pop_up_cancel_button(self):
        time.sleep(3)
        popup_btn = self.find_element(By.ID, "com.ajaxsystems:id/cancel_button")
        time.sleep(3)
        if popup_btn:
            time.sleep(3)
            popup_btn1 = self.find_element(By.ID, "com.ajaxsystems:id/cancel_button")
            time.sleep(3)
            popup_btn1.click()

    def sidebar_settings(self, username: str, password: str):
        time.sleep(3)
        self.login(username=username, password=password)
        time.sleep(15)

        lst = []

        logging.info("Click cancel button in the popup window")
        self.click_pop_up_cancel_button()
        time.sleep(3)

        logging.info("Click sidebar button")
        self.click_element(By.ID, "com.ajaxsystems:id/menuDrawer")
        time.sleep(3)
        logging.info("Click Add Hub button")
        self.click_element(By.ID, "com.ajaxsystems:id/addHub")
        lst.append(False if self.find_element(By.ID, "com.ajaxsystems:id/backButton") else True)
        logging.info("Click Back button")
        self.click_element(By.ID, "com.ajaxsystems:id/backButton")
        time.sleep(3)

        logging.info("Click sidebar button")
        self.click_element(By.ID, "com.ajaxsystems:id/menuDrawer")
        time.sleep(3)
        logging.info("Click App Settings button")
        self.click_element(By.ID, "com.ajaxsystems:id/settings")
        time.sleep(3)
        lst.append(False if self.find_element(By.ID, "com.ajaxsystems:id/back") else True)
        logging.info("Click Back button")
        self.click_element(By.ID, "com.ajaxsystems:id/back")
        time.sleep(3)

        logging.info("Click sidebar button")
        self.click_element(By.ID, "com.ajaxsystems:id/menuDrawer")
        time.sleep(3)
        logging.info("Click Help button")
        self.click_element(By.ID, "com.ajaxsystems:id/help")
        time.sleep(3)
        lst.append(False if self.find_element(By.ID, "com.ajaxsystems:id/back") else True)
        logging.info("Click Back button")
        self.click_element(By.ID, "com.ajaxsystems:id/back")
        time.sleep(3)

        logging.info("Click sidebar button")
        self.click_element(By.ID, "com.ajaxsystems:id/menuDrawer")
        time.sleep(3)
        logging.info("Click Report a problem button")
        self.click_element(By.ID, "com.ajaxsystems:id/logs")
        time.sleep(3)
        lst.append(False if self.find_element(By.ID, "com.ajaxsystems:id/athenaButton") else True)

        return all(lst)
