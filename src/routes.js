const router = require('express').Router();
const pokemonDetails = require('./components/pokemonDetails');
const pokemonTypes = require('./components/pokemonTypes');
const pokemonMoves = require('./components/pokemonMoves');
const pokemonAbilities = require('./components/pokemonAbilities');
const POKEAPI_URL = process.env.POKEAPI_URL || "https://pokeapi.co/api/v2";

const Pokemon = require('./models/pokemonModel');

const validateUrl = require('./helpers/validateUrl');

router.get('/', (req, res) => {
    /* The root route provides context for the server */
    res.status(200).send(`Pokemon Battlefield`);
});

router.post('/', async (req, res) => {
    try {
        /* Pokemon names are posted through the root route which then fetches their details from pokeapi.co */
        let pokemon1Name = decodeURI(req.body.pokemon1);
        let pokemon2Name = decodeURI(req.body.pokemon2);
        if (!pokemon1Name || !pokemon2Name) {
            res.status(404).send("<p>Pokemon not found</p>");
        } else {
            let pokemon1Details = await pokemonDetails.getPokemonDetails(pokemon1Name.toLowerCase(), POKEAPI_URL + "/pokemon")
                .then((data) => { return data })
                .catch((e) => console.log(e));
            let pokemon2Details = await pokemonDetails.getPokemonDetails(pokemon2Name.toLowerCase(), POKEAPI_URL + "/pokemon")
                .then((data) => { return data })
                .catch((e) => console.log(e));
            if (pokemon1Details && pokemon2Details) {
                let pokemon1 = new Pokemon(pokemon1Details.id, pokemon1Details.name, pokemon1Details.stats, pokemon1Details.types, pokemon1Details.moves, pokemon1Details.abilities);
                let pokemon2 = new Pokemon(pokemon2Details.id, pokemon2Details.name, pokemon2Details.stats, pokemon2Details.types, pokemon2Details.moves, pokemon2Details.abilities);
                const pokemonDetails = {
                    pokemon1: pokemon1,
                    pokemon2: pokemon2
                };
                res.status(200).send(JSON.stringify(pokemonDetails));
            } else {
                res.status(404).send("<p>Pokemon not found</p>");
            }
        }
    } catch (error) {
        console.error(error);
        res.status(500).send("<p>Internal server error</p>");
    }
});

router.post('/type', async (req, res) => {
    try {
        /* The type route fetches the pokemon type(s) and returns the damage relations names */
        let typeUrl = req.body.url;
        if (!typeUrl) {
            res.status(404).send("<p>Type not found</p>");
        } else {
            let urlValidate = validateUrl(POKEAPI_URL, typeUrl);
            if (urlValidate == 0) {
                res.status(404).send("<p>Type not found</p>");
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
                    res.status(200).send(damageRelations);
                } else {
                    res.status(404).send("<p>Type not found</p>");
                }
            }
        }
    } catch (error) {
        console.error(error);
        res.status(500).send("<p>Internal server error</p>");
    }
});

router.post('/move', async (req, res) => {
    try {
        /* The move route fetches the details of the randomly selected move and sends its power value */
        let moveUrl = req.body.url;
        if (!moveUrl) {
            res.status(404).send("<p>Move not found</p>");
        } else {
            let urlValidate = validateUrl(POKEAPI_URL, moveUrl);
            if (urlValidate == 0) {
                res.status(404).send("<p>Type not found</p>");
            } else {
                let moveDetails = await pokemonMoves.getPokemonMove(moveUrl)
                    .then((data) => { return data })
                    .catch((e) => { console.log(e) })
                if (moveDetails) {
                    res.status(200).send({ 'power': moveDetails.power });
                } else {
                    res.status(404).send("<p>Move not found</p>");
                }
            }
        }
    } catch (error) {
        console.error(error);
        res.status(500).send("<p>Internal server error</p>");
    }
});

router.post('/ability', async (req, res) => {
    try {
        /* The ability route fetches the ability details and sends a short description  */
        let abilityUrl = req.body.url;
        if (!abilityUrl) {
            res.status(404).send("<p>Ability not found</p>");
        } else {
            let urlValidate = validateUrl(POKEAPI_URL, abilityUrl);
            if (urlValidate == 0) {
                res.status(404).send("<p>Type not found</p>");
            } else {

                let abilityDetails = await pokemonAbilities.getPokemonAbilities(abilityUrl)
                    .then((data) => { return data })
                    .catch((e) => { console.log(e) })
                if (abilityDetails) {
                    let abilityDesc = abilityDetails.flavor_text_entries[0].flavor_text;
                    res.status(200).send({ 'ability_desc': abilityDesc });
                } else {
                    res.status(404).send("<p>Ability not found</p>");
                }
            }
        }
    } catch (error) {
        console.error(error);
        res.status(500).send("<p>Internal server error</p>");
    }
});

module.exports = router;