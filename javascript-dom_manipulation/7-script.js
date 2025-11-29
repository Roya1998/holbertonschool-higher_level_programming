// Fetch movies data from the Star Wars API
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => response.json())
  .then((data) => {
    // Get the ul element with id 'list_movies'
    const listMovies = document.querySelector("#list_movies");

    // Loop through each movie in the results array
    data.results.forEach((movie) => {
      // Create a new li element for each movie
      const listItem = document.createElement("li");
      listItem.textContent = movie.title;

      // Add the li element to the ul
      listMovies.appendChild(listItem);
    });
  })
  .catch((error) => {
    console.error("Error fetching movies:", error);
  });
