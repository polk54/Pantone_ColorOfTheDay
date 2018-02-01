# The purpose of this file is to scrape Pantone's Color of the Day website and create an archive of all the colors they've picked.
# https://www.pantone.com/colorstrology

from bs4 import BeautifulSoup
import requests

# Getting the url
url = requests.get("https://www.pantone.com/colorstrology")
url

# Getting the html of the website
soup = BeautifulSoup(url.content, "html.parser")
print(soup.prettify())

# From inspecting the website, I will need:
# <div class="swatch inner" title="Pantone 15-1607 Pale Mauve">
# <div class="coloredSquare" style="background-color: #C5A4A4;">
# <span class="keyLogon"> HARDWORKING </span>
# <span class="keyLogon"> CARING </span>
# <span class="keyLogon"> PREPARED </span>

# Getting html in the div element
div = soup.find(id="outerWrap")
print(div.prettify())

# Drilling down further
div2 = div.find(id="ctl00_divBody")
print(div2.prettify())

# Finding specific div for color - doesn't have the 3 words
Color = div.find(class_="swatch inner")
print(Color.prettify())

# Print the entire color name from the HTML
ColorName = Color["title"]
print (ColorName)

# Separate PantoneID
PantoneID = ColorName[8:15]
print(PantoneID)

# Separate Pantone Color Name
PantoneName = ColorName[16:]
print(PantoneName)

# Separate background color
ID = div.find(class_="coloredSquare")
ColorID = ID["style"]
print (ColorID)

# Separate hex code
Hex = ColorID[18:25]
print (Hex)

# Getting the 3 words
Text = div2.find("span",{"class":"keyLogon"})
print(Text.get_text())

# Above only prints 1 word, need to figure out how to get the next two words.

for wrapper in div2.find_all("span",{"class":"keyLogon"}):
    print(wrapper.text)

# Put the three words into a list
text = []
for wrapper in div2.find_all("span",{"class":"keyLogon"}):
    wrapper = wrapper.get_text()
    text.append(wrapper)
print(text)

# Gets rid of the trailing spaces
text = [x.strip(' ') for x in text]
print(text)

# Separate list into 3 string variables and makes them all lowercase
Word1 = text[0]
Word1 = str.lower(Word1)
Word2 = text[1]
Word2 = str.lower(Word2)
Word3 = text[2]
Word3 = str.lower(Word3)

import datetime
from datetime import date
today = date.today()
print (today)

# Appends all the scraped items into a .csv
# today, PantoneName, PantoneID, Hex, Word1, Word2, Word3
import csv

destname = 'ColorOfTheDay.csv'
# This section is only to add the header to the .csv
# destfile = open(destname, 'w')
# mywriter = csv.writer(destfile)
# mywriter.writerow(["Date", "PantoneName", "PantoneID", "Hex#", "Word1", "Word2", "Word3"])
# destfile.close()

destfile = open(destname, 'a')
mywriter = csv.writer(destfile)
mywriter.writerow([today, PantoneName, PantoneID, Hex, Word1, Word2, Word3])

destfile.close()
