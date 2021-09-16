from selenium import webdriver
import unittest

class PythonSelenium(unittest.TestCase):

    def setUp(self):
        firefox_options = webdriver.FirefoxOptions()
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=firefox_options
        )
        self.driver.get("http://www.google.com/")

    def test_page_title_name(self):
        pageTitle = self.driver.title;
        self.assertEqual('Google', pageTitle)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
