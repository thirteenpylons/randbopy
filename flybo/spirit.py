"""
This will be the module to check spirit.com flights


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
        driver.get("https://www.spirit.com/")
        driver.implicitly_wait(15)

        # Cookie hack
        cook_button = driver.find_element(
            By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]'
        )
        cook_button.click()
        # BOOK BUTTON
        bookit = driver.find_element(
            By.XPATH,
            value="/html/body/app-root/app-common-header/header/div[2]/div/div[1]/ul/li[1]/a",
        )
        # Where are you departing from?
        depart_in = driver.find_element(
            By.XPATH, value='//*[@id="flight-OriginStationCode"]'
        )
        depart_in.click()
        depart_in.send_keys("")  # Where you need to go
        # Where do you want to go?
        arrive_in = driver.find_element(
            By.XPATH, value='//*[@id="flight-DestinationStationCode"]'
        )
        arrive_in.click()
        arrive_in.send_keys("")  # Destination
        # round trip or one way?
        ask_trip = input("Is this a one way trip or round trip?: ")
        if "one" in ask_trip:
            one_radio = driver.find_element(By.XPATH, value='//*[@id="one-way"]')
        # What date?

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
