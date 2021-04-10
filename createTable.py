import urllib.request
import xlsxwriter
from io import BytesIO

from singlePageScrape import fillContainer
from singlePageScrape import shortWait

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

#fill in the desired number of pages to be scraped
#when empty, it will scrape all the pages
#TODO: take argument from command-line
requestedData = fillContainer(3)

row=1
#creation of new xlsx file
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()

#preparation of xlx file
worksheet.set_column('A:Z', 45)
worksheet.write(0, 1, 'Name')
worksheet.write(0, 2, 'Ground')
worksheet.write(0, 3, 'M2')
worksheet.write(0, 4, 'Rooms')
worksheet.write(0, 5, 'Year of construction')
worksheet.write(0, 6, 'Length of stay')
worksheet.write(0, 7, '+/-')
worksheet.write(0, 8, 'Rent/Consumption')
worksheet.write(0, 9, 'Price/m2')
worksheet.write(0, 10, 'Ownership Cost/Month')

for item in requestedData:
    imageUrl = getattr(item, 'imageUrl')
    postLink = getattr(item, 'link')
    
    #getting image data from image url
    image_data = BytesIO(urlopen(imageUrl).read())

    worksheet.set_row(row, 95)
    #inserts
    worksheet.insert_image(row, 0, postLink, {'image_data': image_data, 'url': postLink})
    worksheet.write(row, 1,  getattr(item, 'name'))
    worksheet.write(row, 2,  getattr(item, 'ground'))
    worksheet.write(row, 3,  getattr(item, 'm2'))
    worksheet.write(row, 4,  getattr(item, 'rooms'))
    worksheet.write(row, 5,  getattr(item, 'yearOfConstruction'))
    worksheet.write(row, 6,  getattr(item, 'lengthOfStay'))
    worksheet.write(row, 7,  getattr(item, 'plusMinus'))
    worksheet.write(row, 8,  getattr(item, 'rentAndConsumption'))
    worksheet.write(row, 9,  getattr(item, 'pricePerM2'))
    worksheet.write(row, 10,  getattr(item, 'ownershipCostPerMonth'))
    row+=1

workbook.close()

