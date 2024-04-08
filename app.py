# app.py
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Titanic Data Visualization",
    page_icon="🛳️",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("🛳️ Titanic Data Visualization")

df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

survival_options = {1: "Yes", 0: "No"}

with st.sidebar:
    # Filter options

    # slider for fare range
    fare_range_slider = st.slider(
        "Fare Range ($)", min(df["Fare"]), max(df["Fare"]), value=max(df["Fare"])
    )

    # selectbox for survivor filter
    survivor_filter = st.selectbox(
        "Survived?", options=list(survival_options.values()), index=None
    )

    # multiselect for passenger class filter
    pclass_filter = st.multiselect(
        "Passenger Class", options=df["Pclass"].unique().tolist()
    )

filtered_df = df.copy()

# Update the dataframe based on filters applied
if pclass_filter:
    filtered_df = filtered_df[filtered_df["Pclass"].isin(pclass_filter)]

if survivor_filter:
    survivor_filter_value = {v: k for k, v in survival_options.items()}[survivor_filter]
    filtered_df = filtered_df[filtered_df["Survived"] == survivor_filter_value]

filtered_df = filtered_df[filtered_df["Fare"] < fare_range_slider]

# Calculate survival rates by passenger class
survival_rates = filtered_df.groupby("Pclass")["Survived"].mean().reset_index()
survival_rates["Pclass"] = survival_rates["Pclass"].astype(str)

# Show RAW and Filtered data
with st.expander("RAW Data"):
    st.write(df)

with st.expander("Filtered Data"):
    st.write(filtered_df)

# Display dataset description
st.markdown(
    """
This dataset contains information about the passengers on the Titanic, along with information relating to their survival.
Descriptions of each column:
- **Survived**: Whether the passenger survived or not (0 = No, 1 = Yes)
- **Pclass**: Passenger class (1 -> 1st class, 2 -> 2nd class, 3 -> 3rd class)
- **Sex**: Gender
- **Age**: Age
- **Fare**: Fare paid
- **Embarked**: Port of embarkation (C -> Cherbourg, Q -> Queenstown, S -> Southampton)
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Cabin**: Cabin number
- **Ticket**: Ticket number
"""
)

# Plot a bar chart to show survival rates amongst each passenger class
fig = px.bar(
    survival_rates,
    x="Pclass",
    y="Survived",
    labels={"Survived": "Survival Rate", "Pclass": "Passenger Class"},
    text="Survived",
    title="Survival Rates Across Different Passenger Classes on the Titanic",
)

# Update the text on each bar to display percentages
fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")

# Updating layout of the plot to add labels
fig.update_layout(
    xaxis_title="Passenger Class",
    yaxis_title="Survival Rate",
    xaxis=dict(
        tickmode="array",
        tickvals=[1, 2, 3],
        ticktext=["1st Class", "2nd Class", "3rd Class"],
    ),
)

st.plotly_chart(fig)

df_filtered_age = filtered_df.dropna(subset=["Age"])
# Scatter plot to show age and gender distribution by survival status
fig2 = px.scatter(
    df_filtered_age,
    x="Sex",
    y="Age",
    color="Survived",
    color_continuous_scale=px.colors.sequential.Cividis,
    labels={"Survived": "Survival Status"},
    title="Age and Gender Distribution by Survival Status on the Titanic",
)

# Update the color axis for clarity
fig2.update_coloraxes(colorbar_title="Survived<br>(1 = Survived, 0 = Not Survived)")

fig2.update_layout(
    width=950,
    height=800,
)

st.plotly_chart(fig2)
