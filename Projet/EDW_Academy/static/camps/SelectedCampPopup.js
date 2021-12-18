
function showPopup(content, id) {
  const popup = document.createElement("div");
  popup.className = "informations-popup";
  popup.id = id;
  popup.innerHTML = content;
  document.body.append(popup);
}

function hidePopup(popup) {
  popup.remove();
}

document.getElementById("campslist").onchange = function() {
  showPopup("<h1>Discover Camps</h1><br><h4> Discover camp's price are always 150 CHF and they are here to make you discover new games. </h4>", "informations-popup");
  setTimeout(function() {
    hidePopup(document.getElementById("informations-popup"));
  }, 4000);
}
