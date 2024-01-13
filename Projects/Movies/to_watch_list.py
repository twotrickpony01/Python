import urllib2
from bs4 import BeautifulSoup

def download_and_parse_movies (year):

    #goes to the Box Office Mojo for the yearly charts
    url = 'http://www.boxofficemojo.com/yearly/chart/?yr=' + str(year) +  '&p=.htm'

    #pulls the page into memory
    filehandle = urllib2.urlopen(url)

    #parses [most of] the unwanted information out of the saved page after opening it
    soup = BeautifulSoup(filehandle)
    movies = soup.find_all('font', attrs={'size' : '2'})

    #adds the relevant information to a list [to be parsed later]
    movie_information = []
    for tr in movies:
        if "Summary of" in tr.text: #this is where the relevant information ends due to web-page oddities
            break
        else:
            movie_information.append((tr.text).encode('utf-8')) #everything should be utf-8 encoded to help normalize data.

    return movie_information

for year in range(1980, 2016): #The year range. Later this can made into a method for specific year queries.
    print(year)
    print(download_and_parse_movies(year)[10:]) #The first 10 entries for each year are worthless
