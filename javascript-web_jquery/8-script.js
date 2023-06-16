$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', data => {
  const movies = data.results;
  const movieTitles = movies.map(movie => `<li>${movie.title}</li>`);
  $('#list_movies').html(movieTitles.join(''));
});