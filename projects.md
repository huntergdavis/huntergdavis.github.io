---
layout: page
title: Projects
permalink: /projects/
---

{% assign tagged = site.posts | where_exp: "p", "p.project" %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": {{ page.title | jsonify }},
  "url": {{ page.url | absolute_url | jsonify }},
  "isPartOf": { "@type": "WebSite", "url": {{ '/' | absolute_url | jsonify }} },
  "mainEntity": {
    "@type": "ItemList",
    "numberOfItems": {{ tagged.size }},
    "itemListElement": [{% for post in tagged %}
      {
        "@type": "ListItem",
        "position": {{ forloop.index }},
        "url": {{ post.url | absolute_url | jsonify }},
        "name": {{ post.title | jsonify }}
      }{% unless forloop.last %},{% endunless %}{% endfor %}
    ]
  }
}
</script>

{% assign projects = site.posts | group_by: "project" | sort: "name" %}
{% for proj in projects %}{% if proj.name and proj.name != "" %}
## {{ site.data.projects[proj.name] | default: proj.name }}

{{ proj.items.size }} post{% if proj.items.size != 1 %}s{% endif %}.

{% for post in proj.items reversed %}- {{ post.date | date: "%b %-d, %Y" }} — [{{ post.title | escape }}]({{ post.url }})
{% endfor %}
{% endif %}{% endfor %}
