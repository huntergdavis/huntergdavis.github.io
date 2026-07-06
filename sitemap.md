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
- [Archive (by year)](/archive/)
- [Timeline (visual)](/timeline/)
- [Tags (all topics)](/tags/)
- [Search](/search.html)
- [Random post](/random.html)

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

## Posts by series

{% assign series_groups = site.posts | group_by: "series" | sort: "name" %}
{% for s in series_groups %}{% if s.name and s.name != "" %}- **{{ s.name | replace: '-', ' ' }}** — {{ s.items.size }} posts: {% assign first_in_series = s.items | sort: "date" | first %}[start here]({{ first_in_series.url }})
{% endif %}{% endfor %}

## All tags

{% assign tag_pairs = site.data.tags | sort %}
{% for pair in tag_pairs %}{% if pair[1] >= 2 %}[{{ pair[0] }}](/tags/{{ pair[0] }}/) ({{ pair[1] }}){% else %}[{{ pair[0] }}](/search.html?query={{ pair[0] | url_encode }}) ({{ pair[1] }}){% endif %}{% unless forloop.last %} &middot; {% endunless %}{% endfor %}

## Feeds and metadata

- [RSS feed (excerpts)](/feed.xml)
- [RSS feed (full content)](/feed-full.xml)
- [XML sitemap for crawlers](/sitemap.xml)
