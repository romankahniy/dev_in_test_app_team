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


class RegistrationPage(Page):

    def registration(
            self,
            username: str,
            email: str,
            email_confirm: str,
            phone_number: str,
            password: str,
            password_confirm: str
    ):
        time.sleep(3)
        logging.info("Click registration button")
        self.click_element(By.ID, 'com.ajaxsystems:id/registration')
        time.sleep(3)
        logging.info("Insert username")
        self.insert_value_to_field(By.ID, 'com.ajaxsystems:id/name', username)
        time.sleep(3)
        logging.info("Insert email")
        self.insert_value_to_field(By.ID, 'com.ajaxsystems:id/login', email)
        time.sleep(3)
        logging.info("Insert email confirmation")
        self.insert_value_to_field(By.ID, 'com.ajaxsystems:id/loginConfirm', email_confirm)
        time.sleep(3)
        logging.info("Insert phone number")
        self.insert_value_to_field(By.ID, 'com.ajaxsystems:id/phone', phone_number)
        time.sleep(3)
        logging.info("Insert password")
        self.insert_value_to_field(By.ID, 'com.ajaxsystems:id/password', password)
        time.sleep(3)
        logging.info("Insert password confirmation")
        self.insert_value_to_field(By.ID, 'com.ajaxsystems:id/passwordConfirm', password_confirm)
        time.sleep(3)
        logging.info("Click agreement button")
        self.click_element(By.ID, 'com.ajaxsystems:id/agreement')
        time.sleep(3)
        logging.info("Click create account button button")
        self.click_element(By.ID, 'com.ajaxsystems:id/mTitle')
        time.sleep(3)
        return False if self.find_element(By.ID, "com.ajaxsystems:id/snackbar_text") else True