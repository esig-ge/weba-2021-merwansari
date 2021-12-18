function showPopup(content) {
  document.getElementById("campslist").onchange = function() {
  showPopup("<h4>Popup!</h4>", "pay-popup");
  setTimeout(function() {
    hidePopup(document.getElementById("pay-popup"));
  }, 2000);
}