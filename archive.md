---
layout: page
title: Archive
permalink: /archive/
---

{% assign by_year = site.posts | group_by_exp: "p", "p.date | date: '%Y'" %}
{% for yr in by_year %}
## {{ yr.name }} {#{{ yr.name }}}

{% for post in yr.items %}- {{ post.date | date: "%b %-d" }} — [{{ post.title | escape }}]({{ post.url }})
{% endfor %}
{% endfor %}
