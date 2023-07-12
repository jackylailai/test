import json
def find_and_print(messages):
# write down your judgment rules in comments
# 先將以下文字內容做推測，發現滿十八歲的Bob及大學學生的Copper和合法年紀的Leslie
# 從字串中找出有相關的字，如果有就判斷為真，然後印出該字典的key
# your code here, based on your own rules
    print("=== TASK 1 ===")
    for name, message in messages.items():
        if "18 years old" in message or "college student" in message or "legal age" in message:
            print(name)   
find_and_print({
"Bob":"My name is Bob. I'm 18 years old.", "Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.", "Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week", "Jenny":"Good morning."
})
print("=== TASK 2 ===")
def calculate_sum_of_bonus(data):
# write down your bonus rules in comments
# 先將美金轉成台幣匯率30
# 各職務保底績效工程師3000，CEO2000，Sales1500
# 根據薪資再加1%
# 根據表現再乘以1.25到0.75的比例
# 最後績效值不得超出10000
# your code here, based on your own rules
    total_bonus=0
    for i in data["employees"]:
        salary = i["salary"]
        if isinstance(salary, str): # 如果薪資是str
            if "USD" in salary: # 如果薪資為美金
                salary = int(salary.replace("USD","")) * 30
            else: # 如果薪資含有","
                salary = int(salary.replace(",",""))
        if i["role"]=="Engineer":
            bonus = 3000
        elif i["role"]=="CEO":
            bonus = 2000
        else:
            bonus=1500
        bonus += int(salary)*0.01

        if i["performance"]=="above average":
            bonus=bonus*1.25
        elif i["performance"]=="average":
            bonus=bonus*1
        else:
            bonus=bonus*0.75
        total_bonus+=bonus
    print(int(total_bonus))
calculate_sum_of_bonus({ "employees":[
{
"name":"John","salary":"1000USD", "performance":"above average", "role":"Engineer"
}, {
    "name":"Bob", "salary":60000, "performance":"average", "role":"CEO"
}, {
    "name":"Jenny", "salary":"50,000", "performance":"below average", "role":"Sales"
} ]
}) # call calculate_sum_of_bonus function
print("=== Task3 ===")
def func(*data):
# your code here
    dic = {}  
    for i in data:
        if i[1] in dic:
            del dic[i[1]]
        else:
            dic[i[1]]=i
    if dic:
        for value in dic.values():
            print(value)
    else:
        print("沒有")  
func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
print("=== Task4 ===")
def get_number(index):
# your code here 
    if index % 2 == 0: # 如果索引是偶數 實際是第一三五項
        n = 0
        ans = 3*(index / 2)
        print(int(ans))
    else: # 如果索引是奇數 實際是第二四六項
        n = 4
        ans = n + 3*((index-1)/ 2)
        print(int(ans))
get_number(1) # print 4
get_number(5) # print 10 
get_number(10) # print 15
# list= [0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15,]
print("=== Task5 ===")
def find_index_of_car(seats, status, number):
# your code here
    final = -1
    li = {}
    for i in range(len(seats)):
        if seats[i] >= number and status[i]==1:#要視為數字不是字串
            seat = seats[i]
            remaining=seat-number
            li[remaining]=i
    if len(li) == 0:    
        print(final)
    else:
        print(li[min(li)])
find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4 
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1 
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2