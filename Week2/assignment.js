console.log("=== task1 ===")
function findAndPrint(messages){
    // write down your judgment rules in comments
    // 先將以下文字內容做推測，發現滿十八歲的Bob及大學學生的Copper和合法年紀的Leslie
    // 從字串中找出有相關的字，如果有就判斷為真，然後印出該字典的key
    // your code here, based on your own rules
    // 如果屬性名稱是存儲在變數中，則需要使用方括號語法
    for(let name in messages){//name變數會被設置為當前"迴圈的key"
        let value = messages[name]//寫成name的話會是key，要寫成messages[name]
        if(value.includes("18 years old") || value.includes("college student") || value.includes("legal age")){
            console.log(name)
        }
    }
    } 

findAndPrint({
    "Bob":"My name is Bob. I'm 18 years old.", "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.", "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning." 
});
console.log("=== task2 ===")
function calculateSumOfBonus(data){
    // write down your bonus rule in comments
    // # 先將美金轉成台幣匯率30
    // # 各職務保底績效工程師3000，CEO2000，Sales1500
    // # 根據薪資再加1%
    // # 根據表現再乘以1.25到0.75的比例
    // # 最後績效值不得超出10000
    // your code here, based on your own rules
    let total_price = 0;
    for(let i of data.employees){
        let salary = i.salary
        if (typeof salary === "string"){
            if(salary.includes("USD")){
                salary = Number(salary.replace("USD",""))*30;
            }else{
                salary = Number(salary.replace(",",""))
            }
        }
        let bonus = 0;
        if(i.role == "Engineer"){
            bonus = 3000;
        }else if(i.role == "CEO"){
            bonus = 2000;
        }else{
            bonus = 1500;
        }//是else if不是 elif
        bonus += salary*0.01;
        if(i.performance == "above average"){
            bonus=bonus*1.25;
        }else if(i.performance == "average"){
            bonus=bonus*1
        }else{
            bonus=bonus*0.75
        }
        total_price+=bonus;
    }
    console.log(total_price)
    } 
calculateSumOfBonus({
    "employees":[ {
    "name":"John", "salary":"1000USD", "performance":"above average", "role":"Engineer"
    }, {
        "name":"Bob", "salary":60000, "performance":"average", "role":"CEO"
    }, {
        "name":"Jenny", "salary":"50,000", "performance":"below average", "role":"Sales"
    } ]
    }); // call calculateSumOfBonus function
console.log("=== task3 ===");
function func(...data){
    // your code here
    let obj={};
    // 如果屬性名稱是存儲在變數中，則需要使用方括號語法
    // in 是用來遍歷物件的鍵
    for(let name of data){
        let second = name[1];
        if(name[1] in obj){
            delete obj[second];
        }else{
            obj[second]=name;
        }
    }
    // 不寫for回圈的話就寫Object.values(obj)[0]
    if(Object.keys(obj).length>0){
        console.log(Object.values(obj)[0]);
    }else{
        console.log("沒有")
    }

    }
    func("彭大牆", "王明雅", "吳明"); // print 彭大牆
    func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花 
    func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
console.log("=== task4 ===");
function getNumber(index){
    // your code here
    // 發現偶數項是4開始公差為3的等差數列
    // 發現奇數項是0開始公差為３的等差數列
    // index奇數其實是偶數項
    // index偶數其實是奇數項
    let n;
    if(index%2 === 0){       
        n=0+ 3 * Math.floor(index/2); 
        
    }else{
        n=4+ 3 * Math.floor((index-1)/2);
        
    }
    console.log(n);
    }
getNumber(1); // print 4 
getNumber(5); // print 10 
getNumber(10); // print 15
console.log("=== task5 ===");
function findIndexOfCar(seats, status, number){
    // your code here
    let final = -1;
    for(let i=0;i<seats.length;i++){
        if(seats[i]>number && status[i]){
            final = i+1;
            break;
        }
    }
    console.log(final)
}
findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4 
findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1 
findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
