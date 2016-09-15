# cef-pyhton-selenium
How to start testing CEF applications with python and selenium on windows

##Installing the Environment
1. Clone this repo
2. Download and install [Python 2.7](https://www.python.org/downloads/)
3. Download [ChromeDriver binary](https://sites.google.com/a/chromium.org/chromedriver/) and move it to c:/chromedriver
4. Add chromedriver to PATH system variable
5. Install necessary python modules
  * python -m pip install selenium
  * may be you need to install more modules (python will tell about in console)
6. Run selenium_chrome_test.py to ensure that there is no errors with python, chrome or chromedriver
  * python selenium_chrome_test.py

##Start Writing CEF-tests
1. Open calc_cef_test.py with any CodeEditor
2. Set APPLICATION_PATH value where is your CEF application is placed (in my case it was cefclient.exe)
3. Set TEST_PAGE_PATH value where is your testing html page is placed (if necessary) or use my test page from calc-proto/index.html
4. Update test case for your needs or use my test cases
4. Run python calc_cef_test.py

##Usefull Resources
* [EN: Java tutorial CEF + ChromeDriver](https://bitbucket.org/chromiumembedded/cef/wiki/UsingChromeDriver)
* [RU: Python3 + Selenium tutorial for FireFox (not CEF)](https://habrahabr.ru/post/248559/)
