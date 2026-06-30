import pandas as pd
import urllib.request
from pprint import pprint # Use pprint if you want to see the table in the least pretty way possible (ex. pp.pprint(p.tables[4]))
from html_table_parser.parser import HTMLTableParser

# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

    # Opens a website and read its
    # binary contents (HTTP Response Body)

    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    #reading contents of the website
    return f.read()

# Constants
DISCTRICTS_COUNT = 32
REGIONS_COUNT = 4

# Note that 2 is for some reason not a valid grouping id, so we skip it :(
GROUPING_IDS = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# Getting stuff from url
xhtml = url_get_contents('https://postings.speechwire.com/r-uil-academics.php?groupingid=8&Submit=View+postings&region=&district=11&state=&conference=3&seasonid=18').decode('utf-8')

# HTMLTableParser object
p = HTMLTableParser()
p.feed(xhtml)

# Cleaning up the data
p.tables[4][0].pop(0)
p.tables[4][0][0] = 'Place'

# converting the parsed data to dataframe
print("\n\nPANDAS DATAFRAME\n")
print(pd.DataFrame(p.tables[4]))