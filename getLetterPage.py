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

        film_url = "https://letterboxd.com" + film_ext

        temp = getFacts.getFacts(film_url)

        film_dict[ temp["title"] ] = temp

        print(temp["title"])