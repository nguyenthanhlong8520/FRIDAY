import pandas as pd

# df = pd.read_csv("data_set.csv")

data = [
    ['Mã cụm:  BKA', 'Số báo danh: 570', 'Toán:', '6.75', 'Ngữ văn:', '4.75', 'Ngoại ngữ:', '3.75', 'Vật lý:', '3.60', 'Địa lý:', '6.50'],
    ['Mã cụm:  BKA', 'Số báo danh: 570', 'Toán:', '6.75', 'Ngữ văn:', '4.75', 'Ngoại ngữ:', '3.75', 'Vật lý:', '3.60', 'Địa lý:', '6.50'],
    ['Mã cụm:  BKA', 'Số báo danh: 4741', 'Toán:', '4.50', 'Ngữ văn:', '5.00', 'Ngoại ngữ:', '5.35', 'Địa lý:', '4.50'],
    ['Mã cụm:  BKA', 'Số báo danh: 5875', 'Toán:', '6.00', 'Vật lý:', '6.20', 'Hóa học:', '5.60'],
    ['Mã cụm:  BKA', 'Số báo danh: 10022', 'Toán:', '2.00', 'Ngữ văn:', '6.25', 'Ngoại ngữ:', '2.75', 'Lịch sử:', '3.00', 'Địa lý:', '4.00'],
    ['Mã cụm:  BKA', 'Số báo danh: 7583', 'Toán:', '7.75', 'Hóa học:', '5.20', 'Sinh học:', '6.80']
]

# "Toán:" "Ngữ văn:"  "Ngoại ngữ:"  "Vật lý:" "Hóa học:" "Sinh học:" "Lịch sử:" "Địa lý:" ""
# 

for i in data:
    if "Ngữ văn:" in i:
        pass
    else:
        i.insert(4,"Ngữ văn:")
        i.insert(5,"None")
    if "Ngoại ngữ:" in i:
        pass
    else:
        i.insert(6,"Ngoại ngữ:")
        i.insert(7,"None")
    if "Vật lý:" in i:
        pass
    else:
        i.insert(8,"Vật lý:")
        i.insert(9,"None")
    if "Hóa học:" in i:
        pass
    else:
        i.insert(10,"Hóa học:")
        i.insert(11,"None")
    if "Sinh học:" in i:
        pass
    else:
        i.insert(12,"Sinh học:")
        i.insert(13,"None")
    if "Lịch sử:" in i:
        pass
    else:
        i.insert(14,"Lịch sử:")
        i.insert(15,"None")
    if "Địa lý:" in i:
        pass
    else:
        i.insert(16,"Địa lý:")
        i.insert(17,"None")
# for i in data:
#     i.re("Mã cụm:","")
    
for i in data:
    print(i[0])
