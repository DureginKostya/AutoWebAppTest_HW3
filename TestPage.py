from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocator:

    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LABEL_BLOG = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CREATE_NEW_BLOG_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_NEW_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_NEW_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_NEW_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_DATE_CREATE_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[5]/div/div/label/input""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_TITLE_NEW_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_TITLE_CONTACT_US = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_NAME_CONTACT_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_CONTACT_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_CONTACT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationHelper(BasePage):

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocator.LOCATOR_ERROR_FIELD)
        msg = error_field.text
        logging.info(f'We find text "{msg}" in error field {TestSearchLocator.LOCATOR_ERROR_FIELD[1]} ')
        return msg

    def get_text_blog(self):
        label_blog = self.find_element(TestSearchLocator.LOCATOR_LABEL_BLOG)
        msg = label_blog.text
        logging.info(f'We find text "{msg}" in field Blog {TestSearchLocator.LOCATOR_LABEL_BLOG[1]} ')
        return msg

    def get_title_new_post(self):
        title_new_post = self.find_element(TestSearchLocator.LOCATOR_TITLE_NEW_POST)
        msg = title_new_post.text
        logging.info(f'We find text "{msg}" in field Title {TestSearchLocator.LOCATOR_TITLE_NEW_POST[1]} ')
        return msg

    def get_title_contact_us(self):
        title_contact_up = self.find_element(TestSearchLocator.LOCATOR_TITLE_CONTACT_US)
        msg = title_contact_up.text
        logging.info(f'We find text "{msg}" in field Title {TestSearchLocator.LOCATOR_TITLE_CONTACT_US[1]} ')
        return msg

    def get_alert_message(self):
        alert = self.driver.switch_to.alert
        msg = alert.text
        logging.info(f'Open alert with message {msg}')
        alert.accept()
        return msg

