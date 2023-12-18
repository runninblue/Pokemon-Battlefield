module.exports = {
    getPokemonAbilities: async (abilityUrl) => {
        let options = { method: "GET" };
        let response = await fetch(abilityUrl, options);
        if (response.status == 200) {
            return response.json();
        } else {
            return null;
        }
    }
}