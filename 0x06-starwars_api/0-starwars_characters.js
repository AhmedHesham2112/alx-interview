#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const data = JSON.parse(body);

  const characters = data.characters;

  const printCharacterNames = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.error('Error:', err);
        return;
      }

      const characterData = JSON.parse(charBody);

      console.log(characterData.name);

      printCharacterNames(index + 1);
    });
  };

  printCharacterNames(0);
});
