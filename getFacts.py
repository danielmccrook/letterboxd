#from collections import namedtuple
import requests
from bs4 import BeautifulSoup
import getWiki
import getReviewPage
import pickle

def getFacts(film_url):

    filmPage = requests.get(film_url)
    film_soup = BeautifulSoup(filmPage.text,'html.parser')

    title = film_soup.find(class_='headline-1 js-widont prettify')
    year = title.find_next_sibling().a
    director = year.parent.find_next_sibling("a")

    plot = getWiki.getWiki(title.get_text(),year.get_text())
    
    # how many pages of reviews
    reviews = getReviewPage.getReviews(film_url,3)

    movie =	{
        "title":    title.get_text(),
        "year":     year.get_text(),
        "director": director.get_text(),
        "plot":     plot,
        "reviews":  reviews
    }

    pickle_out = open(movie["title"] + '.pickle',"wb")
    pickle.dump(movie, pickle_out)
    pickle_out.close()
    
    # with open(movie["title"]+'.pickle', 'wb') as fp:
    #     pickle.dump(movie["title"], fp)
    #     pickle.dump(movie["year"], fp)
    #     pickle.dump(movie["director"], fp)
    #     pickle.dump(movie["plot"], fp)
    #     pickle.dump(movie["reviews"], fp)

    return movie



