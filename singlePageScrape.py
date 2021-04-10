import random
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from listing import Listing
from listingContainer import ListingContainer

url = "https://www.edc.dk/sog/"
op = webdriver.ChromeOptions()
#uncomment if you want the code to run without seeing the browser
#op.add_argument('headless')

#specify path to chromedriver
driver = webdriver.Chrome("/usr/lib/chromium/chromedriver",options=op)

containerObject = ListingContainer()
container = getattr(containerObject, 'allListings')

def shortWait():
    time.sleep(random.uniform(1.0, 3.0))
def longWait():
    time.sleep(random.uniform(2.0, 5.0))
def scrollDown():
    shortWait()
    #TODO: make more precise
    randomLength = str(random.uniform(230.0,240.0))
    driver.execute_script("window.scrollBy(0,"+randomLength+")")
    shortWait()
def getNumberOfCurrentPage():
    currentPage = driver.find_element_by_class_name('pagination__text').text[5:6]
    shortWait()
    return currentPage
def confirmInitialPopUpWindow():
    #TODO: wait till element is visible 
    longWait()

    #TODO: Randomize which button is clicked in the initial pop-up
    driver.find_element_by_class_name('coi-banner__accept').click()

    shortWait()
def scrapeSinglePage():
    shortWait()

    allListings = driver.find_elements_by_xpath('//div[contains(@class,\'maincontent \')]//div[contains(@class,\'propertyitem propertyitem--list\')]')

    longWait()

    for currentListing in allListings:
        #need to scroll down with each listing because of the lazy loading of images
        scrollDown()
        imageUrl = currentListing.find_element_by_css_selector('img').get_attribute('src')
        shortWait()

        name = currentListing.find_element_by_class_name('propertyitem__address--listview').text
        shortWait()

        link = currentListing.find_element_by_class_name('propertyitem__link').get_attribute('href') 
        shortWait()

        price = currentListing.find_element_by_class_name('propertyitem__price').text
        shortWait()
        price = price.split('\n',2)[-1]

        #determine type of listing  
        numberOfAttributes = len(currentListing.find_elements_by_css_selector('th'))
        shortWait()
        info = currentListing.find_elements_by_css_selector('td')
        longWait()
        if(numberOfAttributes == 1):
            newListing = Listing(name=name, link=link, price=price, imageUrl=imageUrl, ground=info[0].text)
            #print(vars(newListing))
            container.append(newListing)
        else:
            if(numberOfAttributes == 2):
                newListing = Listing(name=name, link=link, price=price, imageUrl=imageUrl, m2=info[0].text, rooms=info[1].text)
                container.append(newListing)
            elif(numberOfAttributes == 7):
                newListing = Listing(name=name, link=link, price=price, imageUrl=imageUrl, m2=info[0].text, 
                ground=info[1].text,rooms=info[2].text, yearOfConstruction=info[3].text,
                lengthOfStay=info[4].text, plusMinus=info[5].text, rentAndConsumption=info[6].text)
                container.append(newListing)
            elif(numberOfAttributes == 8):
                newListing = Listing(name=name, link=link, price=price, imageUrl=imageUrl, m2=info[0].text, 
                ground=info[1].text,rooms=info[2].text, yearOfConstruction=info[3].text,
                lengthOfStay=info[4].text, plusMinus=info[5].text, pricePerM2=info[6].text,
                ownershipCostPerMonth=info[7].text)
                container.append(newListing)
            else:
                print("error")
        #uncomment to easily see how pagination works
        #break
        shortWait()
    #TODO: check if the button really exists
    nextPageElement = driver.find_element_by_xpath('//ul[contains(@class,\'pagination\')]//li//a[contains(text(),\'Næste\')]').click()
    shortWait()
def scrapeAmountOfPages(numberOfPages):
    currentPage = getNumberOfCurrentPage()
    while(int(currentPage)<=int(numberOfPages)):
        scrapeSinglePage()
        currentPage = getNumberOfCurrentPage()
        shortWait()
def fillContainer(numberOfPagesToBeScraped='not specified'):
    driver.get(url)

    confirmInitialPopUpWindow()

    if numberOfPagesToBeScraped=='not specified':
        maxPages = driver.find_element_by_class_name('pagination__text').text[-3:].strip()
        shortWait()
        scrapeAmountOfPages(int(maxPages))
    else:
        scrapeAmountOfPages(numberOfPagesToBeScraped)
    
    driver.quit()

    return container


