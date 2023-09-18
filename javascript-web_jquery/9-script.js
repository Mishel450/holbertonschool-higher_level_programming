$(document).ready(function () {
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
    $("#hello").append("<p>" + data.hello + "</p>")
 })
})