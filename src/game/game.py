
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import Axes3D
from enum import Enum


# In[10]:


SUSPECTS = ['Miss Scarlett', 'Professor Plum', 'Mrs. Peacock', 'Mr. Green', 'Colonel Mustard', 'Mrs. White']
WEAPONS = ['Candlestick', 'Knife', 'Lead Pipe', 'Revolver', 'Rope', 'Wrench']
ROOMS = ['Kitchen','Ballroom', 'Conservatory','Dining Room','Lounge','Hall','Study','Library','Billiard Room' ]
    
class Suspect(Enum):
    MS_SCARLETT = 0
    PROFESSOR_PLUM = 1
    MRS_PEACOCK = 2
    MR_GREEN = 3
    COLONEL_MUSTARD = 4
    MRS_WHITE = 5 

    def __str__(self):
        return SUSPECTS[self.value] 

class Weapon(Enum):
    CANDLESTICK = 0
    KNIFE = 1
    LEAD_PIPE = 2
    REVOLVER = 3
    ROPE = 4
    WRENCH = 5

    def __str__(self):
        return WEAPONS[self.value]

class Room(Enum):
    KITCHEN = 0
    BALLROOM = 1
    CONSERVATORY = 2
    DINING_ROOM = 3
    LOUNGE = 4
    HALL = 5
    STUDY = 6
    LIBRARY = 7
    BILLARD_ROOM = 8
    def __str__(self):
        return ROOMS[self.value]

class Game(object):

    
    
    def __init__(self): 
        self.suspect_map = {}    
        self.weapons_map = {}
        self.rooms_map = {}
        self.possible_combinations = None
        self.reset_combinations()

    def reset_combinations(self): 
        # suspects, weapons, room
        self.possible_combinations = np.full((len(SUSPECTS),len(WEAPONS),len(ROOMS)), True, dtype=bool) 
        
    def get_all_combinations(self):
        return self.possible_combinations
    
    def print_all_combinations(self):
        for suspect in Suspect:
            for weapon in Weapon:
                for room in Room:    
                    suspect_index = suspect.value
                    weapon_index = weapon.value
                    room_index = room.value
                    this_row = self.possible_combinations[suspect_index][weapon_index][room_index]
                    print(f"For suspect: {suspect} {weapon} {room} = {suspect_index} {weapon_index} {room_index}: {this_row}")

    def print_possible_combinations(self):
        for suspect in Suspect:
            for weapon in Weapon:
                for room in Room:    
                    suspect_index = suspect.value
                    weapon_index = weapon.value
                    room_index = room.value

                    this_row = self.possible_combinations[suspect_index][weapon_index][room_index]
                    if this_row:
                        print(f"For suspect: {suspect} {weapon} {room} = {suspect_index} {weapon_index} {room_index}: {this_row}")
    def seen_suspect(self, suspect):
        suspect_index = suspect.value
        self.suspect_map[suspect_index] = True
        suspect_rows = self.possible_combinations[suspect_index]
        for weapon in Weapon:
            for room in Room:
                weapon_index = weapon.value
                room_index = room.value
                suspect_rows[weapon_index][room_index] = False
        return self
    
    def seen_weapon(self, weapon):
        weapon_index = weapon.value
        self.weapons_map[weapon_index] = True
        for suspect in Suspect:
            for room in Room:
                suspect_index = suspect.value
                room_index = room.value
                self.possible_combinations[suspect_index][weapon_index][room_index] = False
        return self
                
    def seen_room(self, room):
        room_index = room.value
        self.rooms_map[room_index] = True    
        print(self.rooms_map)
        for suspect in Suspect:
            for weapon in Weapon:
                suspect_index = suspect.value
                weapon_index = weapon.value
                self.possible_combinations[suspect_index][weapon_index][room_index] = False
        
        return self
    def seen(self, itm):
        if isinstance(itm, Suspect):
            # print("Suspect: ",   itm)
            self.seen_suspect(itm)
        elif isinstance(itm, Weapon):
            # print("Weapon: ",   itm)
            self.seen_weapon(itm)
        elif isinstance(itm, Room):
            # print("Room: ",   itm)
            self.seen_room(itm)
        else:
            print("No idea what type this is: ", type(itm))
    def get_possible_suspects(self):
        possibles = []
        for suspect in Suspect:
            suspect_value = suspect.value
            if not self.suspect_map.get(suspect_value, None):
                possibles.append(str(suspect))
                 
        return possibles

    def get_possible_weapons(self):
        possibles = []
        for weapon in Weapon:
            weapon_value = weapon.value
            if not self.weapons_map.get(weapon_value, None):
                possibles.append(str(weapon))
                     
        return possibles

    def get_possible_rooms(self):
        possibles = []
        for room in Room:
            room_value = room.value
            if not self.rooms_map.get(room_value, None):
                possibles.append(str(room))
                
        return possibles




print(__name__)
if __name__ == "__main__":
    game = Game() 
    game.seen(Suspect.MS_SCARLETT) 
    game.seen(Weapon.KNIFE)
    game.seen(Weapon.LEAD_PIPE)

    game.seen(Room.LIBRARY)
    game.seen(Room.KITCHEN)
    game.seen(Room.BALLROOM)
    game.seen(Room.DINING_ROOM)
    game.seen(Room.LOUNGE)
    game.seen(Room.HALL)
    game.seen(Room.STUDY)
    game.seen(Room.CONSERVATORY)

    print("Suspects: ", game.get_possible_suspects())
    print("Weapons: ", game.get_possible_weapons())
    print("Rooms: ", game.get_possible_rooms())


# In[11]:



possible_combinations = game.get_all_combinations()
max_length = max([len(str(suspect)) for suspect in Suspect])
print(max_length)
print("| ".join([" ".rjust(max_length+1)]+[str(suspect).rjust(max_length) for suspect in Suspect]))
for weapon in game.get_possible_weapons():
   print(weapon.rjust(max_length),"|", end="")
   for suspect in game.get_possible_suspects(): 
       rooms = game.get_possible_rooms() 
       for room in rooms:
           print( str(room).rjust(max_length), end="| ")
   print()
   
           
       

        
           



# In[215]:


reset_combinations()

seen(Weapon.KNIFE)
seen(Room.LIBRARY)
seen(Weapon.LEAD_PIPE)
seen(Room.KITCHEN)
seen(Room.BALLROOM)
seen(Room.DINING_ROOM)
seen(Room.LOUNGE)
seen(Room.HALL)
seen(Room.STUDY)

print("Suspects: ", get_possible_suspects())
print("Weapons: ", get_possible_weapons())
print("Rooms: ", get_possible_rooms())

