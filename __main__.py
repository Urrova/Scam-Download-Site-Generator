#!/usr/bin/env python
from modules import videogame_database as vgdb
from modules import garbage_strings as gs
from modules import html_tools as htmlt
from modules import wikipedia_scraper as wks
from modules import gui
from modules import utils

import sqlite3, sys, os, typing, webbrowser, math


def make_site(extremity_coeficient: int):
    if not os.path.exists("./data/"):
        return 1 #Fail 1: NO DATA
    
    print("Eligiendo juego...")

    #Elige un juego random de la base de datos
    VideoDB = vgdb.VideogameDatabase() 
    VideoDB.connect()
    VGData = VideoDB.get_random_game()
    VideoDB.close_connection()

    print("Scrapeando wikipedia...")

    #Scrapea wikipedia
    Scraper = wks.WikipediaScraper()
    article_content: typing.Dict = Scraper.get_article(VGData.name)

    #Prepara datos para completar la pagina web
    article_content["web_title"] = gs.generate_string(gs.downloadstrs["title"], 1, 2*extremity_coeficient, "") + ".com"
    article_content["page_title"] = "DOWNLOAD %s " % (VGData.name) + gs.generate_string(gs.downloadstrs["download"], 2, 3*extremity_coeficient, " ")
    article_content["description"] = "Download the very popular %s game %s by %s now, for FREE! " % (
        (VGData.genre.lower(), VGData.name, VGData.publisher)
    ) + gs.generate_string(gs.downloadstrs["features"], 1, 2*extremity_coeficient, " ")
    article_content["download_link_text"] = gs.generate_string(gs.downloadstrs["download"], 1, 2*extremity_coeficient, " ")
    article_content["download_link"] = gs.generate_url(VGData.name)

    gifs = os.listdir("./data/img/web")
    randomgif = utils.pick_random_list(gifs)
    article_content["download_image"] = htmlt.image_to_img_base64("./data/img/web/"+randomgif, "gif", "class='smallimage'")

    article_content["c_page_background_color"] = utils.pick_random_list(gs.webstuff["colors"]["background"])
    article_content["c_article_background_color"] = utils.pick_random_list(gs.webstuff["colors"]["article_background"])

    article_content["font_face"] = utils.pick_random_list(gs.webstuff["fonts"])

    print("Guardando...")

    #Finalmente genera la pagina
    PageGen = htmlt.HtmlGenerator()
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