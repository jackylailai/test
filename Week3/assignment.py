# info是捷運站
# stitle是景點
# address區域
# file有圖片
# longitude經度
# latitude緯度
import os
import json
import csv
from urllib.request import urlopen
# 讀取
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
response = urlopen(url)
data = json.load(response)

fields = ['stitle', 'address', 'longitude', 'latitude','file']
output_file = 'Week3/tour.csv'
if not os.path.exists(output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        # 寫入CSV 
        writer.writeheader()

        # 寫入每一筆資料
        for item in data['result']['results']:
            address = item['address'].split('市', 1)[1].split('區', 1)[0]+ "區"
            capital = item['file'].split('JPG',1)[0]+'jpg'
            lower = item['file'].split('jpg',1)[0]+'jpg'
            if len(capital)<len(lower):
                image_url = item['file'].split('JPG',1)[0]+'jpg'
            else:
                image_url = item['file'].split('jpg',1)[0]+'jpg'
            row = {
                'stitle': item['stitle'],
                'address': address,
                'longitude': item['longitude'],
                'latitude': item['latitude'],
                'file': image_url
            }
            writer.writerow(row)
    print("finished")
else:
    print("tour existed")
# list=[]
# for i in data['result']['results']:
#     if i["MRT"] in list:
#         continue
#     else:
#         list.append(i["MRT"])
# print(list)
# print(len(list))
mrt_dic={}
for i in data['result']['results']:
    mrt = i['MRT']
    if mrt not in mrt_dic:
        mrt_dic[mrt]=[]
    mrt_dic[mrt].append(i['stitle'])
output_file2="Week3/mrt_tour.csv"

if not os.path.exists(output_file2):
    with open(output_file2,'w',newline='')as file:
        writer = csv.writer(file)
        fields = ['MRT station'] + [f'Attraction{i+1}' for i in range(max(len(attractions) for attractions in mrt_dic.values()))]
        #表格填寫mrt，後續補上景點，首先先將所有景點遍歷找出所有景點的字典長度(此字典包含mrt:attractions)，
        #然後找出最大的值，再將最大值列入另一迴圈寫入表格(按照1,2,3...)，但因為索引值從一開始，統一加一。
        writer.writerow(fields)
        print(fields)
        for mrt,attractions in mrt_dic.items():
            row_data = [mrt] + attractions#attractions是value的list
            # 缺少欄位補上空值
            if len(row_data) < len(fields):
                row_data.extend([''] * (len(fields) - len(row_data)))
            writer.writerow(row_data)
        print("mrt finished")
else:
    print("mri existed")