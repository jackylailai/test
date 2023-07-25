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