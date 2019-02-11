from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class EmailInputElement(BasePageElement):

    locator = MainPageLocators.EMAIL_INPUT


class PasswordInputElement(BasePageElement):

    locator = MainPageLocators.PASSWD_INPUT


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    email_input_element = EmailInputElement()
    password_input_element = PasswordInputElement()

    def is_title_matches(self):
        return "Mail" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)
        element.click()


class MailListPage(BasePage):

    def click_mail_send_button(self):
        self.driver.find_element(*MailListPageLocators.WRITE_MAIL_BUTTON).click()


class MailSendPage(BasePage):

    def new_mail_check(self):
        return "Новое письмо" in self.driver.title

    def mail_address(self, address):
        self.driver.find_element(*MailSendPageLocators.MAIL_ADDRESS_INPUT).send_keys(address)

    def mail_message(self, message):
        iframe = self.driver.find_element(*MailSendPageLocators.MESSAGE_INPUT_FRAME)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*MailSendPageLocators.MAIL_MESSAGE_INPUT).send_keys(message)
        self.driver.switch_to_default_content()

    def send_mail(self):
        element = self.driver.find_element(*MailSendPageLocators.SEND_MAIL_BUTTON)
        element.click()

    def send_check(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception:
            pass
        return "Письмо отправлено" in self.driver.title
