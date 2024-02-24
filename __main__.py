from program_modules import videogame_database as vgdb
from program_modules import garbage_strings as gs
from program_modules import html_generator as htmlg
from program_modules import wikipedia_scraper as wks
import sqlite3, os, typing

extremity_coeficient = 20

def make_site():
    if not os.path.exists("./data/"):
        print("El directorio de datos no existe. Descargue de nuevo la aplicacion.")
        input()
        exit()

    print("Eligiendo juego...")

    VideoDB = vgdb.VideogameDatabase() 
    VideoDB.connect()
    VGData = VideoDB.get_random_game()

    print("Scrapeando wikipedia...")

    Scraper = wks.WikipediaScraper()
    article_content: typing.Dict = Scraper.get_article(VGData.name)
    article_content["web_title"] = gs.generate_string(gs.downloadstrs["title"], 1, 2*extremity_coeficient, "") + ".com"
    article_content["page_title"] = "DOWNLOAD %s " % (VGData.name) + gs.generate_string(gs.downloadstrs["download"], 2, 3*extremity_coeficient, " ")
    article_content["description"] = "Download the very popular %s game %s by %s now, for FREE! " % (
        (VGData.genre.lower(), VGData.name, VGData.publisher)
    ) + gs.generate_string(gs.downloadstrs["features"], 1, 2*extremity_coeficient, " ")
    article_content["download_link_text"] = gs.generate_string(gs.downloadstrs["download"], 1, 3*extremity_coeficient, " ")
    article_content["download_link"] = gs.generate_url(VGData.name)

    if (article_content["__error__"] == "1"):
        print("No se pudo scrapear wikipedia.")

    print("Guardando...")

    PageGen = htmlg.HtmlGenerator()
    PageGen.generate_page(article_content)

    print("-----------------------------------")
    print("Pagina generada correctamente.")
    print("Juego usado:", VGData.name)
    print("-----------------------------------")



if __name__ == "__main__":
    make_site()