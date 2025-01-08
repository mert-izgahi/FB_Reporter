from .locators import Locator
from .utils import wait_for_page_load
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class FB_Reporter:
    FB_URL = "https://www.facebook.com/"
    WAIT_TIME = 5

    def __init__(self, page_url, username, password, proxy=None):
        self.page_url = page_url
        self.username = username
        self.password = password
        self.proxy = proxy
        
        # Setup driver
        chrome_options = Options()
        chrome_options.add_argument(
            "--disable-notifications"
        )  # General argument to disable popups
        chrome_options.add_experimental_option(
            "prefs",
            {
                "profile.default_content_setting_values.notifications": 2
            },  # Block notifications
        )
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

        if proxy:
            self.driver = self.setup_driver_with_proxy(proxy)

    def setup_driver_with_proxy(self, proxy):
        self.driver.execute_cdp_cmd(
            "Network.setExtraHTTPHeaders",
            {
                "headers": {
                    "Proxy-Authorization": f"Basic {proxy}",
                }
            },
        )

        self.driver.execute_cdp_cmd(
            "Network.setExtraHTTPHeaders",
            {
                "headers": {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36",
                }
            },
        )

        return self.driver
    
    def report(self):
        try:
            self.driver.get(self.FB_URL)
            # Authentication
            username_field = self.driver.find_element(*Locator.USERNAME_FIELD)
            username_field.send_keys(self.username)
            password_field = self.driver.find_element(*Locator.PASSWORD_FIELD)
            password_field.send_keys(self.password)
            login_button = self.driver.find_element(*Locator.LOGIN_BUTTON)
            login_button.click()
            # Navigate to the target page
            self.driver.get(self.page_url)
            wait_for_page_load(self.driver)
            # Click on the "Options" button
            options_button = self.driver.find_element(*Locator.OPTIONS_DROPDOWN_BUTTON)
            options_button.click()

            # Click on the "Report" button
            report_button = self.driver.find_element(*Locator.REPORT_BUTTON)
            report_button.click()
            # Wait FOR REPORT MODAL
            time.sleep(self.WAIT_TIME)

            # Click on the "Report Type" button
            report_type_button = self.driver.find_element(*Locator.REPORT_TYPE_BUTTON)
            report_type_button.click()

            # Wait FOR REPORT MODAL
            time.sleep(self.WAIT_TIME)

            # Click on the "Report Second Type" button
            report_second_type_button = self.driver.find_element(
                *Locator.REPORT_SECOND_TYPE_BUTTON
            )
            report_second_type_button.click()

            # Wait FOR REPORT MODAL
            time.sleep(self.WAIT_TIME)

            # Click on the "Report Third Type" button
            report_third_type_button = self.driver.find_element(
                *Locator.REPORT_THIRD_TYPE_BUTTON
            )
            report_third_type_button.click()

            # Wait FOR REPORT MODAL
            time.sleep(self.WAIT_TIME)

            # Click on the "Send Report" button
            send_report_button = self.driver.find_element(*Locator.SEND_REPORT_BUTTON)
            send_report_button.click()

            # Wait FOR REPORT MODAL
            time.sleep(self.WAIT_TIME)
        except Exception as e:
            print(f"Error during reporting: {e}")  # Add meaningful logs
        finally:
            self.driver.quit()

