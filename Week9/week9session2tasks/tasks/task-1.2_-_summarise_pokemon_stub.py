#Not finished
"""
Exercise 1.2: Summarise Pokémon Details (Stub)
- Fetch Pokémon data from the PokéAPI.
- Extract specific details: name, types, stats, and image URL.
- Display the extracted details in a readable format.
"""

import httpx

def summarise_pokemon(name):
    """Fetch and summarise Pokémon details."""
    # TODO: Construct the URL using the Pokémon name
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    # TODO: Make a GET request to the URL
    response = httpx.get(url)

    # TODO: Check if the response is successful (status_code == 200)
    if response.status_code == 200:
        # TODO: Parse the JSON response
        data = response.json()

        # TODO: Extract the Pokémon's name
        name = data['name']
        # TODO: Extract the Pokémon's types
        types = data['types']

        # TODO: Extract the Pokémon's base stats
        stats = data['stats']

        # TODO: Extract the Pokémon's image URL
        image_url = data['image_url']

        # TODO: Print the details in a readable format
        print(f"Name: {name}")
        print(f"Types: {', '.join(types)}")
        print("Base Stats:")
        for stat, value in stats.items():
            print(f"  {stat.capitalize()}: {value}")
        print(f"Image URL: {image_url}")
    else:
        # TODO: Print an error message if the Pokémon is not found
        print(f"Error: Pokémon '{name}' not found!")

# Example usage
summarise_pokemon("squirtle")

"""
Hints:
- Use data['types'] for the Pokémon’s types.
- Use data['stats'] for the Pokémon’s base stats.
- Use a loop to format and display lists or dictionaries.
"""
