---
layout: page
permalink: /students/
title: Students
---

<ul class="students">
{%- for s in site.data.students -%}
  <li>
    <span class="name">
      {% if s.profile %}<a href="{{ s.profile }}">{{ s.name }}</a>{% else %}{{ s.name }}{% endif %}
    </span>
    <span class="meta">— {{ s.degree }}{% if s.coadvisor %}, jointly with {{ s.coadvisor }}{% endif %}{% if s.status %}, {{ s.status }}{% endif %}</span>
    {%- if s.thesis_title -%}
      <div>
        Thesis:
        {% if s.thesis_url %}<a href="{{ s.thesis_url }}">{{ s.thesis_title }}</a>{% else %}{{ s.thesis_title }}{% endif %}
      </div>
    {%- endif -%}
  </li>
{%- endfor -%}
</ul>

<p class="note">Names of current students link to LinkedIn or Google Scholar profiles where available. <em>*</em> = co-advised.</p>
