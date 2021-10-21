from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random

page = requests.get("https://www.reviews.io/company-reviews/store/stevesie.com?utm_source=stevesie.com&utm_medium=widget&utm_campaign=carousel")
page

soup = bs(page.content)
soup

soup.find_all('span',class_='Review__body')

quotes = [i.text for i in soup.find_all('span',class_='Review__body')]
quotes

# Creating a DataFrame to store our newly scraped information
df = pd.DataFrame()# Storing the quotes and authors in their respective columns
df['Quotes'] = quotes
df
