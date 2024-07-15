# Contents of ~/my_app/pages/page_2.py
import streamlit as st

import matplotlib.pyplot as plt
import geopandas as gpd

st.markdown("# Page 2 :earth_africa:")
st.sidebar.markdown("# Page 2 ❄️")

# Load the GeoJSON file (you need to download the file and provide the path here)
geojson_path = 'departement-60-oise.geojson'

# Read the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file(geojson_path)

# Plot the GeoDataFrame

fig, ax = plt.subplots()

# Customize the plot
plt.title('Map of French Departments')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
gdf.plot(ax=ax, color='blue', edgecolor='white', linewidth=0.4)
# Show the plot
# plt.show()
# Afficher le graphique dans l'application Streamlit
st.pyplot(fig)
