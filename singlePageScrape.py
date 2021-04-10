import random
import time
from selenium import webdriver


def shortWait():
    time.sleep(random.uniform(1.0, 3.0))

def longWait():
    time.sleep(random.uniform(2.0, 5.0))
#TODO: Randomize which button is clicked in the initial pop-up

op = webdriver.ChromeOptions()
#op.add_argument('headless')
driver = webdriver.Chrome("/usr/lib/chromium/chromedriver",options=op)
driver.get("https://www.edc.dk/sog/?side=2#lstsort")

#confirm pop-up screen

#TODO: wait till element is visible 
longWait()

driver.find_element_by_class_name('coi-banner__accept').click()

shortWait()

#scrape single page





#driver.quit()