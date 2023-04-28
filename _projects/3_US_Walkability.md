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

_2023.04.28 - by Rafi Gil Diaz_

---

It's no secret that the United States suffers from a "car culture". Metropolitan areas are crowded with parking lots larger than the buildings they were constructed for and wide streets to accommodate heavy traffic. The US highway network spans [over 4 million miles](https://www.statista.com/statistics/183397/united-states-highway-mileage-since-1990/), and an estimated [3.17 _trillion_ vehicle-miles were driven in 2022](https://www.statista.com/statistics/185579/us-vehicle-miles-in-transit-since-1960/) alone.

When compared with other major countries around the world, it becomes apparent just how much more Americans drive: in 2017, 4.1 million passenger-miles (distance of trip × number of passengers) were traveled in the US: overe 2x more than Japan, Great Britain, and Australia combined ([source](https://data.oecd.org/transport/passenger-transport.htm)).

<!-- center the chart-->
<fig style="width: 100%; display: flex; flex-direction: column; align-items: center;">
  <vegachart schema-url="{{ site.baseurl }}/assets/json/car_usage.json" style="width: fit-content"></vegachart>
  <figcaption style="font-style: italic">
    Data: <a href="https://data.oecd.org/transport/passenger-transport.htm">OCED</a>, Viz: <a href="#more-information">Me</a>
  </figcaption>
</fig>

## The National Walkability Index

One method the US Environmental Protection Agency is using in an attempt to promote "smarter" or healthier cities is attempting to create an objective measure of walkability. The [National Walkability Index Dataset](https://catalog.data.gov/dataset/walkability-index) is the culmination of their work in this area, aggregating and transforming data from an earlier EPA project, the [Smart Location Database](https://www.epa.gov/smartgrowth/smart-location-mapping#SLD) (SLD), to consider the factors they found to be most important to a city's walkability.

In loose terms, "walkability" could be defined as "how easy and inviting it is to choose walking over any other mode of transport in any given location". The EPA states in loose terms, "Walkability depends upon characteristics of the built environment that influence the likelihood of walking being used as a mode of travel" ([source](https://catalog.data.gov/dataset/walkability-index)).

To calculate a Walkability Index for each region tracked in the SLD, the EPA team considered four main factors:

1. **8-tier employment entropy** - Employment is divided into 8 categories: retail, office, service, industrial, entertainment, education, healthcare, and public administration ([EPA](https://enviroatlas.epa.gov/enviroatlas/DataFactSheets/pdf/Supplemental/Employmentdiversity.pdf)). Higher entropy means there is a greater mix of job categories.
2. **Employment and household entropy** - Similar to 8-tier employment entropy, but also considers households.
3. **Street intersection density**
4. **Distance from the population-weighted centroid of an area to the nearest transit stop**

In general, a city that is high in **8-tier employment entropy**, **employment and household entropy**, and **street intersection density** will be more walkable than a city low in those factors. A city with a lower **distance from the population-weighted centroid of an area to the nearest transit stop** will likely be more walkable than a city with a higher distance.

I hope this dashboard helps to illustrate the relationships between these different factors and helps to demonstrate the trends mentioned above.

<fig style="width: 100%; display: flex; flex-direction: column; align-items: center; margin: 1.5em 0;">
  <vegachart schema-url="{{ site.baseurl }}/assets/json/walkability.json" style="width: fit-content"></vegachart>
  <figcaption style="font-style: italic">
    Data: <a href="https://catalog.data.gov/dataset/walkability-index">US EPA</a>, Viz: <a href="#more-information">Me</a>
  </figcaption>
</fig>

> _It seems like some of the tooltips break when this site is in dark mode. Use the sun/moon button at the top of the page to switch the theme if you can't read the CBSA Name in the tooltips for the second and third graphs. I tried fixing this with [Altair](https://altair-viz.github.io/), which was used to generate the visualizations, but it seems to be a problem with the way tooltips are rendered, not with any setting that can be changed._


## Other Research About Walkability

While the National Walkability Index has been made available for public use, it has also been used internally by the US government groups for studies or other projects. One such project is the **CDC**'s 2020 study, [_Associations between the National Walkability Index and walking among US Adults_](https://stacks.cdc.gov/view/cdc/111032).

<fig style="width: 100%; display: flex; flex-direction: column; align-items: center; margin: 1.5em 0;">
  <h5>Associations between the National Walkability Index and walking among US Adults</h5>
  <img 
    src="{{ site.baseurl }}/assets/pngs/cdc_111032_DS3.jpeg" 
    style="max-width: 700px"
    alt="Associations between the National Walkability Index and walking among US Adults"
  />
  <figcaption style="font-style: italic">
    Walking habits among US adults as correlated with different census statistics, urban and rural. Source: <a href="https://stacks.cdc.gov/view/cdc/111032">CDC</a>
  </figcaption>
</fig>

This study worked to correlate the data gathered from the EPA's Walkability Index with information about walking habits from the 2015 [National Health Interview Survey](https://www.cdc.gov/nchs/nhis/index.htm). I believe the above visualization does a good job of summarizing their work, showing where different categories of people are more likely to live. As you might guess, urban areas contain more walkable locations (this is in part due to the way Walkability is measured, [described above](#the-national-walkability-index)). It also seems like the Northeast contains the highest percentage of highly walkable areas, for both rural and urban locations.

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
