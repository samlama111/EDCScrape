import random
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.edc.dk/sog/"
op = webdriver.ChromeOptions()
#op.add_argument('headless')
driver = webdriver.Chrome("/usr/lib/chromium/chromedriver",options=op)

def shortWait():
    time.sleep(random.uniform(1.0, 3.0))
def longWait():
    time.sleep(random.uniform(2.0, 5.0))
def waitTillWebsiteLoads():
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.Class, 'coi-banner__accept')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
def scrollDown():
    shortWait()
    #randomLength = str(random.uniform(20.0,80.0))
    #driver.execute_script("window.scrollBy(0,"+randomLength+")")

    #driver.execute_script("arguments[0].scrollIntoView(true)", nextPageElement)
    shortWait()

#TODO: Randomize which button is clicked in the initial pop-up



driver.get(url)

#confirm pop-up screen

#TODO: wait till element is visible 
longWait()

driver.find_element_by_class_name('coi-banner__accept').click()

shortWait()

#scrape single page


nextPageElement = driver.find_element_by_xpath('//ul[contains(@class,\'pagination\')]//li//a')
shortWait()



allListings = driver.find_elements_by_xpath('//div[contains(@class,\'maincontent \')]//div[contains(@class,\'propertyitem propertyitem--list\')]')

longWait()

for listing in allListings:
    name = listing.find_element_by_class_name('propertyitem__address--listview').text
    shortWait()

    price = listing.find_element_by_class_name('propertyitem__price').text
    price = price.split('\n',2)[-1]
    shortWait()

    #depends on which listing 
    typeOfListing = len(listing.find_elements_by_css_selector('th'))
    if(typeOfListing == 1):
        ground = listing.find_element_by_css_selector('td').text
        
    elif(typeOfListing == 2):
        info = listing.find_elements_by_css_selector('td') 
        shortWait()
        m2 = info[0].text
        rooms = info[1].text
        
    elif(typeOfListing == 7):
        info = listing.find_elements_by_css_selector('td')
        shortWait() 
        m2 = info[0].text
        ground = info[1].text
        rooms = info[2].text
        yearOfConstruction = info[3].text
        lengthOfStay = info[4].text
        plusMinus = info[5].text
        RentAndConsumption = info[6].text
        print(m2, ground, rooms, yearOfConstruction, lengthOfStay, plusMinus, RentAndConsumption)
    elif(typeOfListing == 8):
        info = listing.find_elements_by_css_selector('td')
        shortWait() 
        m2 = info[0].text
        ground = info[1].text
        rooms = info[2].text
        yearOfConstruction = info[3].text
        lengthOfStay = info[4].text
        plusMinus = info[5].text
        #extra one
        pricePerMm2 = info[6].text
        ownershipCostPerMonth = info[7].text
        print(m2, ground, rooms, yearOfConstruction, lengthOfStay, plusMinus, pricePerMm2, ownershipCostPerMonth)
    else:
        print("error")


    shortWait()
    




#[elem.find_element_by_class_name('auction-url').get_attribute('href') for elem in itemDivs]




#driver.quit()