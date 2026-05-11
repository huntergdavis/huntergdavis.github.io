---
layout: page
title: Tags
permalink: /tags/
---

{% assign tag_pairs = site.data.tags | sort %}
{% for pair in tag_pairs %}- [{{ pair[0] }}](/search.html?query={{ pair[0] | url_encode }}) <span class="tag-count">({{ pair[1] }})</span>
{% endfor %}
