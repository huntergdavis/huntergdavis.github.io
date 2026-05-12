---
layout: page
title: Archive
permalink: /archive/
---
{% include jsonld_archive_index.html %}
{% assign by_year = site.posts | group_by_exp: "p", "p.date | date: '%Y'" %}
{% for yr in by_year %}
## [{{ yr.name }}](/archive/{{ yr.name }}/) {#{{ yr.name }}}

{% for post in yr.items %}- {{ post.date | date: "%b %-d" }} — [{{ post.title | escape }}]({{ post.url }})
{% endfor %}
{% endfor %}
