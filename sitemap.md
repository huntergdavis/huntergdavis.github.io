---
layout: page
title: Site Map
permalink: /sitemap.html
---

## Pages

- [Home](/)
- [About](/about.html)
- [Leadership and Public Speaking](/public-speaking.html)
- [Projects](/projects/)
- [Archive](/archive/)
- [Timeline](/timeline/)
- [Tags](/tags/)
- [Search](/search.html)

## Recent posts

{% for post in site.posts limit:10 %}- {{ post.date | date: "%b %-d, %Y" }} — [{{ post.title | escape }}]({{ post.url }})
{% endfor %}

## Posts by project

{% assign projects = site.posts | group_by: "project" | sort: "name" %}
{% for proj in projects %}{% if proj.name and proj.name != "" %}
### {{ site.data.projects[proj.name] | default: proj.name }}

{% for post in proj.items reversed %}- {{ post.date | date: "%b %-d, %Y" }} — [{{ post.title | escape }}]({{ post.url }})
{% endfor %}{% endif %}{% endfor %}

## Posts by year

{% assign years = site.posts | group_by_exp: "p", "p.date | date: '%Y'" %}
{% for year_group in years %}- [**{{ year_group.name }}**](/archive/{{ year_group.name }}/) — {{ year_group.items.size }} posts
{% endfor %}

## Feeds and metadata

- [RSS feed (excerpts)](/feed.xml)
- [RSS feed (full content)](/feed-full.xml)
- [XML sitemap for crawlers](/sitemap.xml)
