console.log("成功引入js")
document.addEventListener("DOMContentLoaded", function () {
    var deleteButtons = document.querySelectorAll(".deletebutton");
    deleteButtons.forEach(function (button) {
        button.addEventListener("click", function (event) {
            var confirmed = confirm("確定要刪除嗎？");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
});
document.addEventListener("DOMContentLoaded", function() {
    console.log("成功進入查詢func");
    let searchButton = document.getElementById("searchButton");
    let usernameInput = document.getElementById("usernameInput");
    let resultDiv = document.getElementById("result");

    searchButton.addEventListener("click", function() {
        let username = usernameInput.value;
        if (username) {
            fetchMember(username);
            //找到都丟給下個func處理
        }
    });

    function fetchMember(username) {
        let url = `http://127.0.0.1:3000/api/member?username=${username}`;
        fetch(url)//
            .then(response => response.json())//將從網絡請求返回的 JSON 字串轉換成 JavaScript 物件
            .then(data => {
                if (data.data) {
                    let html = `
                        <p>${data.data.name}(${data.data.username})</p>
                    `;
                    resultDiv.innerHTML = html;
                    console.log("成功查詢完畢");
                } else {
                    resultDiv.innerHTML = "找不到會員資料";
                }
            })
            .catch(error => {
                resultDiv.innerHTML = "查詢出現錯誤";
                console.error(error);
            });
    }
});
document.addEventListener("DOMContentLoaded", function() {
    console.log("成功進入修改func");
    let updateButton = document.getElementById("updateButton");
    let nameUpdateInput = document.getElementById("usernameUpdate");
    let result2 = document.getElementById("result2");

    updateButton.addEventListener("click", function() {
        let newName = nameUpdateInput.value;
        if (newName) {
            updateMemberName(newName);
        }
    });
    //再開一個func
    function updateMemberName(newName) {
        let url = "http://127.0.0.1:3000/api/member";

        fetch(url, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "name": newName })
        })
        .then(response => response.json())
        .then(data => {
            if (data.ok) {
                result2.innerHTML = "姓名更新成功";
            } else {
                result2.innerHTML = "姓名更新失敗";
            }
        })
        .catch(error => {
            result2.innerHTML = "更新過程中出現錯誤";
            console.error(error);
        });
    }
});
