import sqlite3, random

class VideogameData:
    def __init__(self, gameid: int, name: str, genre:str, publisher: str):
        self.gameid: int = gameid
        self.name: str = name
        self.genre: str= genre
        self.publisher: str = publisher

class VideogameDatabase:
    def __init__(self):
        self.connection: sqlite3.Connection = None
        self.cursor: sqlite3.Cursor = None
    
    def connect(self):
        self.connection = sqlite3.connect("./data/databases/videogames.db")
        self.cursor = self.connection.cursor()
    
    def close_connection(self):
        self.connection.close()
        self.cursor = None

    def get_games_quantity(self) -> int:
        games_quantity_table = self.cursor.execute("SELECT COUNT(Id) as count_games FROM game").fetchall()
        games_quantity = games_quantity_table[0][0]
        return games_quantity

    def get_random_game(self) -> VideogameData:
        rand = random.randint(0,self.get_games_quantity()-1)
        VGData = self.get_game(rand)
        return VGData
    
    #Obtiene un juego por ID
    def get_game(self, gameid: int):
        #Encuentra el juego y saca el nombre y el ID del genero
        table = self.cursor.execute("SELECT * FROM game WHERE id=?", (str(gameid), )).fetchall()
        game_genre_id: int = table[0][1]
        game_name: str = table[0][2]

        #Encuentra el nombre del genero
        table = self.cursor.execute("SELECT * FROM genre WHERE id=?", (str(game_genre_id), )).fetchall()
        genre_name: str = table[0][1]

        #Encuentra el ID del publisher y luego al publisher
        table = self.cursor.execute("SELECT * FROM game_publisher WHERE game_id=?", (str(gameid), )).fetchall()
        publisher_id: int = table[0][2]
        table = self.cursor.execute("SELECT * FROM publisher WHERE id=?", (str(publisher_id), )).fetchall()
        publisher_name: str = table[0][1]

        VGData = VideogameData(gameid, game_name, genre_name, publisher_name)

        return VGData