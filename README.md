# Housing Price Predictor

A beginner-friendly data analysis project that explores residential property prices and builds a simple regression model to estimate home values based on key housing features.

## Live App

Open the app using the provided project link. No installation or downloads are required just to view the dashboard.

## Project Overview

This project focuses on understanding the factors that influence residential house prices. Using a dataset of housing records, the analysis explores how characteristics such as area, bedroom count, hot water availability, and air conditioning relate to sale price.

The project combines:
- Exploratory Data Analysis (EDA)
- Data visualization
- Regression modeling
- An interactive Streamlit dashboard

The goal is to present the findings clearly and accessibly for a portfolio project aimed at entry-level data analysis roles.

## Dataset Description

The dataset used in this project is stored in:
- `data/housing_data.csv`

It contains 545 housing records and 5 variables:
- `price` — selling price of the property
- `area` — property size in square feet
- `bedrooms` — number of bedrooms
- `hot water` — whether the property has hot water heating (`yes` / `no`)
- `airconditioning` — whether the property has air conditioning (`yes` / `no`)

The dataset is complete and contains no missing values in the analyzed columns.

## Tools and Technologies

The project uses the following tools and libraries:
- Python
- Pandas
- NumPy
- Plotly
- Statsmodels
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Methodology

The project follows a straightforward data science workflow:

1. Load and inspect the dataset
2. Check for missing values and basic data quality issues
3. Summarize the dataset with descriptive statistics
4. Explore relationships between variables and sale price
5. Encode categorical variables for modeling
6. Build a multiple linear regression model
7. Evaluate the model’s performance
8. Present the results through an interactive dashboard

The model uses:
- Area
- Bedrooms
- Hot Water
- Air Conditioning

as predictors for the target variable:
- Price

## Key Features

- Interactive dashboard with multiple sections:
  - Project Overview
  - Dataset Summary
  - Visualizations
  - Regression Results
  - Price Predictor
- Distribution of home prices
- Area vs. price scatter plot with trendline
- Boxplots comparing price by:
  - number of bedrooms
  - hot water availability
  - air conditioning availability
- Correlation analysis
- Regression model summary
- House price prediction form

## Results and Insights

The project code and dashboard support the following findings:

- The dataset includes properties ranging from approximately ₹1.75M to ₹13.3M
- The average sale price is approximately ₹4.77M
- House area shows the strongest positive relationship with price
- Air conditioning appears to be associated with higher prices
- Bedrooms alone are not as strong a predictor as area
- The regression model explains about 48.1% of the variation in price
- The model’s RMSE is approximately ₹1.35M

These findings are presented in the dashboard and are based on the actual code in the repository.

## Repository Structure

```text
housing-price-predictor/
├── .streamlit/
│   └── config.toml
├── data/
│   └── housing_data.csv
├── images/
│   └── house_clip.png
├── notebooks/
│   └── data_explore.ipynb
├── app.py
├── charts.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to View the Project

To view the app, open the provided live app link in your browser.

If you want to run it locally instead, use:

```bash
streamlit run app.py
```

After installing the required dependencies, the app can be opened in the browser from the local Streamlit URL.

## Summary

This project demonstrates foundational data analysis and predictive modeling skills in a practical, portfolio-ready format. It shows the ability to:
- work with a real dataset
- explore relationships in the data
- build a regression model
- visualize findings clearly
- present results in an interactive dashboard

It is a suitable project for an entry-level data analyst portfolio because it combines technical analysis with clear communication and business-relevant insights.
