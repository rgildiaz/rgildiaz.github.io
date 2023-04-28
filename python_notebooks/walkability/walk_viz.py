# This script creates a visualization of the Walkability dataset.
# It's a stand-in for `./walkability.ipynb`, since the notebook got too big.

# Make sure to run the script from within the `walkability` directory,
# otherwise it won't be able to find the data file.

# imports 
import altair as alt
import pandas as pd
import os
import sys

alt.data_transformers.disable_max_rows()    # src: https://altair-viz.github.io/altair-viz-v4/user_guide/faq.html#maxrowserror-how-can-i-plot-large-datasets

myJekyllDir = '/Users/rafigildiaz/Desktop/IS 445/rgildiaz.github.io/assets/json'

def main():
  sys.stdout.write("Starting the script...\n")
  df = fetch_data()
  sys.stdout.write("Data fetched\n")

  df = clean(df)
  sys.stdout.write("Data cleaned\n")

  chart = viz(df)
  sys.stdout.write("Chart created\n")

  # save the chart as a json file
  chart.save(myJekyllDir + "/walkability.json")

  sys.stdout.write("Script finished\n")

def fetch_data():
  """
  Fetch the Walkability dataset from the web, or use the local file if it's already downloaded.

  Returns:
    df (pd.DataFrame): The Walkability dataset
  """
  # Use the local file if it's downloaded. Otherwise, get the file from where I've hosted it on the web.
  fname = 'EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv'

  if os.path.isfile(os.getcwd() + "/data/" + fname):
    sys.stdout.write("Using the local file...\n")
    df = pd.read_csv("data/" + fname)
  else:
    sys.stdout.write("Downloading the file...\n")
    df = pd.read_csv('https://media.githubusercontent.com/media/rgildiaz/datasets/main/walkability/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv')

  return df

def clean(df: pd.DataFrame):
  """
  Clean the Walkability dataset.

  Args:
    df (pd.DataFrame): The Walkability dataset
  
  Returns: 
    df (pd.DataFrame): The cleaned dataset
  """
  # These are the state FIPS code, used below to get state names
  # not sure why they're in this order, source: https://code.activestate.com/recipes/577775-state-fips-codes-dict/
  state_codes = {
      'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
      'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
      'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
      'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
      'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
      'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
      'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
      'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
      'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46'
  }

  # reverse the dict to get state names from state codes
  state_codes = {int(v): k for k, v in state_codes.items()}

  # calculate the average walkability score for each CBSA
  cbsa_walk = df.groupby('CBSA').agg('mean')['NatWalkInd'].reset_index()
  cbsa_walk.rename(columns={'NatWalkInd': 'CBSA_Walk'}, inplace=True)
  df = df.merge(cbsa_walk, on='CBSA', how='left')

  # before starting, clean the dataset a bit
  # get only the columns that seem useful to explore
  df = df[[
      'STATEFP',      # State FIPS code
      'CSA_Name',     # Combined statistical area name
      "CBSA_Name",    # Core based statistical area (CBSA) name
      'CBSA_POP',     # CBSA population
      'D2A_EPHHM',    # Employment and household entropy (used for Walkability Index)
      'D2B_E8MIXA',   # 8-tier employment entropy (used for Walkability Index)
      'D3B',          # Street intersection density (used for Walkability Index)
      'D4A',          # Dist from pop-weighted centroid to nearest transit stop (used for Walkability Index)
      'NatWalkInd',   # National Walkability Index
      'CBSA_Walk',    # Average walkability score for the CBSA (calculated above)
  ]]

  # drop rows with missing values
  df = df.dropna()

  # drop rows with 0 population
  df = df[df['CBSA_POP'] > 0]

  # drop rows with 0 or negative values
  df = df[
    (df['D3B'] > 0) & 
    (df['D4A'] > 0) & 
    (df['D2A_EPHHM'] > 0) & 
    (df['D2B_E8MIXA'] > 0)
  ]

  # get the state names from FIPS codes
  df['StateName'] = df['STATEFP'].map(state_codes)

  return df

def viz(df: pd.DataFrame):
  """
  Create the visualization.

  Args:
    df (pd.DataFrame): The Walkability dataset

  Returns:
    chart (altair.Chart): The visualization  
  """
  # make the selector
  select = alt.selection_multi(fields=['CBSA_Name'])

  # make the first chart
  chart1 = alt.Chart(df).mark_rect().encode(
      x=alt.X(
        'StateName',
        type='nominal',
        title="State"
      ),
      y=alt.Y(
        'CBSA_POP',
        aggregate='sum',
        type='quantitative',
        title="Population",
        scale=alt.Scale(type='log')
      ),
      color=alt.Color(
        'CBSA_Walk',
        type='quantitative',
        title="Mean Walkability Score",
        legend=alt.Legend(
          title="Walkability Score",
          orient='right',
          titleOrient='right',
        ),
        scale=alt.Scale(scheme='viridis')
      ),
      tooltip=alt.Tooltip(
        field="CBSA_Name",
        type='nominal'
      ),
      order=alt.Order(
        'StateName:N',
        sort='ascending'
      )
  ).properties(
      height=200,
      width=600
  ).add_selection(select)

  # make the second chart
  chart2 = alt.Chart(df).mark_circle(
      size=40,
      opacity=0.75,
  ).encode(
    x=alt.X(
      'D4A',
      type='quantitative',
      title="Distance to Transit"
    ),
    y=alt.Y(
      'D3B',
      type='quantitative',
      title="Street Intersection Density",
      scale=alt.Scale(type='log')
    ),
    color=alt.Color(
      'NatWalkInd',
      type='quantitative',
      title="National Walkability Index",
      legend=alt.Legend(
        title="Walkability Score",
        orient='right',
        titleOrient='right',
      ),
      scale=alt.Scale(scheme='viridis')
    ),
    # this multi-tooltip was found here: https://stackoverflow.com/questions/52223358/rename-tooltip-in-altair
    tooltip=[
      alt.Tooltip(
        field="NatWalkInd",
        type='quantitative',
        title="Walkability Score"
      ),
      alt.Tooltip(
        field="CBSA_Name",
        type='nominal',
        title="CBSA Name"
      )
    ]
  ).properties(
      width=600,
      height=200
  ).transform_filter(select)

  chart3 = alt.Chart(df).mark_circle(
      size=40,
      opacity=0.75,
  ).encode(
    x=alt.X(
      'D2A_EPHHM',
      type='quantitative',
      title="Employment and Household Entropy"
    ),
    y=alt.Y(
      'D2B_E8MIXA',
      type='quantitative',
      title="8-tier Employment Entropy"
    ),
    color=alt.Color(
      'NatWalkInd',
      type='quantitative',
      title="National Walkability Index",
      legend=alt.Legend(
        title="Walkability Score",
        orient='right',
        titleOrient='right',
      ),
      scale=alt.Scale(scheme='viridis')
    ),
    tooltip=[
      alt.Tooltip(
        field="NatWalkInd",
        type='quantitative',
        title="Walkability Score"
      ),
      alt.Tooltip(
        field="CBSA_Name",
        type='nominal',
        title="CBSA Name"
      )
    ]
  ).properties(
      width=600,
      height=200
  ).transform_filter(select)

  chart = alt.vconcat(
    chart1, chart2, chart3,
    title=alt.TitleParams(
      text="Walkability in US Metropolitan Areas",
      anchor="middle",
      fontSize=30,
      subtitle="Select a box or two on the first plot to filter the others."
    )
  ).resolve_scale(
      color='independent'
  )

  return chart

if __name__ == "__main__":
  main()