# OnTheMarket UK properties using Python Scraper framework
- Extract title, address, description, price, image URL, contact details (email / phone number)
- Filter through the properties on onthemarket & sort by sq m / sq ft (in text full description or use Optical Character Recognition in floorpan), years remaining on the lease.
- Don't show: shared ownership, auction, retirement homes

## Prerequisites
1. Install Python, check python --version
2. Install Pip (package manager for Python), check pip --version
3. Setup virtual environment to add project specific third-party modules: vnv comes with Python 3.3, otherwise you need to install manually. 
4. Install Scrapy
5. Install IDE 

### Visual Studio Code venv setup
1. pip install virtualenv
2. cd folderPath
3. python3 -m venv venvprojectfolder
4. activate virtual environment so that any third-party package installed after this will also be installed into project_env folder: source venvprojectfolder/bin/activate
5. pip install Scrapy

### Scrapy project setup
1. open project folder in terminal
2. scrapy startproject projectName: generate basic project which contains an essential _spiders_ folder & optional items.py, middlewares.py, pipelines.py, settings.py. if scraping anything > 1 page it becomes a lot easier to use middlewares.py & pipelines.py instead of having everything custom-made in spider

## Define Spider class
websites to scrape: 
- https://www.onthemarket.com/for-sale/property/goodge-street-station/
- https://www.onthemarket.com/for-sale/flats-apartments/goodge-street-station/?auction=false&max-bedrooms=3&max-price=500000&min-bedrooms=2&min-price=250000&retirement=false&shared-ownership=false&travel-duration=60&travel-type=public-transport

1. in spiders folder: run scrapy genspider spidername scraperwebsiteurl
2. 

## Crawling logic
Crawl all the pages using your browser as the user agent (Developer Tools > Network): Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36

## Making Custom Requests
Create a start_requests(self) function

## Debugging

## Adding selectors

## Importing selectors

## Data extraction

## Title

## Price

## Agency

## Phone number

## Image URLs

## Pages

## Storage Requests

# Resources
- https://www.youtube.com/watch?v=mBoX_JCKZTE
