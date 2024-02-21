import random, urllib.parse
from typing import List, Dict

urlstrs = {
    "subdomains": [
        "www","www1","www2","www3","download","freedownload","free","wwww","wxyz"
    ],
    "domains": [
        "download", "freegamedownlaod", "mediafire", "mega", "1linkdownload", "novirusdownload", "dropbox", "microsoft", "gamers", "videogames", "freedownload"
    ],
    "topdomains": [
        "com", "net", "org", "tor", "onion", "cnet", "blog", "website", "download", "gob", "gov", "gay", "game"
    ],
    "extensions": [
        ".exe", ".fastdownloader.exe", ".turbodownloader.exe", ".iso", ".torrent", ".vbs", ".bat", ".downloader.exe"
    ]
}

downloadstrs = {
    "download": [
        "free download", "1 link", "mediafire", "download here now", "no hacks", "no virus", "100% real no fake", "100% safe", "100% secure",
        "no scam", "torrent", "‼‼"
    ]
}

def pick_random_list(l: List[any]) -> any:
    lenght = len(l)
    item = l[random.randint(0, lenght-1)]
    return item

def generate_url(name: str) -> str:
    url = "http://"+pick_random_list(urlstrs["subdomains"])+"."+pick_random_list(urlstrs["domains"])+"."+pick_random_list(urlstrs["topdomains"])+"/"
    randombits = random.getrandbits(128)
    url += urllib.parse.quote_plus(name)
    url += "%32x" % randombits
    url += pick_random_list(urlstrs["extensions"])
    return url

def generate_string(arr: List[str], min: int, max: int) -> str:
    message = ""
    word_quantity = random.randint(min, max)
    for i in range(1, word_quantity):
        message += pick_random_list(arr) + " "
    return message