import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


data={
    "Quote": [],
    "Author": []
}


for i in range(1,11):
    url=f"https://quotes.toscrape.com/page/{i}"
    try:
        #Fetching html
        
        res=requests.get(url)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request Failed to fetch page {i}: {e}")
        continue

    #Parsing html with Beautifulsoup

    soup=BeautifulSoup(res.content, "html.parser")
    
    #Getting Quotes

    results=soup.find_all("span", class_="text")

    for result in results:
            print(result.get_text())
            data["Quote"].append(result.get_text())

    #Getting Author's 

    s=soup.find_all("small", class_="author")
    for results in s:
             print(results.get_text())
             data["Author"].append(results.get_text())

    sleep(1)


# print(soup.prettify())


#For Saving in Excel File
df=pd.DataFrame(data)
try:
    df.to_excel("Quotes_Scraping.xlsx", index=False)
except Exception as e:
    print("Could not save file", e)

