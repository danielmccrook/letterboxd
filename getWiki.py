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
    
"""
    s1 = wikipedia.suggest("Parasite")

s2 = wikipedia.page("Parasite (2019 film)")

# Parasite (2019 film)

for i in s2:

    if name_predict in i:
        option = i

    if year in i:
        option2 = i

    if "film" in i:
        option3 = i





    wiki_url = wikipedia.page(movie.title + " (" + movie.year + " film)").url
    wiki_page = requests.get(wiki_url)
    wiki_soup = BeautifulSoup(wiki_page.text,'html.parser')


    title_confirm = wiki_soup.find(class_='summary')

    #director_confirm = title_confirm.parent
    director_confirm = title_confirm.parent.parent.find("th",string="Directed by").next_sibling
    #print(director_confirm1)
    #director_confirm = director_confirm1



    #print(director_confirm.get_text())
    # find(title=director).get_text()
    
    title_wiki = title_confirm.get_text()
    director_wiki = director_confirm.get_text()

    plot = wiki_soup.find(id="Plot")

    tit = plot.parent

    sum = tit.find("p")

    print(plot)

    
    #print(title_confirm)
    #print(director_confirm)
    #print(director_confirm1)

    if movie.title != title_wiki:
        print("title error: "+movie.title+" != "+title_wiki)

    if movie.director != director_wiki:
        print("director error: "+movie.director+" != "+director_wiki)



    # .find_next_siblings("tr")
    # director_confirm2 = director_confirm
    # find_next_sibling("th","row","Directed by")
    # .find('Directed by')

    # print(title_confirm)
    # print(director_confirm2)


"""