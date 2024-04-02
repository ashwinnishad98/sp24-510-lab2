# app.py
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Penguin Data Visualization",
    page_icon="🐧",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("🐧 Penguins Data Visualization")

df = pd.read_csv(
    "https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv"
)

st.write(df)

# scatter plot
plot, axs = plt.subplots()
sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species", ax=axs)
axs.set_title("Penguin Bill Measurements")
axs.set_xlabel("Bill Length (mm)")
axs.set_ylabel("Bill Depth (mm)")

st.pyplot(plot)
