$(document).ready(function () {
  $.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
    const results = data.results
    for (i = 0; i < data.count; i++) {
      the_title = results[i]["title"]
      $("#list_movies").append("<li>" + the_title + "</li>")
    }
 })
})