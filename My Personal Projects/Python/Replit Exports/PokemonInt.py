import random

# Define some basic Pokémon and their stats
pokemon_data = {
    "Pikachu": {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90},
    "Charmander": {"HP": 39, "Attack": 52, "Defense": 43, "Speed": 65},
    "Squirtle": {"HP": 44, "Attack": 48, "Defense": 65, "Speed": 43},
}

# Player and enemy Pokémon
player_pokemon = None
enemy_pokemon = None

def select_starter_pokemon():
    global player_pokemon
    print("Choose your starter Pokemon:")
    for pokemon in pokemon_data.keys():
        print(pokemon)
    choice = input()
    if choice in pokemon_data:
        player_pokemon = {"name": choice, **pokemon_data[choice]}
        print(f"You chose {choice}!")
    else:
        print("Invalid choice. Try again.")
        select_starter_pokemon()

def select_enemy_pokemon():
    global enemy_pokemon
    enemy_pokemon = random.choice(list(pokemon_data.keys()))

def battle():
    print("A wild", enemy_pokemon, "appeared!")
    while player_pokemon["HP"] > 0 and enemy_pokemon:
        print(f"{player_pokemon['name']} (HP: {player_pokemon['HP']}) vs. {enemy_pokemon} (HP: {pokemon_data[enemy_pokemon]['HP']})")
        action = input("What will you do? (1. Attack, 2. Run): ")
        if action == "1":
            player_attack = player_pokemon["Attack"]
            enemy_defense = pokemon_data[enemy_pokemon]["Defense"]
            damage = max(player_attack - enemy_defense, 0)
            enemy_hp = pokemon_data[enemy_pokemon]["HP"]
            enemy_hp -= damage
            print(f"{player_pokemon['name']} attacked {enemy_pokemon} for {damage} damage!")
            pokemon_data[enemy_pokemon]["HP"] = enemy_hp
            if enemy_hp <= 0:
                print(f"You defeated {enemy_pokemon}!")
                select_enemy_pokemon()
        elif action == "2":
            print(f"{player_pokemon['name']} ran away!")
            break
        else:
            print("Invalid choice. Try again.")

    if player_pokemon["HP"] <= 0:
        print(f"{player_pokemon['name']} fainted. Game over!")

select_starter_pokemon()
select_enemy_pokemon()
battle()