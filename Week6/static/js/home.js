    // 監聽 submit 事件
console.log("成功導入")
document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("signinForm").addEventListener("submit", function(event) {
        // 取得 checkbox 的狀態
        var agreeCheck = document.getElementById("agree");
        var isChecked = agreeCheck.checked;

        // 如果 checkbox 沒有被勾選，阻止表單的提交，顯示警示對話框
        if (!isChecked) {
            alert("Please check the checkbox first");
            event.preventDefault(); // 阻止表單提交
        }
    });
});
// 啟動監聽器，抓住click的動作，傳入function參數，然後將event再傳入後續的函式
document.addEventListener("DOMContentLoaded", function () {
        document.getElementById("calculateButton").addEventListener("click", function(event) {
            event.preventDefault(); // 首先先阻止表單提交，
            calculateSquared();//才執行我要的function，我後續我自己提交到後端
    });
});
function calculateSquared() {
    // 取得輸入的數字
    var inputNumber = document.getElementById("number").value;
    console.log("實作計算按鈕function")
    // 檢查是否為正整數
    if (!inputNumber || isNaN(inputNumber) || parseInt(inputNumber) <= 0) {
        alert("請輸入一個正整數");
        return false;
    }

    // 導入顯示結果的頁面並將數字附加到網址後面
    window.location.href = "/square/" + inputNumber;
}

