"""
Check websites for flight tickets

airlines:
    spirit
    american airlines
    southwest
    delta
    united airlines
    frontier
    jetblue

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
        driver.get("https://www.facebook.com/")
        driver.implicitly_wait(15)

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
