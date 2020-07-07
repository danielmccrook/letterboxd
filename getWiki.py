import wikipedia
import requests
from bs4 import BeautifulSoup

def getWiki(title,year):

    try:
        wiki_page = wikipedia.page(title + " (" + year + " film)")

    except wikipedia.exceptions.PageError:
        #print("unclear movie result")

        try:
            wiki_page = wikipedia.page(title)
            #print("found by title: " + title)
        except wikipedia.exceptions.PageError:
            #print("unclear movie result")

            guess = wikipedia.search(title)

            for i in guess:
                if year in i:
                    option2 = i

                if "film" in i:
                    option3 = i

            if option2 == option3:
                wiki_page = wikipedia.page(option2)
                #print("found by comparison: " + title)

    return wiki_page.section("Plot")