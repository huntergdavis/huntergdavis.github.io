---
layout: page
title: Tags
permalink: /tags/
---
{% include jsonld_tags_index.html %}
{% assign tag_pairs = site.data.tags | sort %}
{% for pair in tag_pairs %}{% if pair[1] >= 2 %}- [{{ pair[0] }}](/tags/{{ pair[0] }}/) <span class="tag-count">({{ pair[1] }})</span>
{% else %}- [{{ pair[0] }}](/search.html?query={{ pair[0] | url_encode }}) <span class="tag-count">({{ pair[1] }})</span>
{% endif %}{% endfor %}
