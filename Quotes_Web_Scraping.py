import requests
from bs4 import BeautifulSoup
import pandas as pd


data={
    "Quote": [],
    "Author": []
}

res=requests.get("https://quotes.toscrape.com/")
soup=BeautifulSoup(res.content, "html.parser")

# print(soup.prettify())

#For Quotes:

results=soup.find_all("span", class_="text")
for result in results:
    print(result.get_text())
    data["Quote"].append(result.get_text())



#For Author's Name:

s=soup.find_all("small", class_="author")
for results in s:
    print(results.get_text())
    data["Author"].append(results.get_text())


#For Saving in CSV Format

# df=pd.DataFrame(data)
# df.to_csv("Quotes.csv", index=False)


#For Saving in Excel File
df=pd.DataFrame(data)
df.to_excel("QuotesScrapping.xlsx", index=False)