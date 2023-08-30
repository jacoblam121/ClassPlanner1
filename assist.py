import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException


def assist_render():
    assist_url = "https://assist.org/"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(assist_url.format(q='test'))