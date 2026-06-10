import unittest

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy


class BstackSampleTest(unittest.TestCase):
    def setUp(self):
        # The BrowserStack SDK injects the app + device capabilities from
        # browserstack.yml at runtime, so an empty options object is enough.
        options = XCUITestOptions()
        self.driver = webdriver.Remote(
            "https://hub.browserstack.com/wd/hub",
            options=options,
        )
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_text_echo(self):
        # BStackSampleApp.ipa flow:
        # open the text screen, type a value, assert it is echoed back.
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text Button").click()

        text_input = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text Input")
        text_input.send_keys("hello@browserstack.com\n")

        output = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text Output")
        self.assertEqual(output.text, "hello@browserstack.com")


if __name__ == "__main__":
    unittest.main()
