import bs4
import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy
# 13841
#def url
def GetPageContent(url):
   page = requests.get(url,headers={"Accept-Language":"en-VN"})
   return bs4.BeautifulSoup(page.text, "html.parser")

# def craw

index_dataStart = 15000
index_dataEnd = 16000

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

# ###########################################################################
# # replace None value = -1
# for i in data_craw:
#   try:
#     if "Ngữ văn:" in i:
#         pass
#     else:
#         i.insert(4,"Ngữ văn:")
#         i.insert(5,"-1")
#     if "Ngoại ngữ:" in i:
#         pass
#     else:
#         i.insert(6,"Ngoại ngữ:")
#         i.insert(7,"-1")
#     if "Vật lý:" in i:
#         pass
#     else:
#         i.insert(8,"Vật lý:")
#         i.insert(9,"-1")
#     if "Hóa học:" in i:
#         pass
#     else:
#         i.insert(10,"Hóa học:")
#         i.insert(11,"-1")
#     if "Sinh học:" in i:
#         pass
#     else:
#         i.insert(12,"Sinh học:")
#         i.insert(13,"-1")
#     if "Lịch sử:" in i:
#         pass
#     else:
#         i.insert(14,"Lịch sử:")
#         i.insert(15,"-1")
#     if "Địa lý:" in i:
#         pass
#     else:
#         i.insert(16,"Địa lý:")
#         i.insert(17,"-1")
#   except:
#       pass

# for i in data_craw:
#     i[0].replace("Mã cụm:","")
#     i.remove(i[2])

# # remove column no need
# for i in data_craw:
#     try:
#         i.remove(i[3])
#         i.remove(i[4])
#         i.remove(i[5])
#         i.remove(i[6])
#         i.remove(i[7])
#         i.remove(i[8])
#         i.remove(i[9])
#     except:
#         pass
   
# # ep diem thanh float
# for i in data_craw:
#   try:
#     i[2] = float(i[2])
#     i[3] = float(i[3])
#     i[4] = float(i[4])
#     i[5] = float(i[5])
#     i[6] = float(i[6])
#     i[7] = float(i[7])
#     i[8] = float(i[8])
#     i[9] = float(i[9])
#   except:
#     pass

# x = 22

# # so hs co diem higher x
# point = []
# students_A0 = 0
# students_A1 = 0
# students_B0 = 0
# students_C0 = 0
# students_D0 = 0

# # sv tham gia thi khoi...
# students_A0_ = 0
# students_A1_ = 0
# students_B0_ = 0
# students_C0_ = 0
# students_D0_ = 0

# # def cong diem, dem so hs
# for i in data_craw:
#     try:
#         if i[2] != -1 and  i[5] != -1 and i[6] != -1:
#             A0 = i[2] + i[5] + i[6]
#             if  A0 >= x:
#                 students_A0 += 1
#             students_A0_ += 1
            
#         if i[2] != -1 and  i[5] != -1 and i[4] != -1:
#             A1 = i[2] + i[5] + i[4]
#             if A1 >= x:
#                 students_A1 += 1
#             students_A1_ += 1

#         if i[2] != -1 and  i[6] != -1 and i[7] != -1:
#             B0 = i[2] + i[6] + i[7]
#             if B0 >= x:
#                 students_B0 += 1
#             students_B0_ += 1

#         if i[3] != -1 and  i[8] != -1 and i[9] != -1:
#             C0 = i[3] + i[8] + i[9]
#             if C0 >= x:
#                 students_C0 += 1
#             students_C0_ += 1

#         if i[2] != -1 and  i[3] != -1 and i[4] != -1:
#             D0 = i[2] + i[3] + i[4]
#             if D0 >= x:
#                 students_D0 += 1
#             students_D0_ += 1
#     except:
#         pass
    
# point.append(students_A0)
# point.append(students_A1)
# point.append(students_B0)
# point.append(students_C0)
# point.append(students_D0)

# print("So hs tren")
# print(students_A0)
# print(students_A1)
# print(students_B0)
# print(students_C0)
# print(students_D0)
# print("tong so hs")
# print(students_A0_)
# print(students_A1_)
# print(students_B0_)
# print(students_C0_)
# print(students_D0_)

# try:
#     percent_student_higerX = []
#     percent_student_higerX.append( float(students_A0/students_A0_) * 100 ) 
#     percent_student_higerX.append( float(students_A1/students_A1_) * 100 ) 
#     percent_student_higerX.append( float(students_B0/students_B0_) * 100 ) 
#     percent_student_higerX.append( float(students_C0/students_C0_) * 100 ) 
#     percent_student_higerX.append( float(students_D0/students_D0_) * 100 ) 
# except:
#     pass
# print(point)
# print(percent_student_higerX)

# # print(point)

# #####################################################################################
# # Bar chart

# # assigning x and y coordinates 
# language = ['A00','A01','B00','C00', 'D00'] 
# # users = [80,60,20,50,80] 
# users = percent_student_higerX
# figure, axis = plt.subplots()
# axis.set_ylim(0,100)
# # depicting the visualization 
# index = numpy.arange(len(language)) 
# plt.bar(index, users, color='orange') 
# plt.xlabel('Exam block') 
# plt.ylabel('Percentages') 
# plt.xticks(index, language) 
  
# # displaying the title 
# plt.title(label=f'The number of student have scores higher than {x}',  fontweight=10,  pad='2.0') 

# rects = axis.patches

# # Make some labels.

# for rect, label in zip(rects, point):
#     height = rect.get_height()
#     axis.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
#             ha='center', va='bottom')

# plt.show()

# # df = pd.DataFrame(data_craw, columns = ["Mã cụm", "Số báo danh", "Toán", "Văn","Anh", "Lý", "Hóa","Sinh","Sử","Địa"])
# # print(df)
# # df["Toán"].plot(kind = 'hist')
# # plt.show()




