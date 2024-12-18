---
layout: page
title: Search Results
---
<!-- List where search results will be rendered -->
<button id="sort-by-date-button" class="action-button">Sort by date</button>
<button id="sort-by-relevance-button" class="action-button">Sort by Relevance</button>
<ul id="search-results"></ul>

<script>
  // Template to generate the JSON to search
  window.store = {
    {% for post in site.posts %}
      "{{ post.url | slugify }}": {
        "title": "{{ post.title | xml_escape }}",
        "author": "{{ post.author | xml_escape }}",
        "category": "{{ post.category | xml_escape }}",
        "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ post.url | xml_escape }}", 
        "date": "{{ post.date | date_to_long_string | xml_escape }}"
      }
      {% unless forloop.last %},{% endunless %}
    {% endfor %}
  };
</script>

<!-- Import lunr.js from unpkg.com -->
<script src="/js/lunr232.js"></script>
<!-- Custom search script thanks https://www.stephanmiller.com/static-site-search/ -->
<script src="/js/search.js"></script>

<script>
    document.getElementById('sort-by-date-button').addEventListener('click', function() {
        dateSearchIsGo();
    });
    document.getElementById('sort-by-relevance-button').addEventListener('click', function() {
        searchIsGo();
    });
</script>
