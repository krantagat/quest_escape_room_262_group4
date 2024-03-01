# define level and food
# level:
#     level_0[no_food+tunnel_a]--Kranta
#     level_1[4_food+tunnel_b--Kranta
#     level2[4_food+tunnel_c]--Michael
#     level3[4_food+tunnel_dragon]--Reda
#     dragon[4_food+dragon]--Xiaobo

# food:
#   toxic_food*1,key_food*1,eatable_food*2

# import urllib.request 
from PIL import Image 

# LEVEL 1 Definition
mushroom = {
    "name": "mushroom",
    "type": "toxic_food"}
cabbage = {
    "name": "cabbage",
    "type": "key_food",
    "target": "tunnel a"}
apple = {
    "name": "apple",
    "type": "eatable_food"
}
carrot = {
    "name": "carrot",
    "type": "eatable_food"
}
# LEVEL 2 DEFINITION
coffee = {
    "name": "coffee",
    "type": "toxic_food"}
salmon = {
    "name": "salmon",
    "type": "key_food",
    "target": "tunnel b"}
chocolate = {
    "name": "apple",
    "type": "eatable_food"
}
flammekueche = {
    "name": "flammekueche",
    "type": "eatable_food"
}  # Just imagine how great a salmon flammekueche is ;)
# LEVEL 3 DEFINITION
turnip = {
    "name": "turnip",
    "type": "toxic_food"
}
watermelon = {
    "name": "watermelon",
    "type": "key_food",
    "target": "tunnel c"
}
banana = {
    "name": "banana",
    "type": "eatable_food"
}
lemon = {
    "name": "carrot",
    "type": "eatable_food"
}
# LEVEL DRAGON DEFINITION - Xiaobo
melted_ice_cream = {
    "name": "melted ice cream",
    "type": "toxic_food"
}
suspicious_cake = {
    "name": "suspicious cake",
    "type": "key_food",
    "target": "dragon"
}
sparkling_water = {
    "name": "sparkling water",
    "type": "eatable_food"
}
monster_meat = {
    "name": "monster meat",
    "type": "eatable_food"
}
# TUNNELS DEFINITION
tunnel_a = {
    "name": "tunnel a",
    "type": "tunnel"
}
tunnel_b = {
    "name": "tunnel b",
    "type": "tunnel"
}
tunnel_c = {
    "name": "tunnel c",
    "type": "tunnel"
}
dragon = {
    "name": "dragon",
    "type": "tunnel"
}
# LEVELS DEFINITION
# level_0 = {
#     "name": "level 0",
#     "type": "outside",
# }
level_1 = {
    'name': "level 1",
    'type': 'level'
}
level_2 = {
    'name': "level 2",
    'type': 'level'
}
level_3 = {
    'name': "level 3",
    'type': 'level'
}
level_dragon = {
    "name": "level dragon",
    "type": "level"
}
# have to rename variable "exit", because exit() exists
exit_to_outside = {
    "name": "exit"
}
all_levels = [level_1, level_2, level_3, level_dragon]  # wonder if we still need level_0 in this list
all_tunnels = [tunnel_a, tunnel_b, tunnel_c, dragon]

# dictionary object_relations = {key=str:value=list}
object_relations = {
    "level 1": [mushroom, cabbage, apple, carrot, tunnel_a],
    "tunnel a": [level_1, level_2],
    "level 2": [coffee, salmon, chocolate, flammekueche, tunnel_a, tunnel_b],
    "tunnel b": [level_2, level_3],
    "level 3": [turnip, watermelon, banana, lemon, tunnel_b, tunnel_c],
    "tunnel c": [level_3, level_dragon],
    "level dragon": [melted_ice_cream, suspicious_cake, sparkling_water, monster_meat, tunnel_c, dragon],
    "exit": [dragon],
    "dragon": [level_dragon, exit_to_outside]
}

INIT_GAME_STATE = {
    "current_level": level_1,
    "key_food_eaten": [],
    "target_level": exit_to_outside
}


def line_break():
    """
    Print a line break
    """
    print("\n")


def start_game():
    print(
        "You woke up on the ground in front of big tunnel and you heard a strange voice talk to you do you want to "
        "enter the tunnel  \n Do you want adventure? ")

    response = str(input("Do you want adventure? (yes/no): ")).lower()

    while response != "yes":
        if response == "no":
            print("Are you sure you don't want to enter???")
            response = str(input("Do you want adventure? (yes/no): ")).lower()
        else:
            print("You can only answer yes or no!")
            response = str(input("Do you want adventure? (yes/no): ")).lower()

    print("welcome to hell!!!")
    play_level(game_state["current_level"])


def play_level(level):  # kranta
    """
    Play a level. First check if the level being played is the target level.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this level) or examine an item found here.
    """
    line_break()
    game_state["current_level"] = level
    if game_state["current_level"] == game_state["target_level"]:
        print("Congrats! You escaped the dungeon !")
        # urllib.request.urlretrieve( 
        # "https://images4.alphacoders.com/134/1348242.jpeg", 
        # "winwin.png") 
        img = Image.open("winwin.png") 
        img.show()

    else:
        print("You are now in " + level["name"])
        intended_action = input("What would you like to do? Type 'A' for looking around' or 'B' for examining'? ").strip()
        if intended_action == "A":
            explore_level(level)
            play_level(level)
        elif intended_action == "B":
            examine_item(input("What would you like to examine? ").strip())
        else:
            print("Not sure what you mean. Type 'A' for looking around' or 'B' for examining. ")
            play_level(level)
        line_break()


# Explore level function:
# Uses the .join() function

def explore_level(level):
    """
    Explore a room. List all items belonging to this room.
    """

    items = [i["name"] for i in object_relations[level["name"]]]
    print("You look around. \n --> This is " + level["name"] + ". You find " + ", ".join(items))


# Go to next level function

def move_to_next_level(tunnel, current_level):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """

    connected_levels = object_relations[tunnel["name"]]

    for level in connected_levels:
        if current_level != level:
            return level


# Examine level function

def examine_item(item_name):
    """
    Examine an item which can be a food or a tunnel.
    First make sure the intended item belongs to the current level.
    Then check if the item is a tunnel. Tell player if key food hasn't been
    eaten yet. Otherwise, ask player if they want to go to the next
    level. If the item is not a tunnel, then, ask player if they want
    to eat it and check if the food is eatable, toxic or a key food.
    At the end, play either the current or the next level depending on the game state
    to keep playing.
    """

    # global food_eaten
    current_level = game_state["current_level"]
    next_level = ""
    output = None
    # check if the item exists in the current level
    if item_name not in [item["name"] for item in object_relations[current_level["name"]]]:
        print("This item doesn't exist in the current level.")
        play_level(current_level)

    for item in object_relations[current_level["name"]]:
        if item["name"] == item_name:
            output = f"You examine {item_name}. "
            if item["type"] == "tunnel":
                have_keyfood = False
                for food in game_state["key_food_eaten"]:
                    if food["target"] == item["name"]:  # TypeError: list indices must be integers or slices, not str
                        have_keyfood = True
                if have_keyfood:
                    output += "You can now enter the next level with the keyfood you've eaten. "
                    next_level = move_to_next_level(item, current_level)
                else:
                    output += "You can't enter yet since you haven't eaten the keyfood."
            else:
                question = input(f"You just found a {item_name}. Would you like to eat it ? Enter 'yes' or 'no' ")
                if question == 'yes':
                    game_state["key_food_eaten"].append(item)
                    object_relations[current_level["name"]].remove(item)  # remove the eaten food
                    if item["type"] == "toxic_food":
                        print("Oh no! you've been poisoned! You died. ")
                        # urllib.request.urlretrieve( 
                        # 'https://www.pngitem.com/pimgs/b/34-343337_toxic-warning-sign-png-clipart-toxic-warning-label.png', 
                        # "toxic.png") 

                        img = Image.open("toxic.png") 
                        img.show()

                        line_break()
                        start_game()
                    elif item["type"] == "key_food":
                        output += f"You ate {item_name}."
                        print("You can now enter the next level with the keyfood you've eaten. ")

                        # urllib.request.urlretrieve( 
                        # 'https://cdn.oneesports.gg/cdn-data/2024/01/Anime_DeliciousinDungeon_KeyArt_1-1024x576.jpg',
                        # "good_food.jpg") 
                        
                        img = Image.open("goodfood.png") 
                        img.show()
                    else:
                        output += f"You ate {item_name}."
                        print("Nothing happened.")
                        line_break()
            print(output)
            break
    if output is None:
        print("You haven't eaten the keyfood yet to enter the next level.")

    if next_level and input("Do you want to go to the next level? Enter 'yes' or 'no' ").strip() == 'yes':
    #     urllib.request.urlretrieve( 
    #    "https://img.freepik.com/photos-premium/image-dessin-anime-tunnel-pierre-sombre-passerelle-pierre-menant-porte-qui-dit-mot-dessus_265515-679.jpg?w=1060","tunnel.jpg") 
        
        img = Image.open("tunnel.jpg") 
        img.show()
        play_level(next_level)
    else:
        play_level(current_level)

    

game_state = INIT_GAME_STATE.copy()
start_game()

