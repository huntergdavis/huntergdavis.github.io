// Tri-state theme toggle — cycles auto → light → dark → auto.
// Persists choice in localStorage under "theme".
// Applied to <html data-theme="…"> so the dark-mode CSS reacts.
//
// "auto" removes the attribute entirely so prefers-color-scheme wins.
(function () {
  var STATES = ['auto', 'light', 'dark'];
  var LABELS = { auto: 'Theme: auto', light: 'Theme: light', dark: 'Theme: dark' };
  var KEY = 'theme';

  function apply(state) {
    var html = document.documentElement;
    if (state === 'auto') html.removeAttribute('data-theme');
    else html.setAttribute('data-theme', state);
  }

  function next(state) {
    var i = STATES.indexOf(state);
    return STATES[(i + 1) % STATES.length];
  }

  // Restore on load
  var saved = (function () {
    try { return localStorage.getItem(KEY) || 'auto'; }
    catch (e) { return 'auto'; }
  })();
  if (STATES.indexOf(saved) < 0) saved = 'auto';
  apply(saved);

  // Wire the button(s)
  function init() {
    var btns = document.querySelectorAll('.theme-toggle');
    for (var i = 0; i < btns.length; i++) {
      (function (btn) {
        btn.textContent = LABELS[saved];
        btn.setAttribute('aria-label', LABELS[saved]);
        btn.addEventListener('click', function () {
          saved = next(saved);
          apply(saved);
          try { localStorage.setItem(KEY, saved); } catch (e) {}
          btn.textContent = LABELS[saved];
          btn.setAttribute('aria-label', LABELS[saved]);
        });
      })(btns[i]);
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
