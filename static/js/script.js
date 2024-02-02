function toggleTheme() {
  let theme = document.body.getAttribute("data-bs-theme");
  let _theme = theme == "dark" ? "light" : "dark";
  document.body.setAttribute("data-bs-theme", _theme);
  localStorage.setItem("theme", _theme);
}

document.addEventListener("DOMContentLoaded", function () {
  let theme = document.body.getAttribute("data-bs-theme");
  let _theme = localStorage.getItem("theme");
  if (theme != _theme) toggleTheme();
});
