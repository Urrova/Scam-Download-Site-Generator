from program_modules import videogame_database as vgdb
from program_modules import garbage_strings as gs
import sqlite3, os


if __name__ == "__main__":
    if not os.path.exists("./databases/videogames.db"):
        print("La base de datos no existe (./databases/videogames.db). Descargue de nuevo la aplicacion.")
        input()
        exit()

    VideoDB = vgdb.VideogameDatabase()
    VideoDB.connect()
    VGData = VideoDB.get_random_game()
    print(("DOWNLOAD %s " % (VGData.name)) + gs.generate_string(gs.downloadstrs["download"], 3, 10))
    print("Download the very popular %s game %s by %s now, for FREE! Easy installation!" % (
        (VGData.genre.lower(), VGData.name, VGData.publisher)
    ))
    print("DOWNLOAD HERE ---->", gs.generate_url(VGData.name))
    input()