import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.google.com');
search_box = driver.find_element_by_name('q')
search_box.send_keys('sokolnikovalexey/cef-pyhton-selenium')
search_box.submit()
time.sleep(5) # Delete this string if don't want to see results in Chrome Browser
driver.quit()