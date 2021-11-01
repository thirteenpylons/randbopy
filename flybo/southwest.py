"""
This will be the module to check southwest.com flights


Author: Christian M. Fulton
Date: 31.Oct.2021
"""
import datetime, os
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import creds as CREDS


def execute():
    """
    Executes the application
    """
    try:
        #### This code can be modularized ####
        driver = webdriver.Chrome(
            executable_path="/usr/lib/chromium-browser/chromedriver"
        )
        driver.get("https://www.southwest.com/")
        driver.implicitly_wait(15)

        # Where are you departing from?
        depart_in = driver.find_element(
            By.XPATH,
            value='//*[@id="LandingAirBookingSearchForm_originationAirportCode"]',
        )
        depart_in.click()
        depart_in.send_keys("")  # Where you need to go
        depart_in.send_keys("\ue007")
        # Where do you want to go?
        arrive_in = driver.find_element(
            By.XPATH,
            value='//*[@id="LandingAirBookingSearchForm_destinationAirportCode"]',
        )
        arrive_in.click()
        arrive_in.send_keys("")  # Destination
        arrive_in.send_keys("\ue007")
        # round trip or one way?
        trip_in = input("Is this a one way trip or round trip?: ")
        if "one" in trip_in:
            one_radio = driver.find_element(
                By.XPATH,
                value='//*[@id="TabbedArea_4-panel-0"]/div/div/div/form/div[1]/div[1]/fieldset/ul/li[2]/label/input',
            )
            from_in = input("What is the departure date?: YYYY MM DD ")
        else:
            # ask return date
            return_in = input("What would be the return date?: YYYY MM DD ")

        depart_calendar = driver.find_element(
            By.XPATH,
            value='//*[@id="TabbedArea_4-panel-0"]/div/div/div/form/div[2]/div[2]/div[1]/label/div[1]/div/div/div/span/span',
        )
        enter_date = driver.find_element(
            By.PATH, value=f'//*[@id="calendar-138-{2021-12-14}"]'
        )
        email_in = driver.find_element(By.XPATH, value='//*[@id="email"]')
        email_in.send_keys(CREDS.ETSY_UNAME)
        pwd_in = driver.find_element(By.XPATH, value='//*[@id="pass"]')
        pwd_in.send_keys(CREDS.ETSY_PWD + "\ue007")

        orders_btn = driver.find_element(
            By.XPATH,
            value='//*[@id="root"]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li[5]/a',
        )
        orders_btn.click()

        order_qty = driver.find_element(
            By.XPATH,
            value='//*[@id="browse-view"]/div/div[1]/div[2]/nav/ul/li[1]/a/span[2]',
        ).text

        # check for any new orders
        if int(order_qty) > 0:
            pickup()
    except:
        print("Something went wrong...")
        driver.quit()

    driver.quit()
