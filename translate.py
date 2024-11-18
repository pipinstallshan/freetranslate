import time
import traceback
from colorama import Fore, Style
from .webdriver import driver_return 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TranslateFree:
    def __init__(self):
        """
        Initializes the YandexTranslator class.
        Sets up the WebDriver and translation settings.
        """
        self.driver = None

    def init_driver(self):
        """Initialize the WebDriver instance if not already done."""
        if self.driver is None:
            self.driver = driver_return()
            print(Fore.CYAN + "[INFO] WebDriver initialized and running.")

    def translate_string(self, text_to_enter, dest, source="en"):
        """
        Translates a given string using Yandex Translate and Selenium.
        
        Args:
            text_to_enter (str): Text to translate.
            dest (str): Destination language code (e.g., 'de' for German).
            source (str): Source language code (default is 'en' for English).

        Returns:
            str: Translated text.
        """
        try:
            self.init_driver()
            self.driver.get(f"https://translate.yandex.com/?source_lang={source}&target_lang={dest}")
            wait = WebDriverWait(self.driver, 50)

            contenteditable_element = wait.until(EC.presence_of_element_located((By.ID, "fakeArea")))

            script = f"arguments[0].textContent = '{text_to_enter}';"
            self.driver.execute_script(script, contenteditable_element)

            trigger_event_script = """
                var event = new Event('input', { bubbles: true });
                arguments[0].dispatchEvent(event);
            """
            self.driver.execute_script(trigger_event_script, contenteditable_element)

            translated_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".nI3G8IFy_0MnBmqtxi8Z[contenteditable='true']"))
            )
            wait.until(lambda driver: translated_element.text.strip() != "")

            translated_text = translated_element.text.strip()
            print(Fore.GREEN + Style.BRIGHT + f"[200] Translated Text: {translated_text} | Source: {source} | Dest: {dest}")
            return translated_text

        except Exception as e:
            print(Fore.RED + f"[403] An error occurred while translating: {text_to_enter} | Source: {source} | Dest: {dest}")
            # print(Fore.RED + Style.BRIGHT + traceback.format_exc())
            return None