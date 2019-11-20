import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class logout_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_logout(self):
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
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/ul/li[2]/a").click()
        assert "Logged Out"
        time.sleep(5)
        driver.get("http://127.0.0.1:8000")
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(5)




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
