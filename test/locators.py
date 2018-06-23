from selenium.webdriver.common.by import By

class MainPageLocators(object):
    EMAIL_INPUT = 'mailbox:login'
    PASSWD_INPUT = 'mailbox:password'
    SUBMIT_BUTTON = (By.ID, 'mailbox:submit')
    
class MailListPageLocators(object):
	WRITE_MAIL_BUTTON = (By.LINK_TEXT, 'Написать письмо')


class MailSendPageLocators(object):
	MAIL_ADDRESS_INPUT = (By.XPATH, '//textarea[2]')
	MESSAGE_INPUT_FRAME = (By.XPATH, '//*[contains(@id, "composeEditor_ifr")]')
	MAIL_MESSAGE_INPUT = (By.ID, 'tinymce')
	SEND_MAIL_BUTTON = (By.XPATH, "//*[contains(text(), 'Отправить')]")