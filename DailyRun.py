# encoding=utf8
## This file will run:
# 1. The pantone scraping function
# 2. The push to GitHub repository function

# Import files and functions
from DailyScraper_BS_update import colorScrape
from pushHTML import push

# Run the two functions
colorScrape()
push()
