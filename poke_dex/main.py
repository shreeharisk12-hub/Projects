import requests
base_url = "https://pokeapi.co/api/v2/"
def poke_info(name):
    url = f"{base_url}pokemon/{name}"
    data = requests.get(url)
    if data.status_code == 200:
        information = data.json()
        return information
    else:
        print(f"Couldn't retrieve the data {data.status_code}")

pokemon_name = input("Enter the name of the pokemon you want to know about: ")
pokemon_data = poke_info(pokemon_name)
print(f"Name : {pokemon_data["name"]}")
print(f"Weight : {pokemon_data["weight"]}")
print(f"height : {pokemon_data["height"]}")
print(f"base_experience : {pokemon_data["base_experience"]}")
print(f"id : {pokemon_data["id"]}")

