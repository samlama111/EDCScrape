# EDCScrape
Scrape of EDC

Run the createTable.py script to generate a .xlsx file containing scraped data from edc.dk.
The result will be stored in 'result.xlsx' Excel file.
For an already existing result, check the 'result.xlsx'.

In order to run the code, you need to download a Chromedriver (of the same version as your Chrome/Chromium browser) and specify the path to it. 
Python dependencies that might need to be installed (e.g. through pip) are Selenium, BytesIO, urllib.request & xlsxwriter.
