module.exports = {
    getPokemonMove: async (moveUrl) => {
        let options = { method: "GET" };
        let response = await fetch(moveUrl, options);
        if (response.status == 200) {
            return response.json();
        } else {
            return null;
        }
    }
}