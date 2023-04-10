---
name: Homework 10
tools: [Python, HTML, vega-lite]
image: assets/pngs/bigfoot.png
description: Visualizing Bigfoot Sightings with Altair
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

# Vega-lite + Altair

_Visualizing Bigfoot Sightings_

---

This week, I'll be making some modifications to the visualizations I made as part of the last homework assignment. Check out the original visualizations [here](https://starboard.gg/nb/nzlt018)!

## Data Cleaning

Before getting started, the first step is to clean the data:

```py
# Import the dataset, get only the columns we need, and drop any NaNs
URL = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2022/main/data/bfro_reports_fall2022.csv"
df = pd.read_csv(URL)

df = df[['state', 'latitude', 'longitude', 'classification', 'season']].dropna()

# drop any 0s in the lat and long columns
df = df[(df['latitude'] != 0) & (df['longitude'] != 0)]

df.head()
```

Here, I collected only the columns I needed for visualization and dropped NA values. I also dropped 0s in the only quantitative columns I used, since they are used in place of NA values in this dataset. The data is also linked [at the bottom of this page](#sources).

This step is exactly the same as it was in Homework 9 since I am plotting the same variables in a slightly different way.

## Plot 1

This plot shows the location of each reported sighting as well as its classification.

<vegachart schema-url="{{ site.baseurl }}/assets/json/w10_chart1.json" style="width: 100%"></vegachart>

- **Design**
  - **Encoding**: This plot uses latitude, longitude, and classification data. Latitude and longitude are both quantitative, and classification is encoded ordinally since the order of each class matters.
  - **Color Mapping**: After some testing, I chose to use a traditional "green yellow red" color pallet here. At first, I tried using a grayscale scheme for Class A and B reports so a more prominent accent color could be used for Class C, but I found it harder to read.
- **Transformations**: Beyond the simple cleaning explained [above](#data-cleaning), no other transformations are necessary for this plot.
- **Overlap with HW9**: This plot is pretty similar to the first plot from Homework 9. I like the effect of plotting latitude vs. longitude since it gives a good general shape of the US. I decided to plot classification here instead of the season since season data doesn't really matter on a location plot, and since classification was a little hard to read on the bar chart from HW9.


## Plot 2

This second plot show the total number of sightings in each state, as well as the recorded season of the report. You can also hover over each season segment on the plot to see the total count for that section.

<vegachart schema-url="{{ site.baseurl }}/assets/json/w10_chart2.json" style="width: 100%"></vegachart>

- **Design**
  - **Encoding**: Since states are unordered, they are encoded nominally. However, since a count must be aggregated for each state, it is encoded quantitatively along the y-axis. Seasons are encoded nominally as well, since their order also doesn't matter.
  - **Color Mapping**: I chose to use colors that I felt at least somewhat represented each season, which (hopefully) makes the plot a little easier to read.
- **Transformations**: To gather a count of each state's report, `'state:Q', aggregate='count` must be specified for the y-axis. 
- **Overlap with HW9**: This plot is also quite similar to the second plot in Homework 9. It follows the same format of plotting each state's total report count; however, this version shows the distribution of the seasons of each report instead of the classification. I think that this works much better since the seasons are much more evenly distributed.

## Linking the Plots

To put the plots together (and make the visualization a little more interesting), I added an `altair.selection_interval` brush, which can be used to select an area on the first plot. The second plot updates to show the total number of sightings and season just for that region.

<vegachart schema-url="{{ site.baseurl }}/assets/json/w10_dashboard.json" style="width: 100%"></vegachart>

Using the selector on this dashboard can show some interesting data. It seems like some sightings were logged incorrectly (there is a report for Washington that's in the middle of the Pacific Ocean?).

## In Conclusion...

- Altair was much more enjoyable to work with than some of the other tools we've used this semester. I like how easy it is to understand and how straightforward it feels to use.
- Since Altair isn't super old yet, when things did get difficult, it was sometimes hard to find specific documentation or StackOverflow answers. This is especially noticeable when compared to something like MatPlotLib.
- Overall, I'm happy with the way the final dashboard works. However, if I had more time, I might make some aesthetic changes to try to fix resizing and add labels to the tooltips. 
- I'm also not sure how I feel about stacking the plots vertically. Since the first plot needs to be wider than it is tall, it made sense to me to use this format. However, it's a little difficult to fit on screen. If I expanded this dashboard, I might add a third element which can stand vertically on either the right or left side, allowing these first two visualizations to shrink.

<!-- these are written in a combo of html and liquid -->

## Sources

Explore the data on your own here!

<div class="left">
{% include elements/button.html link="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2022/main/data/bfro_reports_fall2022.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/rgildiaz/rgildiaz.github.io/blob/main/python_notebooks/hw10.ipynb" text="The Analysis" %}
</div>
