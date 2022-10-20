import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


count=0
liness = []
with open("advertisers.csv") as f:
    lines = f.readlines()

for line in lines:
    liness.append(line.replace("\n", "").replace(".ro", ""))

COMPARI =  "- informații"

chrome_driver_path = "/Users/robertmuresan/PycharmProjects/chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

URL = "https://www.google.com/"

driver.get(URL)

accept = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
time.sleep(random.randint(1,5))
accept.click()


for line in liness:
    if count == 13 or count== 18:
        time.sleep(33)

    time.sleep(random.randint(1,8))
    driver.get(URL)
    searchbox = driver.find_element(By.CLASS_NAME, "gLFyf")
    time.sleep(random.randint(1,5))
    searchbox.send_keys(f"{line} compari.ro")
    time.sleep(random.randint(1,5))
    searchbox.send_keys(Keys.ENTER)

    titles = driver.find_elements(By.TAG_NAME,"h3")
    count+= 1



    for title in titles:
        print(title.text)
        term1 = f"informatii, preturi, comparatii"
        term2 = f"{line}.ro"
        term3 = line.upper()
        # print(term)
        if (term1 in title.text.lower() and line in title.text.lower()) or (term2 in title.text.lower() and term1 in title.text.lower()) or (term3 in title.text.lower() and term1 in title.text.lower()) or (line.title() in title.text.lower() and term1 in title.text.lower()):
            value = "true"
        else:
            value="false"
        with open("output.txt", "a") as file:
            file.write(f"{line}, {value}\n")

driver.quit()