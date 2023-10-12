###

import urllib.request
import tabula
import tabulate
import pandas
import string
import requests
import selenium
from selenium import webdriver
from assist import assist_render
from assist import test
from assist import assist_to_txt
from assist import get_major
from assist import tunnel

assist_url = "https://assist.org/"
uci_url = "https://assist.org/transfer/results?year=73&institution=49&agreement=120&agreementType=to&view=agreement"
igetc_url = "https://pasadena.edu/academics/degrees-and-certificates/docs/IGETC-Fall-2023-and-Later.pdf"



def igetc_to_csv():
    igetc_data = tabula.read_pdf(igetc_url, pages=1)
    igetc_data[0].to_csv("test.csv", index=False)

# test()
#get_major()
tunnel()
