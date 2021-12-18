function showPopup(content) {
  document.getElementById("campslist").onchange = function() {
  showPopup("<h4>Popup!</h4>", "informations-popup");
  setTimeout(function() {
    hidePopup(document.getElementById("informations-popup"));
  }, 2000);
}

function hidePopup(content, id) {
  const popup = document.createElement("div");
  popup.className = "informations-popup";
  popup.id = id;
  popup.innerHTML = content;
  document.body.append(popup);
}
