//========================= create time ================================

const targetDate = new Date(new Date().getTime() + 2 * 24 * 60 * 60 * 1000).getTime();

const countdownInterval = setInterval(function () {
    const now = new Date().getTime();
    const timeLeft = targetDate - now;

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    document.getElementById("days").textContent = days;
    document.getElementById("hours").textContent = hours;
    document.getElementById("minutes").textContent = minutes;
    document.getElementById("seconds").textContent = seconds;

    if (timeLeft <= 0) {
        clearInterval(countdownInterval);
        document.querySelector('.countdown').style.display = 'none';
        document.getElementById('offer-ended').style.display = 'block';
    }
}, 1000);

//======================== fetch news =================================

document.addEventListener("DOMContentLoaded", () => {
    const newsGrid = document.querySelector(".news-grid");

    async function fetchNews() {
        try {
            const response = await fetch('/fetch_news/');
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            displayNews(data.articles);
        } catch (error) {
            console.error('Error fetching news:', error.message);
            newsGrid.innerHTML = `<p class="error">Unable to load news. Please try again later. (${error.message})</p>`;
        }
    }

    function displayNews(articles) {
        if (!articles || articles.length === 0) {
            newsGrid.innerHTML = `<p class="no-news">No news available at the moment.</p>`;
            return;
        }

        // Limit to 3 articles
        const limitedArticles = articles.slice(0, 3);

        // Populate news content
        newsGrid.innerHTML = limitedArticles
            .map(article => `
                <div class="news-item">
                    <img src="${article.urlToImage || '../../static/img/foot_icon.png'}" alt="${article.title}" class="news-image">
                    <h5 class="news-title"><strong>${article.title}</strong></h5>
                    <p class="news-description">${article.description || 'No description available.'}</p>
                    <a href="${article.url}" target="_blank" class="news-link">Read more</a>
                </div>
            `)
            .join('');
    }
    // Fetch news on page load
    fetchNews();
});

//======================================================================






//====================== saved button ==============================
const savedIcons = document.querySelectorAll('.saved-icon');

savedIcons.forEach(icon => {
icon.addEventListener('click', function() {
    const card = icon.closest('.teacher-card');
    console.log("done");
    card.classList.toggle('saved');
    console.log("saved"); 
});
});

//======================= search bar ================================

document.querySelector('.input-group button').addEventListener('click', function() {
const searchQuery = document.querySelector('.input-group input').value.toLowerCase();
const cards = document.querySelectorAll('.teacher-card');

cards.forEach(card => {
    const teacherName = card.querySelector('.card-title').innerText.toLowerCase();
    if (teacherName.includes(searchQuery)) {
        card.style.display = 'block';
    } else {
        card.style.display = 'none';
    }
});
});
