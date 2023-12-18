module.exports = {
    getPokemonMove: async (moveUrl) => {
        /* Receives pokemon move URL and retrieves its details from pokeapi.co */
        let options = { method: "GET" };
        let response = await fetch(moveUrl, options);
        if (response.status == 200) {
            return response.json();
        } else {
            return null;
        }
    }
}