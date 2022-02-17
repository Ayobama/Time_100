# Python program to fetch the Time 100 Top Influential
# Ayobami

import pandas as pd

from bs4 import BeautifulSoup
import requests

url = "https://time.com/collection/100-most-influential-people-2021/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")
scores = []

for span in soup.findAll('li', class_="article-name"):
    result = list(span.stripped_strings)
    scores.append(result)

scores_a = []
for sublist in scores:
    for item in sublist:
        scores_a.append(item)

print(scores_a)

dict = {"Dimensions": scores_a}

df = pd.DataFrame(dict)

df.to_csv('Time_100_most_influential.csv')