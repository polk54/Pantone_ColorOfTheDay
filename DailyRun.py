## This file will run:
# 1. The pantone scraping function
# 2. The push to GitHub repository function

# Import files and functions
from DailyScraper_BS_update import colorScrape
from pushHTML import push

# set parameters
site = "https://www.pantone.com/colorstrology"
repo_dir = "Pantone_ColorOfTheDay"

# Run the two functions
colorScrape(site)
push(repo_dir)
