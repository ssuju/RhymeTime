from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Contact Us'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Sign Up").click()
        driver.find_element_by_id("id_first_name").click()
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("Gary")
        driver.find_element_by_id("id_last_name").clear()
        driver.find_element_by_id("id_last_name").send_keys("Peters")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("gary@gmail.com")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("gpeters")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("gary")
        driver.find_element_by_id("id_password_repeat").clear()
        driver.find_element_by_id("id_password_repeat").send_keys("gary")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Confirm password:'])[1]/following::input[2]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
