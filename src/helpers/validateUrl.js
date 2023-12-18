function validateUrl(POKEAPI_URL, url) {
    if (url.toLowerCase().includes(POKEAPI_URL.toLowerCase())) {
        return 1;
    } else {
        return 0;
    }
}
module.exports = validateUrl;