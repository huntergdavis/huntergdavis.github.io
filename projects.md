---
layout: page
title: Projects
permalink: /projects/
---

{% assign projects = site.posts | group_by: "project" | sort: "name" %}
{% for proj in projects %}{% if proj.name and proj.name != "" %}
## {{ site.data.projects[proj.name] | default: proj.name }}

{{ proj.items.size }} post{% if proj.items.size != 1 %}s{% endif %}.

{% for post in proj.items reversed %}- {{ post.date | date: "%b %-d, %Y" }} — [{{ post.title | escape }}]({{ post.url }})
{% endfor %}
{% endif %}{% endfor %}
