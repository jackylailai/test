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
