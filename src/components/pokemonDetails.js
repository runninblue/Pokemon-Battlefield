module.exports = {
    get_pokemon_details: async (pokemonName) => {
        const pokeapi = 'https://pokeapi.co/api/v2/pokemon';
        let options = { method: "GET" };
        let response = await fetch(pokeapi + `/${pokemonName.toLowerCase()}`, options);
        if (response.status == 200) {
            return response.json();
        } else {
            return null;
        }
    }
}