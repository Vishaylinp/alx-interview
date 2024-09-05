#!/usr/bin/node

const request = require("request")

const movie_id = process.argv[2];
const movie_url = `https://swapi-api.alx-tools.com/api/films/` + movie_id;

function request_sent(character_list, index) {
  if (character_list.length === index) {
    return;
  }

  request(character_list[index], (error, response, body) => {

    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      request_sent(character_list, index + 1);
    }
  });
}

request(movie_url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const character_list = JSON.parse(body).characters;
    request_sent(character_list, 0);
  }
});
