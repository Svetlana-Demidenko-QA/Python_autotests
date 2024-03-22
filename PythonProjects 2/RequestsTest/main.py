import requests

URL = 'https://api.pokemonbattle.me/'

TOKEN = 'my_token'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body = {
    "name": "Одуванчик",
    "photo": "https://dolnikov.ru/pokemons/albums/256.png"
}

response = requests.post(url = f'{URL}pokemons', headers = HEADERS, json = body)
print(response.text)


body1 = {
    "pokemon_id": "14549",
    "name": "Снежок",
    "photo": "https://dolnikov.ru/pokemons/albums/200.png"
}

response1 = requests.put(url = f'{URL}pokemons', headers = HEADERS, json = body1)
print(response1.text)


body2 ={
    "pokemon_id": "14548"
}

response2 = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADERS, json = body2)
print(response2.text)

