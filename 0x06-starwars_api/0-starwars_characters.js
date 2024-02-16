#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: ./0-starwars_characters.js <Movie ID>');
    process.exit(1);
}

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error fetching data:', error);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error(`Failed to retrieve data. Status Code: ${response.statusCode}`);
        process.exit(1);
    }

    const filmData = JSON.parse(body);
    const charactersList = filmData.characters;

    charactersList.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
        if (error) {
            console.error('Error fetching character data:', error);
            process.exit(1);
        }

        if (response.statusCode !== 200) {
            console.error(`Failed to retrieve character data. Status Code: ${response.statusCode}`);
            process.exit(1);
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
    });
    });
});
