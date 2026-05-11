---
layout: page
title: Search Results
---
<form class="search-page-form" action="/search.html" method="get" role="search">
  <label for="search-page-input" class="visually-hidden">Search</label>
  <input type="search" id="search-page-input" name="query" placeholder="Search…" autocomplete="off" autofocus>
  <button type="submit">Search</button>
</form>
<script>
  (function(){
    var params = new URLSearchParams(location.search);
    var q = params.get('query');
    var input = document.getElementById('search-page-input');
    if (input && q) { input.value = q; input.select(); }
  })();
</script>

<!-- List where search results will be rendered -->
<button id="sort-by-date-button" class="action-button">Sort by date</button>
<button id="sort-by-relevance-button" class="action-button">Sort by Relevance</button>
<p id="search-status">Loading search index…</p>
<ul id="search-results"></ul>

<!-- Import lunr.js -->
<script src="/js/lunr232.js"></script>
<!-- Custom search script thanks https://www.stephanmiller.com/static-site-search/ -->
<script src="/js/search.js"></script>

<script>
  fetch('/search.json')
    .then(function (r) { return r.json(); })
    .then(function (store) {
      window.store = store;
      document.getElementById('search-status').style.display = 'none';
      document.getElementById('sort-by-date-button').addEventListener('click', dateSearchIsGo);
      document.getElementById('sort-by-relevance-button').addEventListener('click', searchIsGo);
      if (getQuery('query')) searchIsGo();
    })
    .catch(function () {
      document.getElementById('search-status').textContent = 'Search index failed to load.';
    });
</script>
