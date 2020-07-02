import requests
from bs4 import BeautifulSoup
import getFacts

def getLetterPage(list_url):

    listPage = requests.get(list_url)
    soup = BeautifulSoup(listPage.text,'html.parser')
    
    all = soup.find_all("li", class_='poster-container')

    film_dict = {}

    for film in all:
        title = film.contents[1]
        film_ext = title['data-film-slug']
        #t2 = title['data-target-link']

        film_url = "https://letterboxd.com" + film_ext

        temp = getFacts.getFacts(film_url)

        film_dict[ temp["title"] ] = temp

        #print("Found: " + temp["title"])

    


#getLetterPage('https://letterboxd.com/crew/list/the-2010s-most-popular-films/')