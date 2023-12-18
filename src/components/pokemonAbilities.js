module.exports = {
    getPokemonAbilities: async (abilityUrl) => {
        /* Receives pokemon ability URL and receives its details from pokeapi.co */
        let options = { method: "GET" };
        let response = await fetch(abilityUrl, options);
        if (response.status == 200) {
            return response.json();
        } else {
            return null;
        }
    }
}