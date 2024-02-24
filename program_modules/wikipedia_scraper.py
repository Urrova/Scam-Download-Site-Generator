import requests, urllib.parse, typing
from bs4 import BeautifulSoup

class WikipediaScraper:
    def __init__(self):
        pass
    #Obtiene un articulo y lo scrapea, devuelve un diccionario
    def get_article(self, article_name: str) -> typing.Dict:
        #Crea un diccionario para dumpear toda la informacion
        article_content: typing.Dict[str, str] = {"title":"", "resume": "", "__error__": "0"}

        #Obtiene la pagina y la convierte a soup
        req_url = "https://en.wikipedia.org/w/index.php?search="+urllib.parse.quote_plus(article_name)
        try:
            req = requests.get(req_url)
        except requests.exceptions.ConnectionError:
            article_content["__error__"] = "1"
            return article_content
        
        soup = BeautifulSoup(req.content, 'html.parser')

        #Titulo
        article_content["title"] = soup.find(id="firstHeading").get_text() 

        #Resumen
        article_resume_tag: str = soup.find(attrs={"class": "mw-content-ltr mw-parser-output"})
        if article_resume_tag != None:
            article_content["resume"] = article_resume_tag.p.get_text()

        #Imagen
        article_image_tag = soup.find(attrs={"class": "infobox-image"})
        if article_image_tag != None:
            article_content["image"] = "https:"+article_image_tag.span.a.img["src"]

        #FALTARIA: Parsear cada una de las secciones y luego imagenes

        return article_content