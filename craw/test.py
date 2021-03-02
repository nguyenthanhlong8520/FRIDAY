
import bs4
import requests
import csv
import pandas as pd

def GetPageContent(url):
   page = requests.get(url,headers={"Accept-Language":"en-VN"})
   return bs4.BeautifulSoup(page.text, "html.parser")

def CrawData():
   data_craws=[]
   #13841 -> 999999
   for i in range(14841,14850):
      try:
         data_craw=[]
         x = str(i)
         url = 'https://diemthi.vnexpress.net/diem-thi-nam-2018/detail/id/' + x
         soup = GetPageContent(url)
        #  table=soup.find("div",class_="monthi_thisinh").text
        #  table = table.replace("\n\n","")
        #  data_craw.append(table.replace("\n",", "))
        
         place = soup.find("div",class_="macum_thisinh").text
        #  place = place.replace("Mã cụm:  ","")
         place = place.replace(" - ","")
         infor = soup.find("ul",class_='tt_coban').text
        #  infor = infor.replace("Số báo danh:","")
         data_craw.append(place.replace("\n",""))
         data_craw.append(infor.replace("\n",""))
         point = soup.find("div", class_="monthi_thisinh right")

         point = point.findAll("li")
         for li in point:
             li = li.text
            #  li = li.replace("Toán:","")
            #  li = li.replace("Ngữ văn:","")
            #  li = li.replace("Ngoại ngữ:","")
            #  li = li.replace("Vật lý:","")
            #  li = li.replace("Địa lý:","")
            #  li = li.replace("Hóa học:","")
            #  li = li.replace("Sinh học:","")
             data_craw.append(li)
            
         data_craws.append(data_craw)
      except:
         pass
   print(soup)
   return data_craws

def Export(data_craw):
   with open('data_set.csv','w',encoding="utf-8") as csvfile:
      ewriter=csv.writer(csvfile)
      ewriter.writerows(data_craw)


data_craw = CrawData()

data_craw = CrawData()
# Export(data_craw)
# print(data_craw)
for i in data_craw:
      print(i)

# df = pd.DataFrame(data_craw)
# print(df)



