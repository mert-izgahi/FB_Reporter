from reporter import reporter
from reporter.utils import load_proxies_list
import random

TARGET_PAGE = "https://www.facebook.com/profile.php?id=61567627802700&sk=reels_tab"
USERNAME = "mertizgahi900@gmail.com"
PASSWORD = "Yusuf17Aslan24@"


proxies = load_proxies_list("proxies.txt")
random_proxy = random.choice(proxies)

client = reporter.FB_Reporter(
    page_url=TARGET_PAGE, username=USERNAME, password=PASSWORD, proxy=random_proxy
)

client.report()

input("Press enter to exit...")
