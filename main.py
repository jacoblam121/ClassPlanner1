###

import urllib.request
import tabula
import tabulate
import pandas
import string

test_url = "https://admission.universityofcalifornia.edu/admission-requirements/transfer-requirements/preparing-to-transfer/general-education-igetc/igetc/"
igetc_url = "https://pasadena.edu/academics/degrees-and-certificates/docs/IGETC-Fall-2023-and-Later.pdf"


def assist_to_txt():
    response = urllib.request.urlopen(assist_url).read()
    response = str(response)
    print(type(response))
    with open("assist.txt", "w") as file:
        file.write(response)

def igetc_to_csv():
    igetc_data = tabula.read_pdf(igetc_url, pages=1)
    igetc_data[0].to_csv("test.csv", index=False)

#assist_render()
