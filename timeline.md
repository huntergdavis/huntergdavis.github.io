---
layout: page
title: Timeline
permalink: /timeline/
---

<p class="timeline-summary">Every post on one page, newest year first.</p>

{% assign by_year = site.posts | group_by_exp: "p", "p.date | date: '%Y'" %}
{% for yr in by_year %}
<section class="timeline-year">
<h2 id="{{ yr.name }}"><a href="/archive/{{ yr.name }}/">{{ yr.name }}</a> <span class="timeline-year-count">{{ yr.items.size }} post{% if yr.items.size != 1 %}s{% endif %}</span></h2>
<div class="timeline-grid">
{% for post in yr.items %}{% assign hero = post.image | default: post.featured_img %}<a class="timeline-card{% unless hero %} no-hero{% endunless %}" href="{{ post.url }}">
  {% if hero != blank %}<img class="timeline-thumb" src="{{ hero }}" loading="lazy" decoding="async" alt="">{% endif %}
  <div class="timeline-card-body">
    <time class="timeline-card-date">{{ post.date | date: "%b %-d" }}</time>
    <h3 class="timeline-card-title">{{ post.title | escape }}</h3>
  </div>
</a>
{% endfor %}
</div>
</section>
{% endfor %}
