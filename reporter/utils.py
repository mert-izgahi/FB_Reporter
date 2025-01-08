from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_for_page_load(driver, timeout=10):
    element = WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    return element


def wait_for_element(driver, by, locator, timeout=10):
    element = WebDriverWait(driver, timeout=timeout).until(
        EC.presence_of_element_located((by, locator))
    )
    return element


def load_proxies_list(file_path):
    with open(file_path, "r") as f:
        proxies = f.read().splitlines()
    return proxies


def register_proxy(driver, proxy):
    ip, port = proxy.split(":")
    driver.execute_cdp_cmd(
        "Network.setExtraHTTPHeaders",
        {
            "headers": {
                "Proxy": f"{ip}:{port}",
            }
        },
    )
    driver.execute_cdp_cmd(
        "Network.setExtraHTTPHeaders",
        {
            "headers": {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36",
            }
        },
    )

    return driver
