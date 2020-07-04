import requests
from bs4 import BeautifulSoup
import getReviewPage

def getReviews(film_url):

    review_url = film_url + "reviews/by/activity/"

    i = 1
    reviews = ['1']

    while i<=10:

        if i>1:
            review_url = film_url + 'reviews/by/activity/page/' + str(i) + '/'

        if i==1:
            reviews[0] = getReviewPage.getReviews(review_url)
        else:
            reviews.append(getReviewPage.getReviews(review_url))

        i += 1
    
    #reviewPage = requests.get(review_url)
    #review_soup = BeautifulSoup(reviewPage.text,'html.parser')

    #page1 = review_soup.find_all("li",class_="film-detail")

    #for review in page1:
    #    print("1")

getReviews('https://letterboxd.com/film/moonlight-2016/')
print("done")