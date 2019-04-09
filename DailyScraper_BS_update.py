# encoding=utf8

# # Python Code for Creating Color Archive
#
# The purpose of this file is to scrape Pantone's Color of the Day website and create an archive of all the colors they've picked.
# https://www.pantone.com/colorstrology
#
# When run, this code will output three files:
#     1. Colors.csv
#     2. newcolor.html
#     3. index.html

#### DEFINE FUNCTION
def colorScrape(site):
    # ## Section 1
    # Getting COTD info from Pantone's Color of the Day website and putting it into a csv.

    from bs4 import BeautifulSoup, Tag, NavigableString
    import requests
    import os

    # Getting the url
    url = requests.get(site)
    url

    # Getting the html of the website
    soup = BeautifulSoup(url.content, "html.parser")
    #print(soup.prettify())

    # I need:
    # <div class="swatch inner" title="Pantone 15-1607 Pale Mauve">
    # <div class="coloredSquare" style="background-color: #C5A4A4;">
    # <span class="keyLogon"> HARDWORKING </span>
    # <span class="keyLogon"> CARING </span>
    # <span class="keyLogon"> PREPARED </span>

    # Getting html in the div element
    div = soup.find(id="outerWrap")

    # Drilling down further
    div2 = div.find(id="ctl00_divBody")

    # Finding specific div for color - doesn't have the 3 words
    Color = div.find(class_="swatch inner")
    #print(Color.prettify())

    # Print the entire color name from the HTML
    ColorName = Color["title"]
    #print(ColorName)

    # Separate PantoneID
    PantoneID = ColorName[8:15]
    #print(PantoneID)

    # Separate Pantone Color Name
    PantoneName = ColorName[16:]
    #print(PantoneName)

    # Separate background color
    ID = div.find(class_="coloredSquare")
    ColorID = ID["style"]
    #print(ColorID)

    # Separate hex code
    Hex = ColorID[18:25]
    #print(Hex)

    # Getting the 3 words
    Text = div2.find("span",{"class":"keyLogon"})
    #print(Text.get_text())

    # need to figure out how to get the next two words.

    #for wrapper in div2.find_all("span",{"class":"keyLogon"}):
        #print(wrapper.text)

    # Puts the three words into a list
    text = []
    for wrapper in div2.find_all("span",{"class":"keyLogon"}):
        wrapper = wrapper.get_text()
        text.append(wrapper)
    #print(text)

    # Gets rid of the trailing space
    text = [x.strip(' ') for x in text]
    #print(text)

    # Separate list into 3 string variables and makes them all lowercase
    Word1 = text[0]
    Word1 = str.lower(Word1)
    Word2 = text[1]
    Word2 = str.lower(Word2)
    Word3 = text[2]
    Word3 = str.lower(Word3)

    # Creating the date variable
    import datetime
    from datetime import date
    today = datetime.date.today()
    today = (today.strftime("%m/%d/%Y"))
    #print (today)

    # Appends all the scraped items into a .csv
    # The variables I need: today, PantoneName, PantoneID, Hex, Word1, Word2, Word3
    import csv

    destname = 'Colors.csv'
    #This section was only needed to add the header to the .csv
    #destfile = open(destname, 'w')
    #mywriter = csv.writer(destfile)
    #mywriter.writerow(["Date", "PantoneName", "PantoneID", "Hex#", "Word1", "Word2", "Word3"])
    #destfile.close()

    destfile = open(destname, 'a')
    mywriter = csv.writer(destfile)
    mywriter.writerow([today, PantoneName, PantoneID, Hex, Word1, Word2, Word3])

    destfile.close()


    # ## Section 2
    # Using the variable names, like "PantoneName", to create new "color-item" section in the html.

    # Creating the new color section
    NewColor = """
    <div class="color-item">
    <svg height="200" width="200">
       <rect fill=
        """

    NewColor2 = """
        height="200" width="200" x="0" y="0">
       </rect>
      </svg>
      <div class= "date">
       <p>
        """

    NewColor3 = """
       </p>
      </div>
      <div class="text">
       <p>
        """

    Break = """
        <br/>
        """
    End = """
        </p>
        </div>
    </div>
        """

    # Making the date into a string
    today_str = str(today)
    today_str

    # Adding the color variables to the HTML text from above
    NewColorHTML = [NewColor] + [Hex] + [NewColor2] + [today_str] + [NewColor3] + [PantoneName] + [Break] + [PantoneID] + [Break] + [Hex] + [End]

    # Making the list into a string
    NewColorHTML = "".join(NewColorHTML)
    NewColorHTML

    #Saving the string as new HTML file
    file = open("newcolor.html","w")
    file.write(NewColorHTML)
    file.close()


    # ## Section 3
    # Adding "newcolor.html" to "index.html" - for now "newindex.html" until it's perfect

    # Now I need to add this code to index.html
    # Right after <div class="colors">

    # Getting the URL for my COTD archive
    cotd_archive = requests.get("https://polk54.github.io/Pantone_ColorOfTheDay/")
    soup2 = BeautifulSoup(cotd_archive.content, "html.parser")

    # Saving the COTD archive as a new html file
    with open("cotd.html", "w") as file:
        file.write(str(soup2))
        file.close()

    # Opening the cotd and newcolor html files
    soup3 = BeautifulSoup(open("cotd.html"), "html.parser")
    soup4 = BeautifulSoup(open("newcolor.html"), "html.parser")

    # Finding where the new color should go
    colorsection = soup3.find(class_="color-item")

    # Inserting the newcolor html - that was read using BS
    colorsection.insert_before(soup4)

    # Saving the file
    with open("index.html", "w") as file:
        file.write(str(soup3))

#### RUN FUNCTION
#colorScrape("https://www.pantone.com/colorstrology")
