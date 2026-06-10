import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class BstackSampleTest(unittest.TestCase):
    def setUp(self):
        # The BrowserStack SDK injects the app + device capabilities from
        # browserstack.yml at runtime, so an empty options object is enough.
        options = UiAutomator2Options()
        self.driver = webdriver.Remote(
            "https://hub.browserstack.com/wd/hub",
            options=options,
        )
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_search_wikipedia(self):
        # WikipediaSample.apk flow:
        # tap the "Search Wikipedia" entry point, type a query, assert results.
        search_element = self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"
        )
        search_element.click()

        insert_text_element = self.driver.find_element(
            AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"
        )
        insert_text_element.send_keys("BrowserStack")

        # Allow the result list to render.
        import time
        time.sleep(5)

        results = self.driver.find_elements(
            AppiumBy.CLASS_NAME, "android.widget.TextView"
        )
        self.assertGreater(len(results), 0)


if __name__ == "__main__":
    unittest.main()
