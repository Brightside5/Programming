"""
Exercise 3.1: Fetch and Compare Pokémon Stats (Stub)
- Fetch data for two Pokémon from the PokéAPI.
- Calculate their stats at level 50.
- Compare their base stats (e.g., attack, defense, speed).
"""

import httpx

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def compare_pokemon(pokemon1, pokemon2):
    """Compare the calculated stats of two Pokémon."""
    # TODO: Fetch data for both Pokémon from the PokéAPI
    url1 = f"https://pokeapi.co/api/v2/pokemon/{pokemon1}"
    url2 = f"https://pokeapi.co/api/v2/pokemon/{pokemon2}"
    response1 = httpx.get(url1)
    response2 = httpx.get(url2)
    data1 = response1.json()
    data2 = response2.json()
    # TODO: Extract relevant stats (HP, attack, defense, speed)
    stat1 = {
        'HP': data1['stats'][0]['base_stat'],
        'attack': data1['stats'][1]['base_stat'],
        'defense': data1['stats'][2]['base_stat'],
        'speed': data1['stats'][5]['base_stat']
    }
    
    stat2 = {
        'HP': data2['stats'][0]['base_stat'],
        'attack': data2['stats'][1]['base_stat'],
        'defense': data2['stats'][2]['base_stat'],
        'speed': data2['stats'][5]['base_stat']
    }

    stat150 = {
        'HP': calculate_hp(data1['stats'][0]['base_stat']),
        'attack': calculate_stat(data1['stats'][1]['base_stat']),
        'defense': calculate_stat(data1['stats'][2]['base_stat']),
        'speed': calculate_stat(data1['stats'][5]['base_stat'])
    }
    stat250 = {
        'HP': calculate_hp(data2['stats'][0]['base_stat']),
        'attack': calculate_stat(data2['stats'][1]['base_stat']),
        'defense': calculate_stat(data2['stats'][2]['base_stat']),
        'speed': calculate_stat(data2['stats'][5]['base_stat'])
    }

    
    print(f"Comparing {pokemon1.capitalize()} and {pokemon2.capitalize()}:")
    for stat in ['HP', 'attack', 'defense', 'speed']:
        if stat150[stat] > stat250[stat]:
            print(f"{pokemon1.capitalize()} has higher {stat}: {stat150[stat]} vs {stat250[stat]}")
        elif stat250[stat] > stat150[stat]:
            print(f"{pokemon2.capitalize()} has higher {stat}: {stat250[stat]} vs {stat150[stat]}")
        else:
            print(f"Both have the same {stat}: {stat150[stat]}")

# Example usage
if __name__ == "__main__":
    compare_pokemon("pikachu", "bulbasaur")

"""
Hints:
- Use httpx.get(url) to fetch data for each Pokémon.
- Access base stats using data['stats'] and extract base_stat values.
- Use calculate_stat and calculate_hp to compute level 50 stats.
"""
