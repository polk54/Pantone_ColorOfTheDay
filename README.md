# Pantone Color Of The Day

** paused **

The purpose of this project is to create an archive of all of Pantone's "Color of the Day" colors
<br>Pantone site: https://www.pantone.com/color-intelligence/color-education/colorstrology <br>
My archive: https://polk54.github.io/Pantone_ColorOfTheDay/

FILES:
The *DailyScraper_BS_update.py* has a function that does the following:
  1. Scrapes the Color of the Day website to get the Color name, Pantone ID, Hex code, and 3 describing words.
  2. Appends this info to  Colors.csv
  3. Uses that info to write a new html div section and add it to index.html
     (This feature was added 2/4/18, so any html text previous to that date might be formatted a bit different)

The *pushHTML.py* has a function that does the following:
  1. Pushes the updated index.html and Colors.csv to this repository

The *DailyRun.py* file imports the previous 2 files/functions and runs them.

AUTOMATION:
Using Apple's Automator, I created a "Run Shell Script" bin/bash command (pass input: to stdin)
- cd /Users/parulagarwal/Documents/Code/GitHub/Pantone_ColorOfTheDay
- /Users/parulagarwal/anaconda3/bin/python DailyRun.py

The second line specifies the proper installation of Python. This is to make sure you can use all your installed packages (previously running into an issue with "bs4").
<br> <br>
Finally, I created an recurring Apple calendar event where the alert opened the Automator file.
