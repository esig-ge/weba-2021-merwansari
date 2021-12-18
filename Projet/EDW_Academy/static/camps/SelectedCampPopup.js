function showPopup(content) {
  document.getElementById("campslist").onchange = function() {
  showPopup("<h4>Popup!</h4>", "pay-popup");
  setTimeout(function() {
    hidePopup(document.getElementById("pay-popup"));
  }, 2000);
}

function hidePopup(content, id) {
  const popup = document.createElement("div");
  popup.className = "pay-popup";
  popup.id = id;
  popup.innerHTML = content;
  document.body.append(popup);
}
