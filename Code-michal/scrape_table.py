from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

url = "https://www.americashealthrankings.org/explore/annual"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
time.sleep(2)

browser.links.find_by_text('National Overall')
time.sleep(2)
html = browser.html
soup = bs(html,'html.parser')
table =soup.find_all('table')


table=pd.read_html(str(table[1]))
df_table=table[0]

healthRankTable = df_table.to_html()

