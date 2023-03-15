import streamlit as st
import pandas as pd
import altair as alt
from dateutil.parser import parse

df = pd.read_csv('global_monthly_stats.csv', thousands=',')

df = df.rename(columns=lambda x: x.lower().replace(' ', '_'))
df.iloc[:, 2:] = df.iloc[:, 2:].apply(pd.to_numeric, errors='coerce')

# global_poi_count = df.iloc[-1]['total_poi_with_parking_lots']
#
# curr_release = df.loc[df.index[-7:], ['country', 'total_poi', 'total_poi_with_parking_lots', 'distinct_brands', 'branded_poi']]
# curr_release['percent_branded'] = curr_release['branded_poi'] / curr_release['total_poi']
# curr_release['percent_branded'] = curr_release['percent_branded'].apply(lambda x: '{:.1%}'.format(x))
# curr_release = curr_release[['country', 'total_poi_with_parking_lots', 'distinct_brands', 'percent_branded']].reset_index(drop=True)
# curr_release[['total_poi_with_parking_lots', 'distinct_brands']] = curr_release[['total_poi_with_parking_lots', 'distinct_brands']].applymap('{:,.0f}'.format)
# curr_release_styled = curr_release.style.apply(lambda x: ['background-color: #DFE7ED' if i%2==0 else '' for i in range(len(x))], axis=0)
#
# #parking lots
# st.write(f"Total POI count across countries, including parking lots POI is: <b>{global_poi_count:,.0f}</b>", unsafe_allow_html=True)
# st.write(curr_release_styled)
#
# parking_df = pd.read_csv('summaryStats/data/parking_lots.csv')
# parking_df = parking_df.rename(columns=lambda x: x.lower().replace(' ', '_'))
# parking_df['distinct_brands'] = 'NA'
# parking_df['percent_branded'] = 'NA'
# parking_df = parking_df[['country', 'total_poi', 'distinct_brands', 'percent_branded']]
# st.write(f"Latest Release - Parking")
# st.write(parking_df)

st.write("Counts from Last 12 Months")
df['release_month'] = df['release_month'].apply(lambda x: parse(x))

grouped_df = df.groupby(['release_month', 'country'], as_index=False)['total_poi'].sum()

filtered_df = grouped_df[grouped_df['country'] != 'Grand Total']
filtered_df = filtered_df[filtered_df['release_month'].isin(filtered_df['release_month'].unique()[-12:])]

chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('yearmonth(release_month):T', axis=alt.Axis(title='', format='%b %Y', labelAngle=50, labelOverlap='parity')),
    y=alt.Y('total_poi', title='Total POI', axis=alt.Axis(format='~s', labelExpr="datum.value ? datum.value / 1000000 + 'M' : ''")),
    color='country',
    tooltip=[alt.Tooltip('release_month:T', title='Release Month', format='%b %Y'), 'country', 'total_poi']
).properties(
    width=800,
    height=500
)

chart