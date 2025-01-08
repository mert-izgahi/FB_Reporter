from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self):
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

    def register_proxy(self, proxy):
        ip, port = proxy.split(":")
        self.driver.execute_cdp_cmd(
            "Network.setExtraHTTPHeaders",
            {
                "headers": {
                    "Proxy": f"{ip}:{port}",
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
