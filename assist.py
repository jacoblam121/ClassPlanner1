import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
# from PIL import Image
# import io
# import requests
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import ElementClickInterceptedException

#price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# search_bar = driver.find_element(By.NAME, value="Institution")
# print(search_bar.tag_name)

def assist_render():
    assist_url = "https://assist.org/"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(assist_url.format(q='test'))