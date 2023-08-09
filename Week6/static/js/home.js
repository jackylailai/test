// 監聽 submit 事件
console.log("成功導入")
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("signinForm").addEventListener("submit", function (event) {
        var username = document.getElementById("username2").value;
        var password = document.getElementById("password2").value;

        if (!username || !password) {
            alert("請填寫帳號和密碼");
            event.preventDefault(); // 阻止表單提交
        }
    });
});
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("signupForm").addEventListener("submit", function (event) {
        var fullname = document.getElementById("fullname").value;
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;

        if (!fullname || !username || !password) {
            alert("請填寫完整資訊");
            event.preventDefault(); // 阻止表单提交
        }
    });
})

