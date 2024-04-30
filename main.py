import requests

links = ["https://ej-portfolio.onrender.com","https://ej-todo.onrender.com","https://ej-cafe-api.onrender.com",
         "https://ej-blog-app.onrender.com","https://ej-ecom-website.onrender.com","https://ej-cafe-finder.onrender.com",
         "https://ej-stock-api-website.onrender.com","https://ej-image-color-palatte.onrender.com",
         "https://ej-pdf-to-voice.onrender.com"]


for url in links:
    data = requests.get(url=url)
