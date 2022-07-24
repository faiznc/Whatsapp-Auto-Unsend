from library import *
from Whatsapp import Whatsapp

if __name__ == "__main__":
    # Initiate Driver
    driver = get_driver()
    browser = Whatsapp(driver)

    browser.goto_whatsapp() # Go to Whatsapp main page

    # Step 1 - SETUP THE WHATSAPP
    # Login to Whatsapp and check whether the user is logged in or not.

    if not browser.is_logged_in():
        # If not logged in yet, ask user to scan QR Code
        print("Please scan QR code to login...")
        input("Click enter if you finished.")

    else:
        # Do actual thing.
        print("Doing actions...")

    browser.close_browser()
