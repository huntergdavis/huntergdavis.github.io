---
layout: page
title: Timeline
permalink: /timeline/
---
{% include jsonld_timeline.html %}
{% assign by_year = site.posts | group_by_exp: "p", "p.date | date: '%Y'" %}
<nav class="timeline-jumpnav" aria-label="Jump to year">
{% for yr in by_year %}<a href="#{{ yr.name }}">{{ yr.name }}</a>{% endfor %}
</nav>

{% for yr in by_year %}
<section class="timeline-year">
<h2 id="{{ yr.name }}"><a href="/archive/{{ yr.name }}/">{{ yr.name }}</a> <span class="timeline-year-count">{{ yr.items.size }} post{% if yr.items.size != 1 %}s{% endif %}</span></h2>
<div class="timeline-grid">
{% for post in yr.items %}{% assign hero = "" %}{% if post.image and post.image != "" %}{% assign hero = post.image %}{% elsif post.featured_img and post.featured_img != "" %}{% assign hero = post.featured_img %}{% endif %}<a class="timeline-card{% if hero == "" %} no-hero{% endif %}" href="{{ post.url }}">
  {% if hero != "" %}<img class="timeline-thumb" src="{{ hero }}" loading="lazy" decoding="async" alt="">{% endif %}
  <div class="timeline-card-body">
    <time class="timeline-card-date">{{ post.date | date: "%b %-d" }}</time>
    <h3 class="timeline-card-title">{{ post.title | escape }}</h3>
  </div>
</a>
{% endfor %}
</div>
</section>
{% endfor %}
