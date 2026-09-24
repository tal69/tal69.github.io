---
layout: default
title: Home
description: Researcher in operations research, transportation, and logistics at Tel Aviv University.
---

<section class="about">
  <div>
    <img src="{{ '/assets/img/profile.jpg' | relative_url }}" alt="Tal Raviv">
    <p class="meta">
      School of Industrial &amp; Intelligent Systems Engineering<br>
      Tel Aviv University
    </p>
  </div>
  <div>
    <p class="subtitle">Researcher in operations research, transportation, and logistics</p>

    <p>I am a full professor in the School of Industrial &amp; Intelligent
    Systems Engineering at Tel Aviv University's Iby and Aladar Fleischman
    Faculty of Engineering. I co-head the transportation and logistics group
    at the university with Prof. Michal Tzur.</p>

    <p>My research interests include shared mobility systems, small-parcel
    delivery logistics, public transit planning, warehousing, and traffic
    management. I have published more than 45 papers in the operations research
    literature and advised several start-up companies.</p>

    <p>I earned a B.A. from the Eitan Berglas School of Economics at Tel Aviv
    University in 1993 and an M.B.A. from the Leon Recanati Graduate School of
    Business Administration at Tel Aviv University in 1997. I earned a Ph.D.
    in Operations Research from the William Davidson Faculty of Industrial
    Engineering and Management at the Technion, Israel Institute of Technology,
    in Haifa in 2003. From 2004 to 2006, I was a postdoctoral fellow at the
    Sauder School of Business, University of British Columbia, in Vancouver,
    Canada.</p>
  </div>
</section>

## Selected recent publications

<ul class="pubs">
{%- assign recent = site.data.publications.journal | where_exp: "p", "p.featured" -%}
{%- for p in recent -%}
  <li>
    <span class="authors">{{ p.authors }}</span>,
    “<span class="title">{% if p.url %}<a href="{{ p.url }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</span>”,
    <span class="venue">{{ p.venue }}</span>{% if p.year %} ({{ p.year }}){% endif %}{% if p.pages %}, {{ p.pages }}{% endif %}.
  </li>
{%- endfor -%}
</ul>

<p><a href="{{ '/publications/' | relative_url }}">See the full publication list →</a></p>
