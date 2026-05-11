(function () {
  function copy(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); resolve(); }
      catch (e) { reject(e); }
      finally { document.body.removeChild(ta); }
    });
  }
  var buttons = document.querySelectorAll('.copy-link');
  for (var i = 0; i < buttons.length; i++) {
    (function (btn) {
      btn.addEventListener('click', function () {
        copy(btn.getAttribute('data-url')).then(function () {
          btn.textContent = btn.getAttribute('data-label-done');
          setTimeout(function () { btn.textContent = btn.getAttribute('data-label-copy'); }, 1500);
        });
      });
    })(buttons[i]);
  }
})();
