from selenium import webdriver
from selenium.webdriver.common.by import By


class Whatsapp:
    def __init__(self, driver: webdriver):
        self.driver: webdriver.Chrome = driver
        self.default_implicit_wait = 5  # Default implicit wait = 5 sec
        self.driver.implicitly_wait(self.default_implicit_wait)

    def goto_whatsapp(self) -> None:
        self.driver.get("https://web.whatsapp.com")

    def is_logged_in(self) -> bool:
        """Check whether the Get Started help is shown or not."""
        link = self.driver.find_elements(By.CSS_SELECTOR, "div.landing-window > div.landing-main")
        return False if link else True

    def set_implicit_wait(self, seconds: int) -> None:
        """Set implicit wait time."""
        self.driver.implicitly_wait(seconds)

    def reset_implicit_wait(self) -> None:
        """Reset implicit wait time to default."""
        self.driver.implicitly_wait(self.default_implicit_wait)

    def close_browser(self) -> None:
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    print("This is only support file. Please run main.py instead.")
