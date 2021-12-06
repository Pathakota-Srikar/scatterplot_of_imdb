import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt


url = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"
response = requests.get(url)
pages = np.arange(1, 251, 50)
headers = {"Accept-Language": "en-US,en;q=0.5"}
name = []
ratings = []
votes = []

for page in pages: 
  
    page = requests.get("https://www.imdb.com/search/title/?groups=top_250,desc&start=" + str(page) + "&ref_=adv_nxt", headers=headers)

    soup = BeautifulSoup(page.text,"html.parser")

    movies = soup.findAll('div',{'class':'lister-item mode-advanced'})

    for i in movies:

        ratings.append(i.find('div',{'class':'inline-block ratings-imdb-rating'})['data-value'])

        votes.append(i.find('span',{'name':'nv'})['data-value'])

ratings = sorted(ratings, key=float)
votes = sorted(votes, key=int)

plt.scatter(votes,ratings)
plt.show()