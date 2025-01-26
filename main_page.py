# Contents of ~/my_app/main_page.py
import streamlit as st

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import geopandas as gpd

st.markdown("# Prénoms français donnés à la naissance :smile:")
st.sidebar.markdown("# Présentation :balloon:")

# Read the Parquet file into a DataFrame
df = pd.read_parquet("prenoms-2023-dpt.parquet")

st.write(df.head(6))



