function processProperties(properties, desc) {
    let propNameUrls = [];
    for (let prop of properties) {
        let propObj = {};
        propObj[prop[desc]['name']] = prop[desc]['url'];
        propNameUrls.push(propObj);
    }
    return propNameUrls;
}

class Pokemon {
    constructor(id, name, stats, types, moves, abilities) {
        this.id = id;
        this.name = name;
        this.hp = stats[0]['base_stat'];
        this.attack = stats[1]['base_stat'];
        this.defense = stats[2]['base_stat'];
        this.specialAttack = stats[3]['base_stat'];
        this.specialDefense = stats[4]['base_stat'];
        this.speed = stats[5]['base_stat'];
        this.types = processProperties(types, 'type');
        this.moves = processProperties(moves, 'move');
        this.abilities = processProperties(abilities, 'ability');
    }
}
module.exports = Pokemon;