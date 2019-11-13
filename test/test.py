import unittest
from selenium import webdriver
import page
import argparse


class MailruSendMail(unittest.TestCase):
    def __init__(self, testname, username, passw, email):
        super(MailruSendMail, self).__init__(testname)
        self.username = username
        self.passw = passw
        self.email = email

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("http://mail.ru")

    def test_mail_send(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "mail.ru title doesn't match."

        main_page.email_input_element = self.username
        main_page.click_go_button()
        main_page.password_input_element = self.passw
        main_page.click_go_button()

        mail_list_page = page.MailListPage(self.driver)
        mail_list_page.click_mail_send_button()

        mail_send_page = page.MailSendPage(self.driver)
        assert mail_send_page.new_mail_check(), "send mail page load failed"
        mail_send_page.mail_address(self.email)
        mail_send_page.mail_message('hello world of tests')
        mail_send_page.send_mail()
        assert mail_send_page.send_check(), "mail not send."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mailru selenium send mail")
    parser.add_argument("-u", "--username", help="username", required=True)
    parser.add_argument("-p", "--password", help="password", required=True)
    parser.add_argument("-m", "--email", help="email", required=True)
    args = parser.parse_args()

    test_loader = unittest.TestLoader()
    test_names = test_loader.getTestCaseNames(MailruSendMail)

    suite = unittest.TestSuite()
    for test_name in test_names:
        suite.addTest(MailruSendMail(test_name, args.username, args.password, args.email))

    result = unittest.TextTestRunner().run(suite)
