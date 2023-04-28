---
name: Walkability in the US
tools: [Python, vega-lite]
image: assets/pngs/walkability.png
description: Analyzing the National Walkability Index Database
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

# Walkability in the US

_Analyzing the National Walkability Index Database_

_2023.04.28_

---

It's no secret that the United States suffers from a "car culture". Metropolitan areas are crowded with parking lots larger than the buildings they were constructed for and wide streets to accommodate heavy traffic. The US highway network spans [over 4 million miles](https://www.statista.com/statistics/183397/united-states-highway-mileage-since-1990/), and an estimated [3.17 _trillion_ vehicle-miles were driven in 2022](https://www.statista.com/statistics/185579/us-vehicle-miles-in-transit-since-1960/) alone.

When compared with other major countries around the world, it becomes apparent just how much more Americans drive: in 2017, 4.1 million passenger-miles (distance of trip × number of passengers) were traveled in the US: overe 2x more than Japan, Great Britain, and Australia combined ([source](https://data.oecd.org/transport/passenger-transport.htm)).

<!-- center the chart-->
<fig style="width: 100%; display: flex; flex-direction: column; align-items: center;">
  <vegachart schema-url="{{ site.baseurl }}/assets/json/car_usage.json" style="width: fit-content"></vegachart>
  <figcaption style="font-style: italic">
    Data collected from <a href="https://data.oecd.org/transport/passenger-transport.htm">OCED</a>
  </figcaption>
</fig>

## The National Walkability Index

One method the US Environmental Protection Agency is using in an attempt to promote "smarter" or healthier cities is attempting to create an objective measure of walkability. The [National Walkability Index Dataset](https://catalog.data.gov/dataset/walkability-index) is the culmination of their work in this area, aggregating and transforming data from an earlier EPA project, the [Smart Location Dataset](), and ranking the weight of some measurements that were taken.

I hope this dashboard helps to illustrate the relationships between these different factors.

<fig style="width: 100%; display: flex; flex-direction: column; align-items: center;">
  <vegachart schema-url="{{ site.baseurl }}/assets/json/walkability.json" style="width: 100%"></vegachart>
  <figcaption style="font-style: italic">
    Data collected from <a href="https://catalog.data.gov/dataset/walkability-index">US EPA</a>
  </figcaption>
</fig>

## More Information

Explore the data on your own!

<div class="left">
{% include elements/button.html link="https://catalog.data.gov/dataset/walkability-index" text="The (Walkability) Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/rgildiaz/rgildiaz.github.io/blob/main/python_notebooks/walkability/walkability.ipynb" text="The (Walkability) Analysis" %}
</div>

<div class="left">
{% include elements/button.html link="https://data.oecd.org/transport/passenger-transport.htm" text="The (Car Use) Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/rgildiaz/rgildiaz.github.io/blob/main/python_notebooks/walkability/car_usage.ipynb" text="The (Car Use) Analysis" %}
</div>
