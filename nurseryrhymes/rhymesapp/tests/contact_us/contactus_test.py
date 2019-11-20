import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Upgrade(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_upgrade(self):
        user = "rhymetime"
        pwd = "team3!"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)

        subject = "rhymetime"
        Email = "ebuettner5@gmail.com"
        message = "This is a selenium test"
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
        elem = driver.find_element_by_id("id_subject")
        elem.send_keys(subject)

        time.sleep(5)
        elem = driver.find_element_by_id("id_email_address")
        elem.send_keys(Email)
        time.sleep(5)

        elem = driver.find_element_by_id("id_message")
        elem.send_keys(message)
        time.sleep(5)

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[4]/input").click()



        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
