import logging
import time
from pocketflow import Node
from .selenium_utils import get_driver
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

class CustomInputter(Node):
    """A Node that inputs data into a website."""
    def __init__(self, name: str, url: str, input_data: dict):
        super().__init__()
        self.name = name
        self.url = url
        self.input_data = input_data

    def prep(self, shared: dict) -> dict:
        return shared

    def exec(self, shared: dict) -> None:
        logger.info(f"[{self.name}] Inputting data to {self.url}: {self.input_data}")
        driver = get_driver(headless=True) 
        try:
            driver.get(self.url)
            # Simple heuristic: try to find inputs by name matching the keys
            for key, value in self.input_data.items():
                try:
                    element = driver.find_element(By.NAME, key)
                    element.send_keys(value)
                    logger.info(f"[{self.name}] Filled {key} with {value}")
                except Exception:
                    logger.warning(f"[{self.name}] Could not find input with name '{key}'")
            
            # Mock submission or further interaction
            time.sleep(1) 
            
        except Exception as e:
            logger.error(f"[{self.name}] Error inputting: {e}")
            raise
        finally:
            driver.quit()
