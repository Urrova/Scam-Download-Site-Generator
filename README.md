# 載 DO YOU WANT FREE GAMES¿
**Scam Download Website Generator** is an application made in python that generates fake pirate download websites. 
This works getting a random videogame from a local database, then scraping wikipedia to get more information, and then building the site from an html template. The sites are static and monolithic, with styles and images embedded into the HTML.

![window image](https://github.com/Urrova/scam-download-site-generator/blob/master/docs/window.png)

![example site](https://github.com/Urrova/scam-download-site-generator/blob/master/docs/example_site.png)

# How to use (app)
- Select the EXTREMITY level; this controls how crazy the builder gets.
- Click on "Build Site" and wait 3 hours.
- Click on open site and see your own pirate websiting magnum opus.

# How to build
Install python and pyinstaller; 

**Using make:** 

use `make setup` to install the required dependencies, then use `make windows` to build the executable.

**Without using make:** 

Install the dependencies:

`pip install requests`

`pip install beautifulsoup4`

Then on the root of the project use pyinstaller:

`pyinstaller --onefile  --name ScamDownloadSiteGenerator __main__.py`
