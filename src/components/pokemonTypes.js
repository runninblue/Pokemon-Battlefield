module.exports = {
    getPokemonTypes: async (typeURL) => {
        /* Receives pokemon type URL and retrieves its details from pokeapi.co */
        let options = { method: "GET" };
        let response = await fetch(typeURL, options);
        if (response.status == 200) {
            return response.json();
        } else {
            return null;
        }
    }
}