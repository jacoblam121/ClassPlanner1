###

import urllib.request
import tabula
import tabulate
import pandas
import string

test_url = "https://admission.universityofcalifornia.edu/admission-requirements/transfer-requirements/preparing-to-transfer/general-education-igetc/igetc/"
igetc_url = "https://pasadena.edu/academics/degrees-and-certificates/docs/IGETC-Fall-2023-and-Later.pdf"

response = urllib.request.urlopen(test_url).read()

print(response)

igetc_data = tabula.read_pdf(igetc_url, pages=1)
igetc_data_clean = igetc_data[0].to_csv()
for i in range(0, len(igetc_data_clean)):
    if i == "◊": #u25ca is diamond
        igetc_data_clean[i] = "^"

print(igetc_data_clean)

# with open("test.csv", "w") as file:
#     file.write(igetc_data[0].to_csv())

#print(tabulate(igetc_data[0], headers='keys', tablefmt='psql'))
