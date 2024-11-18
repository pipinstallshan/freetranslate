import undetected_chromedriver as uc
from fake_useragent import UserAgent


def driver_return():
    options = uc.ChromeOptions()
    ua = UserAgent(browsers=['chrome'], os=['windows'])
    options.add_argument("--window-size=150,500")
    options.add_argument("--disable-automation")
    options.add_argument("--no-sandbox")
    options.add_argument('--profile-directory=Default')
    options.add_argument("--lang=en")
    options.add_argument("--enable-javascript")
    options.add_argument("--enable-cookies")
    options.add_argument(f'--user-agent={ua.random}')
    prefs = {
        "profile.default_content_setting_values": {
            "images": 2
        }
    }
    options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options, headless=True, use_subprocess=True)
    driver.maximize_window()
    return driver