from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("/Users/pavanaj/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)
headers=["V Mag.(mv)", "Proper name", "Bayer designation", "distance(ly)", "Spectral class","Mass(M)","Radius(R)","Luminosity(L)"]
planet_data=[]
new_planet_data=[]
def scrape():
    
    for i in range(0,201):

        soup=BeautifulSoup(browser.page_source,"html.parser")
        
        for ul_tag in soup.find_all("ul",attrs=("class","exoplanet")):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            
        #print(planet_data)
        browser.find_element_by_xpath('').click()
        
   # with open("scrap1.csv","w") as f:
    #    csvwriter=csv.writer(f)
     #   csvwriter.writerow(headers)
      #  csvwriter.writerows(planet_data)

def scrape_more_data(hyperlink):
    

    page=requests.get(hyperlink)
    soup=BeautifulSoup(page.content,"html.passer")
    temp_list=[]
    for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
        td_tags=tr_tag.find_all("td")
        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
            except:
                temp_list.append("")
        new_planet_data.append(temp_list)



scrape()
for data in planet_data:
    scrape_more_data(data[5])

final_star_data=[]
for index,data in enumerate(planet_data):
    final_star_data.append(data+final_star_data[index])

with open("final.csv","w") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_star_data)