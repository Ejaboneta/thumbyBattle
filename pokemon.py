from thumbyGrayscale import Sprite
from moves import get_move

class Pokemon:
    def __init__(self, pdata):
        self.name = pdata["name"]
        self.frontPic = Sprite(30,30,pdata["frontPic"],0,0)
        self.backPic = Sprite(30,30,pdata["backPic"],0,0)
        self.type = pdata["type"]
        self.hp = pdata["hp"]
        self.max_hp = pdata["hp"]
        self.hp_bar = int(self.hp / self.max_hp * 30)
        self.speed = pdata["speed"]
        self.attack = pdata["attack"]
        self.defense = pdata["defense"]
        self.spAttack = pdata["spAttack"]
        self.spDefense = pdata["spDefense"]
        self.moves = [get_move(move_id) for move_id in pdata["moves"] if get_move(move_id)]
        
    def set_hp(self, hp):
        self.hp = hp
        self.hp_bar = int(self.hp / self.max_hp * 30)


def get_pokemon(pokemon_id):
    for pdata in all_pokemon:
        if pdata["id"] == pokemon_id:
            return Pokemon(pdata)
    return None

all_pokemon = [
    {
        "id": 0,
        "name": "MissingNo.",
        "type": ["Normal"],
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "spDefense": 100,
        "spAttack": 100,
        "speed": 100,
        "moves": [1,2,3,4],
        "frontPic": (
            bytearray([255,255,255,255,10,255,219,207,216,108,63,31,12,138,203,
                223,223,223,223,19,239,62,46,42,254,171,171,130,194,175,
                175,228,172,4,160,228,11,174,172,132,1,221,29,31,223,
                13,13,21,21,29,45,17,62,58,22,30,38,2,20,19]),
            bytearray([0,0,0,0,168,146,179,160,163,139,202,172,191,39,164,
                224,224,224,32,242,39,196,78,74,162,48,0,190,190,154,
                16,210,18,243,55,18,180,21,149,181,188,0,252,48,27,
                50,51,43,47,63,62,44,1,27,27,6,29,57,0,40]),
        ),
        "backPic": (
            bytearray([255,255,255,255,10,255,219,207,216,108,63,31,12,138,203,
                223,223,223,223,19,239,62,46,42,254,171,171,130,194,175,
                175,228,172,4,160,228,11,174,172,132,1,221,29,31,223,
                13,13,21,21,29,45,17,62,58,22,30,38,2,20,19]),
            bytearray([0,0,0,0,168,146,179,160,163,139,202,172,191,39,164,
                224,224,224,32,242,39,196,78,74,162,48,0,190,190,154,
                16,210,18,243,55,18,180,21,149,181,188,0,252,48,27,
                50,51,43,47,63,62,44,1,27,27,6,29,57,0,40])
        ),
    },
    # {"id": 1, "name": "Bulbasaur", "type": ["Grass","Poison"], "hp": 45, "attack": 49, "defense": 49, "spDefense": 49, "spAttack": 49, "speed": 49, "moves": [4,5,6,7]},
    # {"id": 2, "name": "Ivysaur", "type": ["Grass", "Poison"], "hp": 60, "attack": 62, "defense": 63, "spDefense": 80, "spAttack": 80, "speed": 60, "moves": [4,5,6,7]},
    # {"id": 3, "name": "Venusaur", "type": ["Grass", "Poison"], "hp": 80, "attack": 82, "defense": 83, "spDefense": 100, "spAttack": 100, "speed": 80, "moves": [4,5,6,7]},
    # {"id": 4, "name": "Charmander", "type": ["Fire"], "hp": 39, "attack": 52, "defense": 43, "spDefense": 50, "spAttack": 60, "speed": 65, "moves": [4,5,6,7]},
    # {"id": 5, "name": "Charmeleon", "type": ["Fire"], "hp": 58, "attack": 64, "defense": 58, "spDefense": 65, "spAttack": 80, "speed": 80, "moves": [4,5,6,7]},
    # {"id": 6, "name": "Charizard", "type": ["Fire", "Flying"], "hp": 78, "attack": 84, "defense": 78, "spDefense": 85, "spAttack": 109, "speed": 100, "moves": [4,5,6,7]},
    # {"id": 7, "name": "Squirtle", "type": ["Water"], "hp": 44, "attack": 48, "defense": 65, "spDefense": 50, "spAttack": 50, "speed": 43, "moves": [4,5,6,7]},
    # {"id": 8, "name": "Wartortle", "type": ["Water"], "hp": 59, "attack": 63, "defense": 80, "spDefense": 65, "spAttack": 65, "speed": 58, "moves": [4,5,6,7]},
    # {"id": 9, "name": "Blastoise", "type": ["Water"], "hp": 79, "attack": 83, "defense": 100, "spDefense": 85, "spAttack": 85, "speed": 78, "moves": [4,5,6,7]},
    # {"id": 10, "name": "Caterpie", "type": ["Bug"], "hp": 45, "attack": 30, "defense": 35, "spDefense": 20, "spAttack": 20, "speed": 45, "moves": [4,5,6,7]},
    # {"id": 11, "name": "Metapod", "type": ["Bug"], "hp": 50, "attack": 20, "defense": 55, "spDefense": 25, "spAttack": 25, "speed": 30, "moves": [4,5,6,7]},
    # {"id": 12, "name": "Butterfree", "type": ["Bug", "Flying"], "hp": 60, "attack": 45, "defense": 50, "spDefense": 80, "spAttack": 90, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 13, "name": "Weedle", "type": ["Bug", "Poison"], "hp": 40, "attack": 35, "defense": 30, "spDefense": 20, "spAttack": 20, "speed": 50, "moves": [4,5,6,7]},
    # {"id": 14, "name": "Kakuna", "type": ["Bug", "Poison"], "hp": 45, "attack": 25, "defense": 50, "spDefense": 25, "spAttack": 25, "speed": 35, "moves": [4,5,6,7]},
    # {"id": 15, "name": "Beedrill", "type": ["Bug", "Poison"], "hp": 65, "attack": 90, "defense": 40, "spDefense": 80, "spAttack": 45, "speed": 75, "moves": [4,5,6,7]},
    # {"id": 16, "name": "Pidgey", "type": ["Normal", "Flying"], "hp": 40, "attack": 45, "defense": 40, "spDefense": 35, "spAttack": 35, "speed": 56, "moves": [4,5,6,7]},
    # {"id": 17, "name": "Pidgeotto", "type": ["Normal", "Flying"], "hp": 63, "attack": 60, "defense": 55, "spDefense": 50, "spAttack": 50, "speed": 71, "moves": [4,5,6,7]},
    # {"id": 18, "name": "Pidgeot", "type": ["Normal", "Flying"], "hp": 83, "attack": 80, "defense": 75, "spDefense": 70, "spAttack": 70, "speed": 101, "moves": [4,5,6,7]},
    # {"id": 19, "name": "Rattata", "type": ["Normal"], "hp": 30, "attack": 56, "defense": 35, "spDefense": 25, "spAttack": 35, "speed": 72, "moves": [4,5,6,7]},
    # {"id": 20, "name": "Raticate", "type": ["Normal"], "hp": 55, "attack": 81, "defense": 60, "spDefense": 50, "spAttack": 70, "speed": 97, "moves": [4,5,6,7]},
    # {"id": 21, "name": "Spearow", "type": ["Normal", "Flying"], "hp": 40, "attack": 60, "defense": 30, "spDefense": 31, "spAttack": 31, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 22, "name": "Fearow", "type": ["Normal", "Flying"], "hp": 65, "attack": 90, "defense": 65, "spDefense": 61, "spAttack": 61, "speed": 100, "moves": [4,5,6,7]},
    # {"id": 23, "name": "Ekans", "type": ["Poison"], "hp": 35, "attack": 60, "defense": 44, "spDefense": 40, "spAttack": 54, "speed": 55, "moves": [4,5,6,7]},
    # {"id": 24, "name": "Arbok", "type": ["Poison"], "hp": 60, "attack": 85, "defense": 69, "spDefense": 65, "spAttack": 79, "speed": 80, "moves": [4,5,6,7]},
    {
        "id": 25, 
        "name": "Pikachu", 
        "type": ["Electric"], 
        "hp": 35, 
        "attack": 55, 
        "defense": 40, 
        "spDefense": 50, 
        "spAttack": 50,
        "speed": 90, 
        "moves": [5,6,7,8],
        "frontPic": bytearray([255,255,255,255,255,143,15,15,31,31,159,191,191,63,127,127,255,255,255,255,255,63,143,231,243,1,240,255,255,255,
           255,63,143,239,239,231,247,7,126,252,61,139,227,251,255,254,252,253,253,253,252,254,255,39,3,120,255,255,255,255,
           255,252,241,135,63,255,255,255,96,121,252,225,15,15,15,15,15,159,159,191,255,255,249,240,216,166,127,63,63,255,
           63,63,63,63,60,61,61,32,2,48,39,7,12,1,35,35,35,51,51,63,63,63,63,63,31,3,59,59,58,56]),
        "backPic": bytearray([255,255,255,255,255,143,15,15,31,31,159,191,191,63,127,127,255,255,255,255,255,63,143,231,243,1,240,255,255,255,
           255,63,143,239,239,231,247,7,126,252,61,139,227,251,255,254,252,253,253,253,252,254,255,39,3,120,255,255,255,255,
           255,252,241,135,63,255,255,255,96,121,252,225,15,15,15,15,15,159,159,191,255,255,249,240,216,166,127,63,63,255,
           63,63,63,63,60,61,61,32,2,48,39,7,12,1,35,35,35,51,51,63,63,63,63,63,31,3,59,59,58,56])
    },
    # {"id": 26, "name": "Raichu", "type": ["Electric"], "hp": 60, "attack": 90, "defense": 55, "spDefense": 70, "spAttack": 90, "speed": 110, "moves": [4,5,6,7]},
    # {"id": 27, "name": "Sandshrew", "type": ["Ground"], "hp": 50, "attack": 75, "defense": 85, "spDefense": 30, "spAttack": 30, "speed": 40, "moves": [4,5,6,7]},
    # {"id": 28, "name": "Sandslash", "type": ["Ground"], "hp": 75, "attack": 100, "defense": 110, "spDefense": 55, "spAttack": 55, "speed": 65, "moves": [4,5,6,7]},
    # {"id": 29, "name": "Nidoran@", "type": ["Poison"], "hp": 55, "attack": 47, "defense": 52, "spDefense": 40, "spAttack": 40, "speed": 41, "moves": [4,5,6,7]},
    # {"id": 30, "name": "Nidorina", "type": ["Poison"], "hp": 70, "attack": 62, "defense": 67, "spDefense": 55, "spAttack": 55, "speed": 56, "moves": [4,5,6,7]},
    # {"id": 31, "name": "Nidoqueen", "type": ["Poison", "Ground"], "hp": 90, "attack": 92, "defense": 87, "spDefense": 75, "spAttack": 75, "speed": 85, "moves": [4,5,6,7]},
    # {"id": 32, "name": "NidoranB", "type": ["Poison"], "hp": 46, "attack": 57, "defense": 40, "spDefense": 40, "spAttack": 40, "speed": 50, "moves": [4,5,6,7]},
    # {"id": 33, "name": "Nidorino", "type": ["Poison"], "hp": 61, "attack": 72, "defense": 57, "spDefense": 55, "spAttack": 55, "speed": 65, "moves": [4,5,6,7]},
    # {"id": 34, "name": "Nidoking", "type": ["Poison", "Ground"], "hp": 81, "attack": 102, "defense": 77, "spDefense": 75, "spAttack": 75, "speed": 85, "moves": [4,5,6,7]},
    # {"id": 35, "name": "Clefairy", "type": ["Fairy"], "hp": 70, "attack": 45, "defense": 48, "spDefense": 60, "spAttack": 65, "speed": 35, "moves": [4,5,6,7]},
    # {"id": 36, "name": "Clefable", "type": ["Fairy"], "hp": 95, "attack": 70, "defense": 73, "spDefense": 95, "spAttack": 90, "speed": 60, "moves": [4,5,6,7]},
    # {"id": 37, "name": "Vulpix", "type": ["Fire"], "hp": 38, "attack": 41, "defense": 40, "spDefense": 50, "spAttack": 65, "speed": 65, "moves": [4,5,6,7]},
    # {"id": 38, "name": "Ninetales", "type": ["Fire"], "hp": 73, "attack": 76, "defense": 75, "spDefense": 81, "spAttack": 100, "speed": 100, "moves": [4,5,6,7]},
    # {"id": 39, "name": "Jigglypuff", "type": ["Normal", "Fairy"], "hp": 115, "attack": 45, "defense": 20, "spDefense": 25, "spAttack": 45, "speed": 20, "moves": [4,5,6,7]},
    # {"id": 40, "name": "Wigglytuff", "type": ["Normal", "Fairy"], "hp": 140, "attack": 70, "defense": 45, "spDefense": 50, "spAttack": 85, "speed": 45, "moves": [4,5,6,7]},
    # {"id": 41, "name": "Zubat", "type": ["Poison", "Flying"], "hp": 40, "attack": 45, "defense": 35, "spDefense": 40, "spAttack": 40, "speed": 55, "moves": [4,5,6,7]},
    # {"id": 42, "name": "Golbat", "type": ["Poison", "Flying"], "hp": 75, "attack": 80, "defense": 70, "spDefense": 75, "spAttack": 75, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 43, "name": "Oddish", "type": ["Grass", "Poison"], "hp": 45, "attack": 50, "defense": 55, "spDefense": 75, "spAttack": 75, "speed": 30, "moves": [4,5,6,7]},
    # {"id": 44, "name": "Gloom", "type": ["Grass", "Poison"], "hp": 60, "attack": 65, "defense": 70, "spDefense": 85, "spAttack": 85, "speed": 40, "moves": [4,5,6,7]},
    # {"id": 45, "name": "Vileplume", "type": ["Grass", "Poison"], "hp": 75, "attack": 80, "defense": 85, "spDefense": 100, "spAttack": 100, "speed": 50, "moves": [4,5,6,7]},
    # {"id": 46, "name": "Paras", "type": ["Bug", "Grass"], "hp": 35, "attack": 70, "defense": 55, "spDefense": 55, "spAttack": 55, "speed": 25, "moves": [4,5,6,7]},
    # {"id": 47, "name": "Parasect", "type": ["Bug", "Grass"], "hp": 60, "attack": 95, "defense": 80, "spDefense": 80, "spAttack": 80, "speed": 30, "moves": [4,5,6,7]},
    # {"id": 48, "name": "Venonat", "type": ["Bug", "Poison"], "hp": 60, "attack": 55, "defense": 50, "spDefense": 55, "spAttack": 55, "speed": 45, "moves": [4,5,6,7]},
    # {"id": 49, "name": "Venomoth", "type": ["Bug", "Poison"], "hp": 70, "attack": 65, "defense": 60, "spDefense": 90, "spAttack": 90, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 50, "name": "Diglett", "type": ["Ground"], "hp": 10, "attack": 55, "defense": 25, "spDefense": 35, "spAttack": 35, "speed": 95, "moves": [4,5,6,7]},
    # {"id": 51, "name": "Dugtrio", "type": ["Ground"], "hp": 35, "attack": 80, "defense": 50, "spDefense": 70, "spAttack": 70, "speed": 120, "moves": [4,5,6,7]},
    # {"id": 52, "name": "Meowth", "type": ["Normal"], "hp": 40, "attack": 45, "defense": 35, "spDefense": 40, "spAttack": 40, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 53, "name": "Persian", "type": ["Normal"], "hp": 65, "attack": 70, "defense": 60, "spDefense": 65, "spAttack": 65, "speed": 115, "moves": [4,5,6,7]},
    # {"id": 54, "name": "Psyduck", "type": ["Water"], "hp": 50, "attack": 52, "defense": 48, "spDefense": 50, "spAttack": 50, "speed": 55, "moves": [4,5,6,7]},
    # {"id": 55, "name": "Golduck", "type": ["Water"], "hp": 80, "attack": 82, "defense": 78, "spDefense": 80, "spAttack": 80, "speed": 85, "moves": [4,5,6,7]},
    # {"id": 56, "name": "Mankey", "type": ["Fighting"], "hp": 40, "attack": 80, "defense": 35, "spDefense": 35, "spAttack": 35, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 57, "name": "Primeape", "type": ["Fighting"], "hp": 65, "attack": 105, "defense": 60, "spDefense": 60, "spAttack": 60, "speed": 95, "moves": [4,5,6,7]},
    # {"id": 58, "name": "Growlithe", "type": ["Fire"], "hp": 55, "attack": 70, "defense": 45, "spDefense": 50, "spAttack": 50, "speed": 60, "moves": [4,5,6,7]},
    # {"id": 59, "name": "Arcanine", "type": ["Fire"], "hp": 90, "attack": 110, "defense": 80, "spDefense": 80, "spAttack": 80, "speed": 95, "moves": [4,5,6,7]},
    # {"id": 60, "name": "Poliwag", "type": ["Water"], "hp": 40, "attack": 50, "defense": 40, "spDefense": 40, "spAttack": 40, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 61, "name": "Poliwhirl", "type": ["Water"], "hp": 65, "attack": 65, "defense": 65, "spDefense": 50, "spAttack": 50, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 62, "name": "Poliwrath", "type": ["Water", "Fighting"], "hp": 90, "attack": 95, "defense": 95, "spDefense": 70, "spAttack": 70, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 63, "name": "Abra", "type": ["Psychic"], "hp": 25, "attack": 20, "defense": 15, "spDefense": 105, "spAttack": 105, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 64, "name": "Kadabra", "type": ["Psychic"], "hp": 40, "attack": 35, "defense": 30, "spDefense": 120, "spAttack": 120, "speed": 105, "moves": [4,5,6,7]},
    # {"id": 65, "name": "Alakazam", "type": ["Psychic"], "hp": 55, "attack": 50, "defense": 45, "spDefense": 135, "spAttack": 135, "speed": 120, "moves": [4,5,6,7]},
    # {"id": 66, "name": "Machop", "type": ["Fighting"], "hp": 70, "attack": 80, "defense": 50, "spDefense": 35, "spAttack": 35, "speed": 35, "moves": [4,5,6,7]},
    # {"id": 67, "name": "Machoke", "type": ["Fighting"], "hp": 80, "attack": 100, "defense": 70, "spDefense": 50, "spAttack": 50, "speed": 45, "moves": [4,5,6,7]},
    # {"id": 68, "name": "Machamp", "type": ["Fighting"], "hp": 90, "attack": 130, "defense": 80, "spDefense": 65, "spAttack": 65, "speed": 55, "moves": [4,5,6,7]},
    # {"id": 69, "name": "Bellsprout", "type": ["Grass", "Poison"], "hp": 50, "attack": 75, "defense": 35, "spDefense": 70, "spAttack": 70, "speed": 40, "moves": [4,5,6,7]},
    # {"id": 70, "name": "Weepinbell", "type": ["Grass", "Poison"], "hp": 65, "attack": 90, "defense": 50, "spDefense": 85, "spAttack": 85, "speed": 55, "moves": [4,5,6,7]},
    # {"id": 71, "name": "Victreebel", "type": ["Grass", "Poison"], "hp": 80, "attack": 105, "defense": 65, "spDefense": 100, "spAttack": 100, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 72, "name": "Tentacool", "type": ["Water", "Poison"], "hp": 40, "attack": 40, "defense": 35, "spDefense": 100, "spAttack": 100, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 73, "name": "Tentacruel", "type": ["Water", "Poison"], "hp": 80, "attack": 70, "defense": 65, "spDefense": 120, "spAttack": 120, "speed": 100, "moves": [4,5,6,7]},
    # {"id": 74, "name": "Geodude", "type": ["Rock", "Ground"], "hp": 40, "attack": 80, "defense": 100, "spDefense": 30, "spAttack": 30, "speed": 20, "moves": [4,5,6,7]},
    # {"id": 75, "name": "Graveler", "type": ["Rock", "Ground"], "hp": 55, "attack": 95, "defense": 115, "spDefense": 45, "spAttack": 45, "speed": 35, "moves": [4,5,6,7]},
    # {"id": 76, "name": "Golem", "type": ["Rock", "Ground"], "hp": 80, "attack": 120, "defense": 130, "spDefense": 55, "spAttack": 55, "speed": 45, "moves": [4,5,6,7]},
    # {"id": 77, "name": "Ponyta", "type": ["Fire"], "hp": 50, "attack": 85, "defense": 55, "spDefense": 65, "spAttack": 65, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 78, "name": "Rapidash", "type": ["Fire"], "hp": 65, "attack": 100, "defense": 70, "spDefense": 80, "spAttack": 80, "speed": 105, "moves": [4,5,6,7]},
    # {"id": 79, "name": "Slowpoke", "type": ["Water", "Psychic"], "hp": 90, "attack": 65, "defense": 65, "spDefense": 40, "spAttack": 40, "speed": 15, "moves": [4,5,6,7]},
    # {"id": 80, "name": "Slowbro", "type": ["Water", "Psychic"], "hp": 95, "attack": 75, "defense": 110, "spDefense": 80, "spAttack": 80, "speed": 30, "moves": [4,5,6,7]},
    # {"id": 81, "name": "Magnemite", "type": ["Electric", "Steel"], "hp": 25, "attack": 35, "defense": 70, "spDefense": 95, "spAttack": 95, "speed": 45, "moves": [4,5,6,7]},
    # {"id": 82, "name": "Magneton", "type": ["Electric", "Steel"], "hp": 50, "attack": 60, "defense": 95, "spDefense": 120, "spAttack": 120, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 83, "name": "Farfetch'd", "type": ["Normal", "Flying"], "hp": 52, "attack": 65, "defense": 55, "spDefense": 58, "spAttack": 58, "speed": 60, "moves": [4,5,6,7]},
    # {"id": 84, "name": "Doduo", "type": ["Normal", "Flying"], "hp": 35, "attack": 85, "defense": 45, "spDefense": 35, "spAttack": 35, "speed": 75, "moves": [4,5,6,7]},
    # {"id": 85, "name": "Dodrio", "type": ["Normal", "Flying"], "hp": 60, "attack": 110, "defense": 70, "spDefense": 60, "spAttack": 60, "speed": 100, "moves": [4,5,6,7]},
    # {"id": 86, "name": "Seel", "type": ["Water"], "hp": 65, "attack": 45, "defense": 55, "spDefense": 70, "spAttack": 70, "speed": 45, "moves": [4,5,6,7]},
    # {"id": 87, "name": "Dewgong", "type": ["Water", "Ice"], "hp": 90, "attack": 70, "defense": 80, "spDefense": 95, "spAttack": 95, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 88, "name": "Grimer", "type": ["Poison"], "hp": 80, "attack": 80, "defense": 50, "spDefense": 40, "spAttack": 40, "speed": 25, "moves": [4,5,6,7]},
    # {"id": 89, "name": "Muk", "type": ["Poison"], "hp": 105, "attack": 105, "defense": 75, "spDefense": 65, "spAttack": 65, "speed": 50, "moves": [4,5,6,7]},
    # {"id": 90, "name": "Shellder", "type": ["Water"], "hp": 30, "attack": 65, "defense": 100, "spDefense": 45, "spAttack": 45, "speed": 40, "moves": [4,5,6,7]},
    # {"id": 91, "name": "Cloyster", "type": ["Water", "Ice"], "hp": 50, "attack": 95, "defense": 180, "spDefense": 85, "spAttack": 85, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 92, "name": "Gastly", "type": ["Ghost", "Poison"], "hp": 30, "attack": 35, "defense": 30, "spDefense": 100, "spAttack": 100, "speed": 80, "moves": [4,5,6,7]},
    # {"id": 93, "name": "Haunter", "type": ["Ghost", "Poison"], "hp": 45, "attack": 50, "defense": 45, "spDefense": 115, "spAttack": 115, "speed": 95, "moves": [4,5,6,7]},
    # {"id": 94, "name": "Gengar", "type": ["Ghost", "Poison"], "hp": 60, "attack": 65, "defense": 60, "spDefense": 130, "spAttack": 130, "speed": 110, "moves": [4,5,6,7]},
    # {"id": 95, "name": "Onix", "type": ["Rock", "Ground"], "hp": 35, "attack": 45, "defense": 160, "spDefense": 30, "spAttack": 30, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 96, "name": "Drowzee", "type": ["Psychic"], "hp": 60, "attack": 48, "defense": 45, "spDefense": 90, "spAttack": 90, "speed": 42, "moves": [4,5,6,7]},
    # {"id": 97, "name": "Hypno", "type": ["Psychic"], "hp": 85, "attack": 73, "defense": 70, "spDefense": 115, "spAttack": 115, "speed": 67, "moves": [4,5,6,7]},
    # {"id": 98, "name": "Krabby", "type": ["Water"], "hp": 30, "attack": 105, "defense": 90, "spDefense": 25, "spAttack": 25, "speed": 50, "moves": [4,5,6,7]},
    # {"id": 99, "name": "Kingler", "type": ["Water"], "hp": 55, "attack": 130, "defense": 115, "spDefense": 50, "spAttack": 50, "speed": 75, "moves": [4,5,6,7]},
    # {"id": 100, "name": "Voltorb", "type": ["Electric"], "hp": 40, "attack": 30, "defense": 50, "spDefense": 55, "spAttack": 55, "speed": 100, "moves": [4,5,6,7]},
    # {"id": 101, "name": "Electrode", "type": ["Electric"], "hp": 60, "attack": 50, "defense": 70, "spDefense": 80, "spAttack": 80, "speed": 140, "moves": [4,5,6,7]},
    # {"id": 102, "name": "Exeggcute", "type": ["Grass", "Psychic"], "hp": 60, "attack": 40, "defense": 80, "spDefense": 60, "spAttack": 60, "speed": 40, "moves": [4,5,6,7]},
    # {"id": 103, "name": "Exeggutor", "type": ["Grass", "Psychic"], "hp": 95, "attack": 95, "defense": 85, "spDefense": 125, "spAttack": 125, "speed": 55, "moves": [4,5,6,7]},
    # {"id": 104, "name": "Cubone", "type": ["Ground"], "hp": 50, "attack": 50, "defense": 95, "spDefense": 40, "spAttack": 50, "speed": 35, "moves": [4,5,6,7]},
    # {"id": 105, "name": "Marowak", "type": ["Ground"], "hp": 60, "attack": 80, "defense": 110, "spDefense": 50, "spAttack": 80, "speed": 45, "moves": [4,5,6,7]},
    # {"id": 106, "name": "Hitmonlee", "type": ["Fighting"], "hp": 50, "attack": 120, "defense": 53, "spDefense": 110, "spAttack": 35, "speed": 87, "moves": [4,5,6,7]},
    # {"id": 107, "name": "Hitmonchan", "type": ["Fighting"], "hp": 50, "attack": 105, "defense": 79, "spDefense": 110, "spAttack": 35, "speed": 76, "moves": [4,5,6,7]},
    # {"id": 108, "name": "Lickitung", "type": ["Normal"], "hp": 90, "attack": 55, "defense": 75, "spDefense": 60, "spAttack": 60, "speed": 30, "moves": [4,5,6,7]},
    # {"id": 109, "name": "Koffing", "type": ["Poison"], "hp": 40, "attack": 65, "defense": 95, "spDefense": 60, "spAttack": 60, "speed": 35, "moves": [4,5,6,7]},
    # {"id": 110, "name": "Weezing", "type": ["Poison"], "hp": 65, "attack": 90, "defense": 120, "spDefense": 85, "spAttack": 85, "speed": 60, "moves": [4,5,6,7]},
    # {"id": 111, "name": "Rhyhorn", "type": ["Ground", "Rock"], "hp": 80, "attack": 85, "defense": 95, "spDefense": 30, "spAttack": 30, "speed": 25, "moves": [4,5,6,7]},
    # {"id": 112, "name": "Rhydon", "type": ["Ground", "Rock"], "hp": 105, "attack": 130, "defense": 120, "spDefense": 45, "spAttack": 45, "speed": 40, "moves": [4,5,6,7]},
    # {"id": 113, "name": "Chansey", "type": ["Normal"], "hp": 250, "attack": 5, "defense": 5, "spDefense": 105, "spAttack": 35, "speed": 50, "moves": [4,5,6,7]},
    # {"id": 114, "name": "Tangela", "type": ["Grass"], "hp": 65, "attack": 55, "defense": 115, "spDefense": 100, "spAttack": 100, "speed": 60, "moves": [4,5,6,7]},
    # {"id": 115, "name": "Kangaskhan", "type": ["Normal"], "hp": 105, "attack": 95, "defense": 80, "spDefense": 40, "spAttack": 80, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 116, "name": "Horsea", "type": ["Water"], "hp": 30, "attack": 40, "defense": 70, "spDefense": 25, "spAttack": 70, "speed": 60, "moves": [4,5,6,7]},
    # {"id": 117, "name": "Seadra", "type": ["Water"], "hp": 55, "attack": 65, "defense": 95, "spDefense": 45, "spAttack": 95, "speed": 85, "moves": [4,5,6,7]},
    # {"id": 118, "name": "Goldeen", "type": ["Water"], "hp": 45, "attack": 67, "defense": 60, "spDefense": 50, "spAttack": 50, "speed": 63, "moves": [4,5,6,7]},
    # {"id": 119, "name": "Seaking", "type": ["Water"], "hp": 80, "attack": 92, "defense": 65, "spDefense": 80, "spAttack": 80, "speed": 68, "moves": [4,5,6,7]},
    # {"id": 120, "name": "Staryu", "type": ["Water"], "hp": 30, "attack": 45, "defense": 55, "spDefense": 70, "spAttack": 70, "speed": 85, "moves": [4,5,6,7]},
    # {"id": 121, "name": "Starmie", "type": ["Water", "Psychic"], "hp": 60, "attack": 75, "defense": 85, "spDefense": 100, "spAttack": 100, "speed": 115, "moves": [4,5,6,7]},
    # {"id": 122, "name": "Mr. Mime", "type": ["Psychic", "Fairy"], "hp": 40, "attack": 45, "defense": 65, "spDefense": 100, "spAttack": 120, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 123, "name": "Scyther", "type": ["Bug", "Flying"], "hp": 70, "attack": 110, "defense": 80, "spDefense": 80, "spAttack": 55, "speed": 105, "moves": [4,5,6,7]},
    # {"id": 124, "name": "Jynx", "type": ["Ice", "Psychic"], "hp": 65, "attack": 50, "defense": 35, "spDefense": 95, "spAttack": 95, "speed": 95, "moves": [4,5,6,7]},
    # {"id": 125, "name": "Electabuzz", "type": ["Electric"], "hp": 65, "attack": 83, "defense": 57, "spDefense": 85, "spAttack": 95, "speed": 105, "moves": [4,5,6,7]},
    # {"id": 126, "name": "Magmar", "type": ["Fire"], "hp": 65, "attack": 95, "defense": 57, "spDefense": 85, "spAttack": 100, "speed": 93, "moves": [4,5,6,7]},
    # {"id": 127, "name": "Pinsir", "type": ["Bug"], "hp": 65, "attack": 125, "defense": 100, "spDefense": 55, "spAttack": 55, "speed": 85, "moves": [4,5,6,7]},
    # {"id": 128, "name": "Tauros", "type": ["Normal"], "hp": 75, "attack": 100, "defense": 95, "spDefense": 70, "spAttack": 70, "speed": 110, "moves": [4,5,6,7]},
    # {"id": 129, "name": "Magikarp", "type": ["Water"], "hp": 20, "attack": 10, "defense": 55, "spDefense": 20, "spAttack": 15, "speed": 80, "moves": [4,5,6,7]},
    # {"id": 130, "name": "Gyarados", "type": ["Water", "Flying"], "hp": 95, "attack": 125, "defense": 79, "spDefense": 100, "spAttack": 100, "speed": 81, "moves": [4,5,6,7]},
    # {"id": 131, "name": "Lapras", "type": ["Water", "Ice"], "hp": 130, "attack": 85, "defense": 80, "spDefense": 95, "spAttack": 95, "speed": 60, "moves": [4,5,6,7]},
    # {"id": 132, "name": "Ditto", "type": ["Normal"], "hp": 48, "attack": 48, "defense": 48, "spDefense": 48, "spAttack": 48, "speed": 48, "moves": [4,5,6,7]},
    # {"id": 133, "name": "Eevee", "type": ["Normal"], "hp": 55, "attack": 55, "defense": 50, "spDefense": 65, "spAttack": 65, "speed": 55, "moves": [4,5,6,7]},
    # {"id": 134, "name": "Vaporeon", "type": ["Water"], "hp": 130, "attack": 65, "defense": 60, "spDefense": 110, "spAttack": 95, "speed": 65, "moves": [4,5,6,7]},
    # {"id": 135, "name": "Jolteon", "type": ["Electric"], "hp": 65, "attack": 65, "defense": 60, "spDefense": 110, "spAttack": 110, "speed": 130, "moves": [4,5,6,7]},
    # {"id": 136, "name": "Flareon", "type": ["Fire"], "hp": 65, "attack": 130, "defense": 60, "spDefense": 110, "spAttack": 95, "speed": 65, "moves": [4,5,6,7]},
    # {"id": 137, "name": "Porygon", "type": ["Normal"], "hp": 65, "attack": 60, "defense": 70, "spDefense": 75, "spAttack": 85, "speed": 40, "moves": [4,5,6,7]},
    # {"id": 138, "name": "Omanyte", "type": ["Rock", "Water"], "hp": 35, "attack": 40, "defense": 100, "spDefense": 55, "spAttack": 55, "speed": 35, "moves": [4,5,6,7]},
    # {"id": 139, "name": "Omastar", "type": ["Rock", "Water"], "hp": 70, "attack": 60, "defense": 125, "spDefense": 70, "spAttack": 70, "speed": 55, "moves": [4,5,6,7]},
    # {"id": 140, "name": "Kabuto", "type": ["Rock", "Water"], "hp": 30, "attack": 80, "defense": 90, "spDefense": 55, "spAttack": 55, "speed": 45, "moves": [4,5,6,7]},
    # {"id": 141, "name": "Kabutops", "type": ["Rock", "Water"], "hp": 60, "attack": 115, "defense": 105, "spDefense": 65, "spAttack": 70, "speed": 80, "moves": [4,5,6,7]},
    # {"id": 142, "name": "Aerodactyl", "type": ["Rock", "Flying"], "hp": 80, "attack": 105, "defense": 65, "spDefense": 75, "spAttack": 70, "speed": 130, "moves": [4,5,6,7]},
    # {"id": 143, "name": "Snorlax", "type": ["Normal"], "hp": 160, "attack": 110, "defense": 65, "spDefense": 110, "spAttack": 65, "speed": 30, "moves": [4,5,6,7]},
    # {"id": 144, "name": "Articuno", "type": ["Ice", "Flying"], "hp": 90, "attack": 85, "defense": 100, "spDefense": 95, "spAttack": 125, "speed": 85, "moves": [4,5,6,7]},
    # {"id": 145, "name": "Zapdos", "type": ["Electric", "Flying"], "hp": 90, "attack": 90, "defense": 85, "spDefense": 125, "spAttack": 125, "speed": 100, "moves": [4,5,6,7]},
    # {"id": 146, "name": "Moltres", "type": ["Fire", "Flying"], "hp": 90, "attack": 100, "defense": 90, "spDefense": 125, "spAttack": 125, "speed": 90, "moves": [4,5,6,7]},
    # {"id": 147, "name": "Dratini", "type": ["Dragon"], "hp": 41, "attack": 64, "defense": 45, "spDefense": 50, "spAttack": 50, "speed": 50, "moves": [4,5,6,7]},
    # {"id": 148, "name": "Dragonair", "type": ["Dragon"], "hp": 61, "attack": 84, "defense": 65, "spDefense": 70, "spAttack": 70, "speed": 70, "moves": [4,5,6,7]},
    # {"id": 149, "name": "Dragonite", "type": ["Dragon", "Flying"], "hp": 91, "attack": 134, "defense": 95, "spDefense": 100, "spAttack": 100, "speed": 80, "moves": [4,5,6,7]},
    # {"id": 150, "name": "Mewtwo", "type": ["Psychic"], "hp": 106, "attack": 110, "defense": 90, "spDefense": 154, "spAttack": 154, "speed": 130, "moves": [4,5,6,7]},
    {
        "id": 151, 
        "name": "Mew", 
        "type": ["Psychic"], 
        "hp": 100, 
        "attack": 100, 
        "defense": 100, 
        "spDefense": 100, 
        "spAttack": 100, 
        "speed": 10, 
        "moves": [9,10,11,12],
        "frontPic": bytearray([127,63,31,31,31,175,175,215,215,215,219,217,221,205,237,237,245,251,255,255,255,255,255,255,255,255,255,255,255,255,
           248,246,224,40,35,195,248,252,251,251,119,115,251,235,199,31,95,95,63,191,191,63,127,127,255,255,255,255,255,255,
           255,255,255,255,254,248,247,239,239,151,102,23,119,125,252,251,235,203,52,60,188,60,88,36,152,199,255,255,255,255,
           63,63,63,63,63,63,63,63,63,63,60,56,56,60,60,60,48,39,47,48,60,62,63,63,63,63,63,63,63,63]),
        "backPic": bytearray([127,63,31,31,31,175,175,215,215,215,219,217,221,205,237,237,245,251,255,255,255,255,255,255,255,255,255,255,255,255,
           248,246,224,40,35,195,248,252,251,251,119,115,251,235,199,31,95,95,63,191,191,63,127,127,255,255,255,255,255,255,
           255,255,255,255,254,248,247,239,239,151,102,23,119,125,252,251,235,203,52,60,188,60,88,36,152,199,255,255,255,255,
           63,63,63,63,63,63,63,63,63,63,60,56,56,60,60,60,48,39,47,48,60,62,63,63,63,63,63,63,63,63])
        
    },
]