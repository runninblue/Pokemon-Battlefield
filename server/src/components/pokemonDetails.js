module.exports = {
    getPokemonDetails: async (pokemonName, POKEAPI_URL) => {
        /* Receives pokemon name and retrieves its details from pokeapi.co */
        const options = { method: "GET" };
        let response = await fetch(POKEAPI_URL + `/${pokemonName.toLowerCase()}`, options);
        if (response.status == 200) {
            return response.json();
        } else {
            return null;
        }
    }
}