const express = require('express');
const pokemonDetails = require('./components/pokemonDetails');
const pokemonTypes = require('./components/pokemonTypes');
const pokemonMoves = require('./components/pokemonMoves');
const pokemonAbilities = require('./components/pokemonAbilities');
const app = express();
const PORT = 5000;

/* Initializing express app */
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    /* The root route provides context for the server */
    res.send(` Pokemon Battlefield`);
});

app.post('/', async (req, res) => {
    /* Pokemon names are posted through the root route which then fetches their details from pokeapi.co */
    params = req.body;
    if (!params.pokemon1 || !params.pokemon2) {
        res.status(404).send("<p>Not found</p>");
    } else {
        const pokemon1 = decodeURI(params.pokemon1);
        const pokemon2 = decodeURI(params.pokemon2);
        let pokemon1Details = await pokemonDetails.getPokemonDetails(pokemon1)
            .then((data) => { return data })
            .catch((e) => console.log(e));
        let pokemon2Details = await pokemonDetails.getPokemonDetails(pokemon2)
            .then((data) => { return data })
            .catch((e) => console.log(e));
        if (pokemon1Details && pokemon2Details) {
            const pokemonDetails = {
                pokemon1: pokemon1Details,
                pokemon2: pokemon2Details
            };    
            res.send(pokemonDetails);
        } else {
            res.status(404).send("<p>Not found</p>");
        }
    }
});

app.post('/type', async(req, res) => {
    /* The type route fetches the pokemon type(s) and returns the damage relations names */
    let typeUrl = req.body.url;
    if (!typeUrl) {
        res.status(404).send("<p>Not found</p>");
    } else {
        let typeDetails = await pokemonTypes.getPokemonTypes(typeUrl)
            .then((data) => { return data })
            .catch((e) => { console.log(e) })
        if (typeDetails) {
            let damageRelations = typeDetails.damage_relations;
            for (let damage in damageRelations) {
                let relationNames = [];
                for (let relation in damageRelations[damage]) {
                    relationNames.push(damageRelations[damage][relation].name);
                }
                damageRelations[damage] = relationNames;
            }
            res.send(damageRelations);
        } else {
            res.status(404).send("<p>Not found</p>");
        }
    }
});

app.post('/move', async(req, res) => {
    /* The move route fetches the details of the randomly selected move and sends its power value */
    let moveUrl = req.body.url;
    if (!moveUrl) {
        res.status(404).send("<p>Not found</p>");
    } else {
        let moveDetails = await pokemonMoves.getPokemonMove(moveUrl)
            .then((data) => { return data })
            .catch((e) => { console.log(e) })
        if (moveDetails) {
            res.send({ 'power' : moveDetails.power });
        } else {
            res.status(404).send("<p>Not found</p>");
        }
    }
});

app.post('/ability', async(req, res) => {
    /* The ability route fetches the ability details and sends a short description  */
    let abilityUrl = req.body.url;
    if (!abilityUrl) {
        res.status(404).send("<p>Not found</p>");
    } else {
        let abilityDetails = await pokemonAbilities.getPokemonAbilities(abilityUrl)
            .then((data) => { return data })
            .catch((e) => { console.log(e) })
        if (abilityDetails) {
            let abilityDesc = abilityDetails.flavor_text_entries[0].flavor_text;
            res.send({ 'ability_desc' : abilityDesc });
        } else {
            res.status(404).send("<p>Not found</p>");
        }
    }
});

app.listen(PORT, () => {
    /* Server initialization */
    console.log(`Server running on port ${PORT}`);
});