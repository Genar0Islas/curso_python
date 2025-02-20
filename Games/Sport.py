"""Clase Sport"""
class Sport:
    def __init__(self, name:str, players:int, league:str):
        self.name = name
        if isinstance(players, int):
            self.players = players
        else:
            self.players = int(players)
        self.league = league

    def __str__(self):
        return f"Sport: {self.name}, Players: {self.players}, League: {self.league}"
    
    def __repr__(self):
        """Metodo para representar la clase como string"""
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')" 

    def to_json(self):
        """Metodo para convertir la clase a un diccionario"""
        return {"name":self.name, "players":self.players, "league":self.league}
    
if __name__ == "__main__":
    s = Sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())
    nfl = Sport("Football", "22", "NFL")
    lmp = Sport("Baseball", 9, "LMP")
    mlb = Sport("Baseball", 9, "MLB")
    lmx = Sport("Soccer", 11, "Liga MX")
    nba = Sport("Basketball", 5, "NBA")
    lista_deportes = [nfl, lmp, mlb, lmx, nba]
    archivo_deportes = "deportes.txt"
    with open(archivo_deportes, "w") as file:
        for deportes in lista_deportes:
            file.write(repr(deportes) + "\n")
    
    sport_list = []
    with open(archivo_deportes, "r") as file:
        for line in file:
            d = eval(line)
            sport_list.append(d)
    print(sport_list)
    print(sport_list[0].to_json())

    #Escribimos el arhivo en formato JSON
    import json
    archivo_json = "deportes.json"
    #convert all sports to JSON format
    sports_json = [sport.to_json() for sport in sport_list]
    #Write the etire list as a single JSNON array
    with open(archivo_json, "w", encoding='utf8') as file:
            json.dump(sports_json, file, indent=4)
    #Leemos el archivo JSON
    sport_list_json = []
