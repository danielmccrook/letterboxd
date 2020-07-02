#import re
#import requests
#import wikipedia
#from bs4 import BeautifulSoup
#from csv import writer
#from collections import namedtuple
# functions
#import getWiki
#import getFacts
import getLetterPage

#letterboxdPage = requests.get('https://letterboxd.com/film/parasite-2019/')
# response = requests.get('https://letterboxd.com/film/moonlight-2016/')

#soup = BeautifulSoup(letterboxdPage.text,'html.parser')

list_url = 'https://letterboxd.com/crew/list/the-2010s-most-popular-films/'

getLetterPage.getLetterPage(list_url)

#print("Letterboxd movie is " + movie.title + " from " + movie.year + " by " + movie.director)

# TO-DO
# Confirm year and director attributes with wikipedia.  return that the wikipedia article is a match
# go through top 250 films and check for all


#movie.plot = getWiki.getWiki(movie)
print("done")
"""

def not_lacie(href):
    return href and not re.compile("lacie").search(href)
soup.find_all(href=not_lacie)


def listMethod(list_url):
    list_page = requests.get(list_url)
    list_soup = BeautifulSoup(list_page.text,'html.parser')
    movies = list_soup.find_all(class_="poster-container numbered-list-item")

    for film in movies:
        bar = film.find(class_="frame")
        bar2 = bar.parent
        # key = re.compile("film")
        # bar3 = bar2.find_all("film")
        # bar4 = bar2.find(re.compile("/film/"))
        bar3 = bar2.find_all(lambda t: t.get("data-film-slug","").startswith("/film"))

        print(bar3)


listMethod('https://letterboxd.com/visdave34/list/official-top-250-narrative-feature-films/')
"""