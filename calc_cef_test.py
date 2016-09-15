import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    APPLICATION_PATH = '/path/to/your/cef/app.exe'
    TEST_PAGE_PATH = 'calc_proto/index.html' #here should be path to your testing page

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = self.APPLICATION_PATH
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get(self.TEST_PAGE_PATH)

    def test_math_operations(self):
        driver = self.driver
        operand1 = driver.find_element_by_id('operand1')
        operand2 = driver.find_element_by_id('operand2')
        result = driver.find_element_by_id('result')
        calculateButton = driver.find_element_by_id('calculateButton')

        operand1.send_keys('2')
        operand2.send_keys('3')
        calculateButton.click()
        assert result.get_attribute('value') == '5'

        #unkomment string below to see the result in cef application
        #time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()