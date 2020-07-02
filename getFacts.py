#from collections import namedtuple
import requests
from bs4 import BeautifulSoup
import getWiki


def getFacts(film_url):

    filmPage = requests.get(film_url)
    film_soup = BeautifulSoup(filmPage.text,'html.parser')

    title = film_soup.find(class_='headline-1 js-widont prettify')
    year = title.find_next_sibling().a
    director = year.parent.find_next_sibling("a")

    plot = getWiki.getWiki(title.get_text(),year.get_text())

    movie =	{
        "title":    title.get_text(),
        "year":     year.get_text(),
        "director": director.get_text(),
        "plot":     plot
    }

    return movie



