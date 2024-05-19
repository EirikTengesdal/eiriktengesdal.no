---
layout: page
title: Statements
permalink: /statements/
description: This collection contains response statements to public consultations for comments (<em>høringer</em>).
nav: true
nav_order: 6
display_categories: [work]
horizontal: false
---

<!-- pages/statement.md -->
<div class="statements">
{% if site.enable_statements_categories and page.display_categories %}
  <!-- Display categorized statements -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_statements = site.statements | where: "category", category %}
  {% assign sorted_statements = categorized_statements | sort: "importance" %}
  <!-- Generate cards for each statement -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-2">
    {% for statement in sorted_statements %}
      {% include statements_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="grid">
    {% for statement in sorted_statements %}
      {% include statements.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display statements without categories -->

{% assign sorted_statements = site.statements | sort: "importance" %}

  <!-- Generate cards for each statement -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-2">
    {% for statement in sorted_statements %}
      {% include statements_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="grid">
    {% for statement in sorted_statements %}
      {% include statements.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
