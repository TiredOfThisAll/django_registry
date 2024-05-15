from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import os

from urllib3 import disable_warnings

disable_warnings()

requests.packages.urllib3.disable_warnings() 

def get_download_links(url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Загрузить')]")

    download_links = []
    for button in buttons:
        parent_anchor = button.find_element(By.XPATH, "./..")

        link = parent_anchor.get_attribute('href')
        if link:
            download_links.append(link)

    driver.quit()

    return download_links


def download_file(url, filename):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        with open("downloads/" + str(filename) + ".csv", 'wb') as f:
            f.write(response.content)
    else:
        print(f"Ошибка загрузки файла: {url}")


if not os.path.exists("downloads"):
    os.makedirs("downloads")
