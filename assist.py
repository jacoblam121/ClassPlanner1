# import os
# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import tabula
import tabulate
import pandas
import string
# import time
# from PIL import Image
# import io
# import requests
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import ElementClickInterceptedException

#price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# search_bar = driver.find_element(By.NAME, value="Institution")
# print(search_bar.tag_name)

def test():
    return 0



def assist_to_txt(current_assist_url):

    response = urllib.request.urlopen(current_assist_url).read()
    print(type(response))
    assist_data = tabula.read_pdf(current_assist_url, pages=1)
    #assist_data[0].to_csv("test.csv", index=False)


# def assist_to_txt(current_assist_url):
#     response = urllib.request.urlopen(current_assist_url).read()
#     response = str(response)
#     print(type(response))
#     with open("assist.txt", "w") as file:
#         file.write(response)


def assist_driver_close(driver = webdriver):
    driver.close()

def assist_driver_quit(driver = webdriver):
    driver.quit()


def assist_render():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    url_open = "https://assist.org/?year=73&institution=49&agreement=0&agreementType=to&view=agreement&viewBy=major"
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url_open)
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(2)

    # search_bar = driver.find_element(By.NAME, value="q")
    # print(search_bar.tag_name)

    assist_search_bar = driver.find_element(By.XPATH, value='//*[@id="agreement"]')
    assist_search_bar.send_keys("University of California, Irvine")
    assist_search_bar.send_keys(Keys.ENTER)

    view_agreements = driver.find_element(By.XPATH, value='//*[@id="transfer-agreement-search"]/div[4]/button')
    view_agreements.click()

    driver.implicitly_wait(2)

    college_window = driver.current_window_handle

    major_search_bar = driver.find_element(By.XPATH, value='/html/body/app-root/div[2]/app-transfer/section[1]/app-report-items/section/div[1]/div[3]/input')
    major_search_bar.send_keys("Computer Science")

    major_click = driver.find_element(By.XPATH, value='//*[@id="autocomplete-options--destination"]/div[2]/a/div[4]')
    major_click.click()

    pdf_click = driver.find_element(By.XPATH, value='//*[@id="view-results"]/app-report-download/div/div[2]/div[4]/a')
    pdf_click.click()

    wait.until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != college_window:
            driver.switch_to.window(window_handle)
            break

    current_assist_url = driver.current_url
    print(current_assist_url)
    assist_to_txt(current_assist_url)
    #driver.quit()