import requests
from django.shortcuts import render

def pokemon_view(request):
    pokemon_data = None
    error = None

    if request.method == "POST":
        pokemon_name = request.POST.get("pokemon_name", "").lower().strip()
        if pokemon_name:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    pokemon_data = response.json()
                else:
                    error = f"Pokémon '{pokemon_name}' não encontrado."
            except requests.exceptions.RequestException as e:
                error = f"Ocorreu um erro ao acessar a PokeAPI: {str(e)}"
        else:
            error = "Por favor, insira o nome de um Pokémon."

    return render(request, "pokemon/pokemon.html", {"pokemon_data": pokemon_data, "error": error})
