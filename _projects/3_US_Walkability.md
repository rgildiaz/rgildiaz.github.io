---
name: Walkability in the US
tools: [Python, vega-lite]
image: assets/pngs/bigfoot.png
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

It's no secret that the United States suffers from a "car culture". Parking lots bigger than the malls or apartments they were built for are a regular sight in metropolitan areas. The US highway network spans [over 4 million miles](https://www.statista.com/statistics/183397/united-states-highway-mileage-since-1990/), and an estimated [3.17 _trillion_ vehicle-miles were driven in 2022](https://www.statista.com/statistics/185579/us-vehicle-miles-in-transit-since-1960/) alone.

When put compared with other major countries around the world, it becomes apparent just how much more Americans drive: in 2017, 4.1 million passenger-miles (distance of trip × number of passengers) were traveled in the US, less than Japan, Great Britain, and Australia combined ([source](https://data.oecd.org/transport/passenger-transport.htm)).

<!-- center the chart-->
<div style="width: 100%; display: flex; flex-direction: column; align-items: center;">
  <vegachart schema-url="{{ site.baseurl }}/assets/json/car_usage.json" style="width: fit-content"></vegachart>
</div>

## The National Walkability Index

<vegachart schema-url="{{ site.baseurl }}/assets/json/walkability.json" style="width: 100%"></vegachart>

## More Information

Explore the data on your own!

<div class="left">
{% include elements/button.html link="https://catalog.data.gov/dataset/walkability-index" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/rgildiaz/rgildiaz.github.io/blob/main/python_notebooks/hw10.ipynb" text="The Analysis" %}
</div>
