// Minimal theme toggle with persistence + system-preference default.
(function () {
  var KEY = "jv-theme";
  var root = document.documentElement;

  function apply(theme) {
    root.setAttribute("data-theme", theme);
    var btn = document.querySelector(".theme-toggle");
    if (btn) btn.textContent = theme === "dark" ? "◑ light" : "◐ dark";
  }

  var saved = localStorage.getItem(KEY);
  var prefersDark = window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches;
  apply(saved || (prefersDark ? "dark" : "light"));

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".theme-toggle")) return;
    var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    localStorage.setItem(KEY, next);
    apply(next);
  });
})();
