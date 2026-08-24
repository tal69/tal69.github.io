---
layout: page
permalink: /publications/
title: Publications
---

{% assign journal_papers = site.data.publications.journal | sort: "cv_number" %}
{% assign book_chapters = site.data.publications.chapters | sort: "year" %}

## Papers in peer-reviewed journals

<ol class="pubs cv-numbered">
{%- for p in journal_papers -%}
  <li data-cv-number="{{ p.cv_number }}">
    <span class="authors">{{ p.authors }}</span>,
    “<span class="title">{% if p.url %}<a href="{{ p.url }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</span>”,
    <span class="venue">{{ p.venue }}</span>{% if p.year %} ({{ p.year }}){% endif %}{% if p.pages %}, {{ p.pages }}{% endif %}.
    {%- if p.extras -%}
      <span class="extras">
        {%- for e in p.extras -%} <a href="{{ e.url }}">{{ e.label }}</a>{%- endfor -%}
      </span>
    {%- endif -%}
  </li>
{%- endfor -%}
</ol>

## Book chapters

<ol class="pubs">
{%- for p in book_chapters -%}
  <li>
    <span class="authors">{{ p.authors }}</span>,
    “<span class="title">{% if p.url %}<a href="{{ p.url }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</span>”,
    <span class="venue">{{ p.venue }}</span>{% if p.year %} ({{ p.year }}){% endif %}{% if p.pages %}, {{ p.pages }}{% endif %}.
    {%- if p.extras -%}
      <span class="extras">
        {%- for e in p.extras -%} <a href="{{ e.url }}">{{ e.label }}</a>{%- endfor -%}
      </span>
    {%- endif -%}
  </li>
{%- endfor -%}
</ol>

## Working papers

<ol class="pubs">
{%- for p in site.data.publications.working reversed -%}
  <li>
    <span class="authors">{{ p.authors }}</span>,
    “<span class="title">{% if p.url %}<a href="{{ p.url }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</span>”{% if p.date %}, {{ p.date }}{% endif %}.
    {%- if p.extras -%}
      <span class="extras">
        {%- for e in p.extras -%} <a href="{{ e.url }}">{{ e.label }}</a>{%- endfor -%}
      </span>
    {%- endif -%}
  </li>
{%- endfor -%}
</ol>
