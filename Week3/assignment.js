console.log("js succeed");
fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
    .then(response => response.json())
    .then(data => {
        console.log("fetch succeed");
        const attractions = data.result.results; // results是一個array
        let titles = [];
        let images = [];

        // 取得前三個attractions的title和image
        for (let i = 0; i < 3; i++) {
            const title = attractions[i].stitle;
            console.log("for內", title);
            titles.push(title);

            const firstImageUrl = attractions[i].file.split("https://")[1];
            console.log("First Image URL: " + "https://" + firstImageUrl);
            images.push("https://" + firstImageUrl);
        }

        console.log("for外", titles);
        console.log("for外", images);

        // 將前三個attractions的title和image顯示在promotion區塊
        for (let i = 0; i < 3; i++) {
            const promotionDiv = document.getElementById(`promotion${i + 1}`);
            const promotionImage = promotionDiv.querySelector('img');
            const promotionTitle = promotionDiv.querySelector('.title');

            promotionImage.src = images[i];
            promotionTitle.textContent = titles[i];
        }

        // 將後續的區塊插入圖片和文字
        for (let i = 3; i < attractions.length; i++) {
            const title = attractions[i].stitle;
            console.log("for內", title);
            titles.push(title);

            const imageUrl = attractions[i].file.split("https://")[1];
            console.log("Image URL: " + "https://" + imageUrl);
            images.push("https://" + imageUrl);

            const titlePicDiv = document.createElement('div');
            titlePicDiv.classList.add('titlepic');

            const titleImage = document.createElement('img');
            titleImage.src = images[i];
            titleImage.classList.add('image');
            titleImage.id = `pic${i + 1}`;

            const titleText = document.createElement('div');
            titleText.classList.add('title');
            titleText.textContent = titles[i];
            titleText.id = `title${i + 1}`;

            titlePicDiv.appendChild(titleImage);
            titlePicDiv.appendChild(titleText);

            const content2 = document.querySelector('.content2');
            content2.appendChild(titlePicDiv);
        }
    })
    .catch(error => console.error('Error:', error));
