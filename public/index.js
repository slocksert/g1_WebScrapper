function formatDate(dateString){
    const date = new Date(dateString);
    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const year = String(date.getFullYear()).slice(-2);
    return `${day}/${month}/${year}`;
}

function createElement(element, content){
    const newElement = document.createElement(element);
    newElement.textContent = content;
    return newElement;
}

function createDateElement(element, content){
    const newElement = document.createElement(element);
    newElement.textContent = "Data:" + formatDate(content);
    return newElement;
}

function createLinkElement(link) {
    const newLi = document.createElement('li');
    const newA = document.createElement('a');
    newA.href = link;
    newA.textContent = "Link: " + link;
    newA.target = "_blank"
    newLi.appendChild(newA);
    return newLi;
}

function createImageElement(news) {
    const imageLi = document.createElement('li');
    const image = document.createElement('img');
    image.className = 'image-item';

    if (news.image && news.image.trim() !== "") {
        image.src = news.image;
    } else {
        image.src = 'noimage.jpg';
    }

    image.alt = news.news;
    image.width = 500;
    image.height = 350;
    imageLi.appendChild(image);
    return imageLi;
}

async function loadData() {
    const response = await axios.get('http://localhost:8000/news');
    const items = response.data;
    const container = document.getElementById('grid-container');

    items.forEach(news => {
        console.log(news.image)
        const ul = document.createElement('ul');
        ul.className = 'flex-item';
        const nameLi = createElement('li', `Notícia: ${news.news}`)
        const linkLi = createLinkElement(news.link)
        const dateLi = createDateElement('li', news.date)
        const imageLi = createImageElement(news)

        ul.appendChild(nameLi);
        ul.appendChild(linkLi);
        ul.appendChild(dateLi);
        ul.appendChild(imageLi);

        container.appendChild(ul);
    });
}

loadData()