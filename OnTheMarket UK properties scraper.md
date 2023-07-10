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
2. it will auto-generate a name so that you can do Scrapy crawl to kick the spider off with that name; allowed_domains is important for crawling as it lists only the domain you want the spider to scrape & preventing the spider from scraping the entire internet; start_urls is the first URL that the spider starts scraping.
3. it will auto-generate a parse function that gets called once the response comes back: fill it with all the pieces you want to extract the data from the page.
4. Use the Scrapy shell to find the CSS selectors you want to get the data from the page: open developer tools via Inspect > elements to see all the HTML & CSS that make up the page. Pick out the tags so Scrapy knows which pieces of data to extract.
5. pip install ipython: load a different shell in terminal to make it easier to read. Go to scrapy.cfg & add "shell = ipython" as a separate line under [settings]
6. run scrapy shell to see a list of the available commmands: fetch('url'), response.css('csstag.classname')
7. run response.status to check if the status is ok (should be 200), if getting [403](https://doc.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned) this could be anti-scraping measure implemented by the site

## Fake User-Agents & Browser headers
1. Developer tools > Network > Doc: check Preview & Response, this is what you end up scraping when using Scrapy.
2. Check Headers > General to see everything that's sent when you request this page: request url, request method, status code 
3. IMPORTANT: Request headers is everything you send when you make a request to the url, user-agent gives all the important info about who you are to the server that you're requesting the web page from. Paste the user-agent string into [useragentstring.com](https://useragentstring.com/) for data analysis. This is fine when browing the web but if you're doing any large-scale scraping on commercial sites you're likely to get blocked by anti-bots. 

### Why we get blocked when web scraping
- Commercial sites want to protect their data & only make it available to customers: check terms & conditions for legal purposes of scraping
- Generally if it's publicly available & you don't have to log in then it's usually ok to scrape the data
- Anti-bots look at the IP address of your machine in order to block requests: they might set something in your cookies in your session so they know it's you coming back every time
- Difference between headers & user agents: headers is everything under Network > Developer Tools > Doc > Headers, it encompasses accepted responses that are returned, accept-language, accept-encoding; user-agent is just a subset of the overall request
- For some sites that are not too complex: if you change the user-agent each time you make a request the website will think it's a different browser & a different computer looking for the data every time so it'll let the request go through.
- For complicated sites: they'll look at everything in the request headers, they'll want everything to be different. They might throw a captcha page & if that captcha is not solved then the requests are blocked. You need to change the entirety of the request headers rather than just the user-agent

### Using user agents to bypass getting blocked
### using request headers to bypass getting blocked

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
