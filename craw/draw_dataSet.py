# importing modules  
import matplotlib.pyplot as plt 
import numpy
import pandas as pd
import csv
import time
from more_itertools import unique_everseen

start_time = time.time()

data_craw = []

with open('data_draw.csv',newline='', encoding='utf-8') as f, open('data_remove_dup.csv','w',newline='', encoding='utf-8') as out_file:
    out_file.writelines(unique_everseen(f))

with open('data_remove_dup.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
            data_craw.append(row)

for i in data_craw:
    if len(i) == 0:
       data_craw.remove(i)

print("Total number of studens: " + str(len(data_craw)))
# for i in data_craw:
#     print(i)
    

for i in data_craw:
  try:
    if "Ngữ văn:" in i:
        pass
    else:
        i.insert(4,"Ngữ văn:")
        i.insert(5,"-1")
    if "Ngoại ngữ:" in i:
        pass
    else:
        i.insert(6,"Ngoại ngữ:")
        i.insert(7,"-1")
    if "Vật lý:" in i:
        pass
    else:
        i.insert(8,"Vật lý:")
        i.insert(9,"-1")
    if "Hóa học:" in i:
        pass
    else:
        i.insert(10,"Hóa học:")
        i.insert(11,"-1")
    if "Sinh học:" in i:
        pass
    else:
        i.insert(12,"Sinh học:")
        i.insert(13,"-1")
    if "Lịch sử:" in i:
        pass
    else:
        i.insert(14,"Lịch sử:")
        i.insert(15,"-1")
    if "Địa lý:" in i:
        pass
    else:
        i.insert(16,"Địa lý:")
        i.insert(17,"-1")
  except:
      pass

for i in data_craw:
    i[0].replace("Mã cụm:","")
    i.remove(i[2])

# remove column no need
for i in data_craw:
    try:
        i.remove(i[3])
        i.remove(i[4])
        i.remove(i[5])
        i.remove(i[6])
        i.remove(i[7])
        i.remove(i[8])
        i.remove(i[9])
    except:
        pass
   
# ep diem thanh float
for i in data_craw:
  try:
    i[2] = float(i[2])
    i[3] = float(i[3])
    i[4] = float(i[4])
    i[5] = float(i[5])
    i[6] = float(i[6])
    i[7] = float(i[7])
    i[8] = float(i[8])
    i[9] = float(i[9])
  except:
    pass

x = 25

# so hs co diem higher x
point = []
students_A0 = 0
students_A1 = 0
students_B0 = 0
students_C0 = 0
students_D0 = 0

# sv tham gia thi khoi...
students_A0_ = 0
students_A1_ = 0
students_B0_ = 0
students_C0_ = 0
students_D0_ = 0

# def cong diem, dem so hs
for i in data_craw:
    try:
        if i[2] != -1 and  i[5] != -1 and i[6] != -1:
            A0 = i[2] + i[5] + i[6]
            if  A0 >= x:
                students_A0 += 1
            students_A0_ += 1
            
        if i[2] != -1 and  i[5] != -1 and i[4] != -1:
            A1 = i[2] + i[5] + i[4]
            if A1 >= x:
                students_A1 += 1
            students_A1_ += 1

        if i[2] != -1 and  i[6] != -1 and i[7] != -1:
            B0 = i[2] + i[6] + i[7]
            if B0 >= x:
                students_B0 += 1
            students_B0_ += 1

        if i[3] != -1 and  i[8] != -1 and i[9] != -1:
            C0 = i[3] + i[8] + i[9]
            if C0 >= x:
                students_C0 += 1
            students_C0_ += 1

        if i[2] != -1 and  i[3] != -1 and i[4] != -1:
            D0 = i[2] + i[3] + i[4]
            if D0 >= x:
                students_D0 += 1
            students_D0_ += 1
    except:
        pass
    
point.append(students_A0)
point.append(students_A1)
point.append(students_B0)
point.append(students_C0)
point.append(students_D0)

point_ = []
point_.append(students_A0_)
point_.append(students_A1_)
point_.append(students_B0_)
point_.append(students_C0_)
point_.append(students_D0_)

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

try:
    percent_student_higerX = []
    percent_student_higerX.append( round(float(students_A0/students_A0_) * 100,2) ) 
    percent_student_higerX.append( round(float(students_A1/students_A1_) * 100,2) ) 
    percent_student_higerX.append( round(float(students_B0/students_B0_) * 100,2) ) 
    percent_student_higerX.append( round(float(students_C0/students_C0_) * 100,2) ) 
    percent_student_higerX.append( round(float(students_D0/students_D0_) * 100,2) ) 
except:
    pass
print(f"So luong hoc sinh điểm cao trên {x}: " + str(point))
print(f"So luong hoc xet tuyen to hop: " + str(point_))
print("Phần trăm theo khối: " +  str(percent_student_higerX))
#################################################
# Bar chart
# assigning x and y coordinates 

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
}

ExamBlock = ['A00','A01','B00','C00', 'D00'] 
# users = [80,60,20,50,80] 
users = percent_student_higerX
figure, axis = plt.subplots()
axis.set_ylim(0,100)
# depicting the visualization 
index = numpy.arange(len(ExamBlock)) 
plt.bar(index, users, color='pink') 
plt.xlabel('Exam block') 
plt.xlabel(f'Total students: {len(data_craw)}',fontdict=font) 
plt.ylabel('Percentages (%)', fontdict=font) 
plt.xticks(index, ExamBlock) 
  
# displaying the title 
plt.title(label=f'The number of students reached scores higher than {x}',  fontweight=10,  pad='3.0',fontdict=font) 

rects = axis.patches

# Make some labels.

for rect, label in zip(rects, point):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
