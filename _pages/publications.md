---
layout: page
permalink: /publications/
title: Publications
---

## Papers in peer-reviewed journals

{%- assign journal_papers = site.data.publications.journal | sort: "year" -%}
<ol class="pubs">
{%- for p in journal_papers -%}
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

## Book chapters

<ol class="pubs">
{%- assign book_chapters = site.data.publications.chapters | sort: "year" -%}
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
