from program_modules import videogame_database as vgdb
from program_modules import garbage_strings as gs
from program_modules import html_generator as htmlg
from program_modules import wikipedia_scraper as wks
from program_modules import gui
import sqlite3, os, typing, webbrowser


def make_site(extremity_coeficient: int):
    if not os.path.exists("./data/"):
        return 1 #Fail 1: NO DATA
    
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

    print("Guardando...")

    PageGen = htmlg.HtmlGenerator()
    PageGen.generate_page(article_content)

    print("-----------------------------------")
    print("Pagina generada correctamente.")
    print("Juego usado:", VGData.name)
    print("-----------------------------------")

    if (article_content["__error__"] == "1"):
        print("No se pudo scrapear wikipedia.")
        return 2 #FAIL 2: NO CONNECTION

    return 0 #Sucess

def open_built_site():
    webbrowser.open("file://"+os.path.realpath("./out/page.html"))

if __name__ == "__main__":
    window = gui.Gui(make_site, open_built_site)
    window.make_main_window()
    window.mainloop()