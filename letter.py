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

# list_url = 'https://letterboxd.com/crew/list/the-2010s-most-popular-films/'

list_url = 'https://letterboxd.com/jaywill/list/my-highest-rated-of-every-year/'

getLetterPage.getLetterPage(list_url)


print("done")