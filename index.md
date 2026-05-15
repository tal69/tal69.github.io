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
    <h1>Prof. Tal Raviv</h1>
    <p class="subtitle">Researcher in operations research, transportation &amp; logistics</p>

    <p>My main research interests are shared mobility systems, small-parcel
    delivery logistics, public transit planning, warehousing, and traffic
    management. I have published about 45 papers in the operations research
    literature and have advised several start-up companies.</p>

    <p>I am a Full Professor in the School of Industrial &amp; Intelligent
    Systems Engineering at the Iby and Aladar Fleischman Faculty of
    Engineering, Tel Aviv University, and co-head the transportation and
    logistics group at TAU (with Prof. Michal Tzur).</p>

    <p>I hold a B.A. from the Eitan Berglas School of Economics, Tel Aviv
    University (1993), an M.B.A. from the Recanati School of Business, Tel
    Aviv University (1997), and a Ph.D. in Operations Research from the
    William Davidson Faculty of Industrial Engineering and Management,
    Technion – Israel Institute of Technology, Haifa (2003). I spent two
    years (2004–2006) as a postdoctoral fellow at the Sauder School of
    Business, University of British Columbia, Vancouver, Canada.</p>
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
