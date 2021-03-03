import bs4
import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import time

start_time = time.time()
# 13841
#def url
def GetPageContent(url):
   page = requests.get(url,headers={"Accept-Language":"en-VN"})
   return bs4.BeautifulSoup(page.text, "html.parser")

# def craw

index_dataStart = 113000
index_dataEnd = 116000

def CrawData():
   data_craws=[]
   #13841 -> 999999
   for i in range(index_dataStart,index_dataEnd):
      try:
         data_craw=[]
         x = str(i)
         url = 'https://diemthi.vnexpress.net/diem-thi-nam-2018/detail/id/' + x
         soup = GetPageContent(url)
         place = soup.find("div",class_="macum_thisinh").text
         place = place.replace("Mã cụm:  ","")
         place = place.replace(" - ","")
         infor = soup.find("ul",class_='tt_coban').text
         infor = infor.replace("Số báo danh:","")
         data_craw.append(place.replace("\n",""))
         data_craw.append(infor.replace("\n",""))
         point = soup.find("div", class_="monthi_thisinh right")

         point = point.findAll("li")
         for li in point:
             data_craw.append(li.find("p").text)
             li = li.find("strong").text
             data_craw.append(li)
            
         data_craws.append(data_craw)
      except:
         pass
   #print(soup)
   return data_craws

#   Export function
def Export(data_craw):
   with open('data_set.csv','w',encoding="utf-8") as csvfile:
      ewriter=csv.writer(csvfile)
      ewriter.writerows(data_craw)

# def craw_data
data_craw = CrawData()
Export(data_craw)

# print(f"{index_dataStart}" + " " + f"{index_dataEnd}")
print("--- %s seconds ---" % (time.time() - start_time))
