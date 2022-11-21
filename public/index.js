async function carregarDados(){
    const response = await axios.get('http://localhost:8000/news')
    
    const noticias = response.data
    
    const date = document.getElementById('news')
    const news = document.getElementById('news')
    const link = document.getElementById('news')

   
    news.innerHTML = ''
    link.innerHTML = ''
    date.innerHTML = ''

    noticias.forEach(noticia => {

        const date_item = document.createElement('li')
        const news_item = document.createElement('li')
        const link_item = document.createElement('li')
        
        const linha_date = `${noticia.date}`
        const linha_news = `${noticia.news}`
        const linha_link = `${noticia.link}`
        
        news_item.innerText = linha_news
        date_item.innerText = linha_date
        
        const a_item = document.createElement('a')
        a_item.href = linha_link
        a_item.innerText = linha_link

        news.appendChild(date_item)
        news.appendChild(news_item)
        news.appendChild(link_item)
        link_item.appendChild(a_item)

        date_item.setAttribute('id', 'date-id')
        news_item.setAttribute('id', 'news-id')
    })
}

function App(){
    console.log('App iniciado')
    carregarDados()
}

App()