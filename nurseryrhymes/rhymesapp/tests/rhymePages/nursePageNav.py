import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class nursePageNav(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testNav(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/home/")
        time.sleep(2)
        x = driver.find_element_by_xpath("html/body/nav/div/div[2]/ul/li[2]/a")
        x.click()
        time.sleep(2)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/a[6]/h3")
        x.click()
        time.sleep(1)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/a/span")
        x.click()
        time.sleep(5)
        x = driver.find_element_by_xpath("html/body/div/div/div/div[2]/a[2]/span")
        x.click()
        time.sleep(3)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/a/h3")
        x.click()
        time.sleep(2)
        x = driver.find_element_by_xpath("html/body/div/div/div/div/a/span")
        x.click()
        time.sleep(3)
        x = driver.find_element_by_xpath("html/body/div/div/div/div[2]/a/span")
        x.click()
        time.sleep(2)




    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
