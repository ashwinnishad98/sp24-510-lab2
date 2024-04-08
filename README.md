# Lab 2
An interactive application to view the dataset of the passengers aboard the Titanic. The dataset contains information pertaining to the passengers, including whether they survived or not. Filters are present on the sidebar, that users can apply which dynamically changes the graphs plotted. Two graphs are plotted in this application:

    1. Bar graph that shows the survival rates amongst passengers in each class i.e. 1st class, 2nd class, 3rd class.
    2. Scatter plot that shows the distribution of Age and Gender by Survival Status on the Titanic.


## How to Run
Open your terminal (if in VS Code, press ```ctrl + ` ```).

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## What's Included
- app.py: The entry point to the data visualization application. It contains streamlit code to display the graphs and plots, and dataframe operations using the Pandas library to filter specified data.


## Lessons Learned
- Using `plotly_express` package to plot graphs, and the various customization options it offers.
- Learned about Streamlit's dynamic behavior, when filters are applied to a dataframe.

## Questions
- Can interactions with the plots be reflected in the filter values?