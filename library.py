import os
from config import *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

CURRENT_DIR = os.getcwd()
CHROME_DATA_DIR = CURRENT_DIR + "\\ChromeData"


def modify_start_chrome_bat_file(chrome_dir: str, user_dir: str):
    # TODO Develop this function.
    pass


def start_chrome():
    """Starting the chrome browser via .bat file"""
    print("Opening Browser...")
    os.system(CURRENT_DIR + "\\StartChrome.bat")


def get_driver() -> webdriver:
    """Get usable driver"""
    start_chrome()  # Start chrome browser
    # Setup injections
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=" + CHROME_DATA_DIR)  # Set user data dir
    options.add_experimental_option("debuggerAddress", "localhost:" + str(REMOTE_PORT))    # Set port to control
    # Finally return created driver
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


if __name__ == "__main__":
    print("This is only support file. Please run main.py instead.")
    pass
