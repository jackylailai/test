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
mrt_dic[mrt]
output_file2="Week3/mrt_tour.csv"
if not os.path.exists(output_file2):
    with open(output_file2,'w',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['MRT station','Attractions'])
        for mrt,attractions in mrt_dic.items():
            writer.writerow([mrt,",".join(attractions)])
        print("mrt finished")
else:
    print("mri existed")