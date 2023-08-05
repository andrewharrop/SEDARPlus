from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from selenium import webdriver

BASE_URL = "https://www.sedarplus.ca/csa-party/viewInstance/view.html?id=0c11f8b7998bcd96fa6e9bdf94d90ba692b7a86cae7d5604&_timestamp=4937175359398006"

files = os.listdir("./")
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
start_time = time.time()
driver.get(BASE_URL)


button = driver.find_element("xpath", "//button[contains(@aria-label, 'Export')]")
button.click()

# Waiting for the file to be downloaded
while len(os.listdir("./")) == len(files):
    time.sleep(1)

print("Downloaded in %s seconds" % (time.time() - start_time))
downloaded_file = list(set(os.listdir("./")) - set(files))[0]
os.rename(downloaded_file, "SEDARreportingIssuerImport.csv")

# We want to remove the first six lines of the file
with open("SEDARreportingIssuerImport.csv", "r") as f:
    lines = f.readlines()
    lines = lines[5:]
    with open("SEDARreportingIssuerImport.csv", "w") as f:
        f.writelines(lines)



driver.close()


