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

# defining the html contents of a URL.
xhtml = url_get_contents('https://postings.speechwire.com/r-uil-academics.php?groupingid=8&Submit=View+postings&region=&district=11&state=&conference=3&seasonid=18').decode('utf-8')

# Defining the HTMLTableParser object
p = HTMLTableParser()
p.feed(xhtml)

p.tables[4][0].pop(0)
p.tables[4][0][0] = 'Place'

# converting the parsed data to
# dataframe
print("\n\nPANDAS DATAFRAME\n")
print(pd.DataFrame(p.tables[4]))