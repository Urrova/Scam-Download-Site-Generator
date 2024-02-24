import random, urllib.parse
from typing import List, Dict

urlstrs = {
    "subdomains": [
        "www","www1","www2","www3","download","freedownload","free","wwww","wxyz", "www69", "www420", "www666", "www1337", "file", "cdn", "downloadfreefreedownloadfreenowfreedownload"
    ],
    "domains": [
        "download", "freegamedownlaod", "mediafire", "mega", "1linkdownload", "novirusdownload", "dropbox", "microsoft", "gamers", "videogames", "freedownload", "ouo"
    ],
    "topdomains": [
        "com", "net", "org", "tor", "onion", "cnet", "blog", "website", "download", "ru", "ai", "gay", "game", "io"
    ],
    "extensions": [
        ".exe", ".fastdownloader.exe", ".turbodownloader.exe", ".iso", ".torrent", ".vbs", ".bat", ".downloader.exe"
    ]
}

downloadstrs = {
    "download": [
        "free download", "1 link", "mediafire", "download here now", "no hacks", "no virus", "100% real", "no fake", "100% safe", "100% secure",
        "no scam", "torrent", "‼‼", "1 RAR", "1 ZIP", "100% FREE", "---->", ">>>>>"
    ],
    "title": [
        "All", "Games", "Download", "Free", "Videogames", "Bay", "Pirate", "Torrent", "TOR", "Kickass", "Downloader", "Library", "GreenSteam", "Site", "Web", "Website", "Z", "X"
    ],
    "features": [
        "Easy Installation!", 
        "Completely free of charge!", 
        "Antivirus checked!",
        "Available for Windows!",
        "Bot free!",
        "Plug and play!",
        "Available for your device!",
        "Easy download!",
        "Completely legal!",
        "Extremely fun!",
        "One of the better games of the year!",
        "On of the best games ever!",
        "Play n' fun!",
        "FUN FUN FUN FUN FUN!",
        "Better with friends!",
        "Multiplayer support!",
        "With AI technology!",
        "DRM-Free!",
        "No Denuvo!"
    ]
}

#Agarra un elemento random de una lista
def pick_random_list(l: List[any]) -> any:
    lenght = len(l)
    item = l[random.randint(0, lenght-1)]
    return item

#Genera una url random
def generate_url(name: str) -> str:
    url = "http://"+pick_random_list(urlstrs["subdomains"])+"."+pick_random_list(urlstrs["domains"])+"."+pick_random_list(urlstrs["topdomains"])+"/"
    randombits = random.getrandbits(128)
    url += urllib.parse.quote_plus(name)
    url += "%32x" % randombits
    url += pick_random_list(urlstrs["extensions"])
    return url

#Genera un string random usando strings de un array
def generate_string(arr: List[str], min: int, max: int, separator: str) -> str:
    message = ""
    word_quantity = random.randint(min, max)
    for i in range(0, word_quantity):
        message += pick_random_list(arr) + separator
    return message