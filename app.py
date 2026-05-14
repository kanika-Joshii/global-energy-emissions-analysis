import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('clean_energy_data.csv')

# Title
st.title('Global Energy Demand & Emissions Analysis')
st.write('Analyzing how energy demand and sources impact greenhouse gas emissions across 15 major countries (2000-2023)')

# Sidebar
st.sidebar.header('Filters')
selected_country = st.sidebar.selectbox('Select Country', sorted(df['country'].unique()))
selected_metric = st.sidebar.selectbox('Select Metric', [
    'electricity_demand',
    'greenhouse_gas_emissions',
    'renewables_share_energy',
    'fossil_share_energy'
])

# Filter data
country_data = df[df['country'] == selected_country]

# Chart 1 - Selected metric over time
st.subheader(f'{selected_metric.replace("_", " ").title()} Over Time — {selected_country}')
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(country_data['year'], country_data[selected_metric], color='steelblue', linewidth=2)
ax.set_xlabel('Year')
ax.set_ylabel(selected_metric.replace('_', ' ').title())
ax.grid(True, alpha=0.3)
st.pyplot(fig)

# Chart 2 - Emissions vs Renewables share
st.subheader(f'Renewables Share vs Emissions — {selected_country}')
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.scatter(country_data['renewables_share_energy'],
            country_data['greenhouse_gas_emissions'],
            color='green', alpha=0.7)
ax2.set_xlabel('Renewables Share (%)')
ax2.set_ylabel('Greenhouse Gas Emissions')
ax2.grid(True, alpha=0.3)
st.pyplot(fig2)

# Chart 3 - Energy mix breakdown
# Chart 3 - Energy mix breakdown
st.subheader(f'Energy Mix — {selected_country} (Latest Year)')
latest = country_data[country_data['year'] == country_data['year'].max()]
mix = {
    'Coal': latest['coal_consumption'].values[0],
    'Oil': latest['oil_consumption'].values[0],
    'Gas': latest['gas_consumption'].values[0],
    'Renewables': latest['renewables_consumption'].values[0]
}

# Remove negative or zero values
mix = {k: v for k, v in mix.items() if v > 0}

if len(mix) > 0:
    fig3, ax3 = plt.subplots(figsize=(6, 6))
    ax3.pie(mix.values(), labels=mix.keys(), autopct='%1.1f%%', startangle=90)
    ax3.set_title('Current Energy Mix')
    st.pyplot(fig3)
else:
    st.write("Energy mix data not available for this country.")
ax3.set_title('Current Energy Mix')
st.pyplot(fig3)

# Raw data
st.subheader('Raw Data')
st.dataframe(country_data)