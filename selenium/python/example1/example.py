from selenium import webdriver



import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        firefox_options = webdriver.FirefoxOptions()
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444',
            options=firefox_options
        )
        self.driver.get("http://www.google.com/")

    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")

        # enter search keyword and submit
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_class_namemethod

        lists = self.driver.find_elements_by_class_name("r")
        no=len(lists)
        self.assertEqual(10, len(lists))
    
    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()