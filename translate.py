import time
import traceback
from colorama import Fore, Style
from .webdriver import driver_return 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def translate_string(text_to_enter, dest, source="en",):
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
        driver.get(f"https://translate.yandex.com/?source_lang={source}&target_lang={dest}")
        wait = WebDriverWait(driver, 50)

        # Locate the contenteditable element for text input
        contenteditable_element = wait.until(EC.presence_of_element_located((By.ID, "fakeArea")))

        # Set the input text using JavaScript
        script = f"arguments[0].textContent = '{text_to_enter}';"
        driver.execute_script(script, contenteditable_element)

        # Trigger the input event to ensure text is processed
        trigger_event_script = """
            var event = new Event('input', { bubbles: true });
            arguments[0].dispatchEvent(event);
        """
        driver.execute_script(trigger_event_script, contenteditable_element)

        # Wait for the translated text to appear
        translated_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".nI3G8IFy_0MnBmqtxi8Z[contenteditable='true']"))
        )
        wait.until(lambda driver: translated_element.text.strip() != "")

        # Retrieve and return the translated text
        translated_text = translated_element.text.strip()
        print(Fore.GREEN + Style.BRIGHT + f"[200] Translated Text: {translated_text} | Source: {source} | Dest: {dest}")
        return translated_text

    except Exception as e:
        # Print error details with a traceback
        print(Fore.RED + f"[403] An error occurred while translating: {text_to_enter} | Source: {source} | Dest: {dest}")
        # print(Fore.RED + Style.BRIGHT + traceback.format_exc())
        return None
    
if __name__ == "__main__":
    driver = driver_return()
    for text in [
            "In the heart of the city, a quiet revolution is unfolding. It’s not happening in the bustling streets or the crowded squares, but in the minds of the people. These are individuals who, after years of feeling disconnected from the world, are now finding their voices. They are using the tools of technology, the vast reach of the internet, and the power of social media to connect, collaborate, and create",
            "How are you?",
            "What is your name?",
            "I love programming",
            "Can you help me?",
            "Where is the nearest station?",
            "Thank you for your help",
            "I am learning German",
            "This is a beautiful day",
            "See you tomorrow"
        ]:
        translated_text = translate_string(text, dest='zh', source="en")
    driver.quit()