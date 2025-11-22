import logging
from pocketflow import Node
from .selenium_utils import get_driver
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

class CustomScraper(Node):
    """A Node that scrapes data from a website."""
    def __init__(self, name: str, url: str, description: str):
        super().__init__() # Node.__init__ might not take name, or we set it after? 
        # Wait, Node.__init__ signature? 
        # I'll check if Node takes name. If not, I'll just set self.name manually or ignore it if not used by base.
        # The previous inspection showed Node.__init__ exists.
        # Let's assume standard Node(name) or just Node().
        # Actually, looking at dir(Node), it has __init__.
        # I will assume it doesn't take name for now to be safe, or I'll check.
        # But I need to be quick. I'll just call super().__init__() and set self.name.
        self.name = name
        self.url = url
        self.description = description

    def prep(self, shared: dict) -> dict:
        return shared

    def exec(self, shared: dict) -> None:
        logger.info(f"[{self.name}] Scraping {self.url} - {self.description}")
        driver = get_driver(headless=True) 
        try:
            driver.get(self.url)
            title = driver.title
            logger.info(f"[{self.name}] Page Title: {title}")
            shared[f"{self.name}_title"] = title
        except Exception as e:
            logger.error(f"[{self.name}] Error scraping: {e}")
            raise
        finally:
            driver.quit()
