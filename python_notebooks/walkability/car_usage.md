---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.5
  kernelspec:
    display_name: DataViz
    language: python
    name: python3
---

# Car Usage
This notebook will generate some visualizations about car usage across the world.

Data sources:
Passenger-miles outside the US: [https://data.oecd.org/transport/passenger-transport.htm](https://data.oecd.org/transport/passenger-transport.htm)

~~Passenger-miles in the US: [https://www.bts.gov/content/us-passenger-miles](https://www.bts.gov/content/us-passenger-miles)~~ (didn't realize US data is in the first dataset)

```python
# imports
import pandas as pd
import altair as alt
myJekyllDir = '/Users/rafigildiaz/Desktop/IS 445/rgildiaz.github.io/assets/json'
```

```python
# US data is actually unneeded, it's in the other dataset
# # load the US data
# df_us = pd.read_excel('data/statistic_id185769_passenger-miles---highway-traffic-in-the-united-states-1990-2019.xlsx', sheet_name='Data', skiprows=4)

# # the first column is empty
# df_us = df_us.drop(columns=df_us.columns[0])

# # rename the columns
# df_us.columns = ['year', 'passenger_miles']

# # data is in millions of miles
# # df_us['passenger_miles'] = df_us['passenger_miles'] * 1000000

# df_us.head()
```

```python
# load the not-US data
df_world = pd.read_csv('data/DP_LIVE_25042023212441825.csv')

# drop unneeded columns
df_world = df_world.drop(columns=['INDICATOR', 'SUBJECT', 'MEASURE', 'FREQUENCY', 'Flag Codes'])

# rename the columns
df_world.columns = ['country', 'year', 'passenger_miles']

# convert from kilometers to millions of miles (0.621371 miles per kilometer)
df_world['passenger_miles'] = df_world['passenger_miles'] * 0.621371 / 1000000

# only keep some major countries
df_world = df_world[df_world['country'].isin(['AUS', 'CAN', 'GBR', 'JPN', 'USA'])]

# format year as datetime
df_world['year'] = pd.to_datetime(df_world['year'], format='%Y')

df_world.head()
```

```python
# unneeded
# chart1 = alt.Chart(df_us).mark_line().encode(
#     x='year',
#     y='passenger_miles'
# ).properties(
#     title='Passenger miles in the US'
# )

# chart1
```

```python
# found this layering for word marks here: https://stackoverflow.com/questions/61194028/adding-labels-at-end-of-line-chart-in-altair

countries = alt.Chart(df_world).mark_line().encode(
    x=alt.X(
        'year',
        title="Year"
    ),
    y=alt.Y(
        'passenger_miles',
        title="Passenger miles (millions)",
        # scale=alt.Scale(type='log')
    ),
    color=alt.Color(
        'country',
        title="Country",
        scale=alt.Scale(
            scheme='category10',
        ),
        legend=None
    )
).properties(
    title='Yearly Passenger Miles'
)

labels = alt.Chart(df_world).mark_text(
    align='left',
    baseline='middle',
    dx=3,
    size=10
).encode(
    x=alt.X(
        'year',
        title="Year",
        aggregate='max'
    ),
    y=alt.Y(
        'passenger_miles',
        title="Passenger miles (millions)",
        # scale=alt.Scale(type='log'),
        aggregate={'argmax': 'passenger_miles'}
    ),
    text=alt.Text(
        'country'
    ),
    color=alt.Color(
        'country',
        title="Country",
        scale=alt.Scale(
            scheme='category10',
        ),
        legend=None
    )
)

chart = alt.layer(countries, labels).resolve_scale(color='independent').properties(
    width=600,
    height=300
)
chart.save(myJekyllDir + '/car_usage.json')

chart
```
