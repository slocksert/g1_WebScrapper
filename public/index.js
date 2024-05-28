async function carregarDados() {
    const response = await axios.get('http://localhost:8000/news');
    const noticias = response.data;
    const container = document.getElementById('grid-container');

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = String(date.getFullYear()).slice(-2);
        return `${day}/${month}/${year}`;
    };

    noticias.forEach(noticia => {
        const ul = document.createElement('ul');
        ul.className = 'flex-item';

        const nameLi = document.createElement('li');
        nameLi.textContent = `Notícia: ${noticia.news}`;

        const linkLi = document.createElement('li');
        const link = document.createElement('a');
        link.textContent = "Link: " + noticia.link;
        link.href = noticia.link;
        link.target = "_blank";
        linkLi.appendChild(link);

        const dateLi = document.createElement('li');
        dateLi.textContent = `Data: ${formatDate(noticia.date)}`;

        const imageLi = document.createElement('li');
        const image = document.createElement('img');
        image.className = 'image-item';

        if (noticia.image && noticia.image.trim() !== "") {
            image.src = noticia.image;
        } else {
            image.src = 'noimage.jpg';
        }

        image.alt = noticia.news;
        image.width = 500;
        image.height = 350;
        imageLi.appendChild(image);

        ul.appendChild(nameLi);
        ul.appendChild(linkLi);
        ul.appendChild(dateLi);
        ul.appendChild(imageLi);

        container.appendChild(ul);
    });
}

window.onload = carregarDados;