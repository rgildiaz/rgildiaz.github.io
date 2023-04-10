---
layout: page
title: About
permalink: /about/
weight: 3
---

# **About Me**

Hi, I'm **{{ site.author.name }}**. I am definitely not a rat!

<div class="row">
{% include about/skills.html title="Programming Skills" source=site.data.programming-skills %}
{% include about/skills.html title="Other Skills" source=site.data.other-skills %}
</div>

<div class="row">
{% include about/timeline.html %}
</div>
