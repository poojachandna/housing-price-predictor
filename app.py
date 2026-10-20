# importing libraries and charts
import streamlit as st
import pandas as pd
import statsmodels.api as sm
from charts import (price_distribution, area_vs_price, bedrooms_vs_price, hot_water_vs_price, air_conditioning_vs_price, correlation_matrix, actual_vs_predicted)
import plotly.graph_objects as go

#loading data
housing = pd.read_csv("data/housing_data.csv")

#encoding categorical variables into dummies
housing_encoded = housing.copy()

housing_encoded["hot water"] = housing_encoded["hot water"].map({"yes": 1, "no": 0})
housing_encoded["airconditioning"] = housing_encoded["airconditioning"].map({"yes": 1, "no": 0})

st.set_page_config(page_title="House Price Prediction & Analytics", page_icon=":house:", layout="wide")
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to:",
    [
        "Project Overview",
        "Dataset Summary",
        "Visualizations",
        "Regression Results",
        "Price Predictor"
    ]
)

# page 1 =  project overview
if page == "Project Overview":

    from pathlib import Path
    from PIL import Image

    hero = Image.open(Path("images") / "house_clip.png")

    left, center, right = st.columns([3, 2, 3])

    with center:
        st.image(hero, width=220)

    st.markdown(
    """
    <h1 style="text-align:center; margin-bottom:5px;">
    House Price Prediction & Analytics
    </h1>
    """,
    unsafe_allow_html=True,
    )

    st. markdown('''    <h3 style="font-weight:500;">
    Predicting Residential House Prices
    </h3>''' , unsafe_allow_html=True)

    st.markdown("""

This interactive dashboard explores the relationship between property
characteristics and residential house prices using **Exploratory Data Analysis**
and **Multiple Linear Regression**.
""")

    
    st.divider()

    st. markdown('''    <h3 style="font-weight:500;">
    About the Project
    </h3>''' , unsafe_allow_html=True)

    st.markdown("""
This project investigates how housing characteristics such as **area,
bedrooms, hot water heating, and air conditioning** influence residential
property prices.

The dashboard walks through the complete data science workflow—from
exploratory analysis and visualization to regression modelling and
interactive price prediction.
""")

    st.divider()

    st. markdown('''    <h3 style=" font-weight:500;">
    At a Glance
    </h3>''' , unsafe_allow_html=True)


    c1,c2,c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.metric("Properties Analysed","545")

    with c2:
        with st.container(border=True):
            st.metric("Predictor Variables","4")

    with c3:
        with st.container(border=True):
            st.metric("Model R²","48.1%")

    st.divider()

# page 2 = dataset summary

if page == "Dataset Summary":

    st.title("Dataset Summary")
    num_rows = housing.shape[0]
    num_columns = housing.shape[1]

    average_price = housing["price"].mean()

    minimum_price = housing["price"].min()

    maximum_price = housing["price"].max()

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.metric("Observations", f"{len(housing):,}")

    with col2:
        with st.container(border=True):
            st.metric("Variables", len(housing.columns))

    with col3:
        with st.container(border=True):
            st.metric(
                "Average Price",
                f"₹{housing['price'].mean()/1_000_000:.2f}M"
            )

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.metric(
                "Minimum Price",
                f"₹{housing['price'].min()/1_000_000:.2f}M"
            )

    with col2:
        with st.container(border=True):
            st.metric(
                "Maximum Price",
                f"₹{housing['price'].max()/1_000_000:.2f}M"
            )
            
    st.markdown("""
The dataset contains residential housing information used to
develop a multiple linear regression model for predicting
house prices.

Each row represents one property, while each column
describes a characteristic of that property.
""")

    st.subheader("Dataset Preview")

    st.dataframe(housing.head())

    with st.expander("View Complete Dataset"):
        st.dataframe(housing)

# page 3 = visualizations
if page == "Visualizations":

    st.title("Interactive Visualizations")
    st.markdown("""
Explore the relationships between different housing characteristics
and residential property prices through interactive charts.
""")
    st.divider()

    with st.container():

        st.markdown("###### Choose a Visualization")

        chart = st.selectbox(
            "",
            [   "Price Distribution",
                "Area vs Price",
                "Bedrooms vs Price",
                "Hot Water vs Price",
                "Air Conditioning vs Price",
                "Correlation Matrix"
            ]
        )
    st.divider()

    if chart == "Price Distribution":

        fig = price_distribution(housing)

        st.plotly_chart(fig, use_container_width=True)

        st.info("""
                **Insight:** 
                - Most houses are priced between ₹3M and ₹6M. 
                - The distribution is right-skewed, indicating a small number of luxury properties with substantially higher prices.""")

    if chart == "Area vs Price":

        fig = area_vs_price(housing)

        st.plotly_chart(fig, use_container_width=True)

        correlation = housing["area"].corr(housing["price"])

        col1, col2 = st.columns([1,4])

        with col1:
            with st.container(border=True):
                st.metric(
                    "Correlation Coefficient",
                    f"{correlation:.2f}"
                )

        with col2:
            st.info("""
                    **Insight:**
                    - House area has the strongest positive relationship with price in this dataset (r = 0.54).
                    - Although larger houses generally sell for higher prices, the relationship is only moderate, indicating that other factors also influence house values.""")
        
    if chart == "Bedrooms vs Price":

        correlation = housing_encoded["bedrooms"].corr(housing_encoded["price"])


        fig = bedrooms_vs_price(housing)

        st.plotly_chart(
                fig,
                width="stretch"
            )

        col1, col2 = st.columns([1,4])

        with col1:
            with st.container(border=True):
                st.metric(
                    "Correlation",
                    f"{correlation:.2f}"
                )

        with col2:
            st.info("""
            **Insight:** 

        • Median prices increase with bedroom count.

        • Price variability also increases as number of bedrooms increase.

        • The weak positive correlation (r = 0.12) suggests that bedroom count alone is not a sufficient predictor of house prices.
        """)

    if chart == "Hot Water vs Price":

        fig = hot_water_vs_price(housing)

        st.plotly_chart(fig, use_container_width=True)

        correlation = housing_encoded["hot water"].corr(housing_encoded["price"])
        col1, col2 = st.columns([1,4])

        with col1:
            with st.container(border=True):
                st.metric(
                    "Correlation Coefficient",
                    f"{correlation:.2f}"
                )

        with col2:
            st.info("""
                    **Insight:** 
                    - The box plot indicates that houses with hot water heating generally have a higher median selling price than those without hot water heating.
                    - The very weak positive correlation (r = 0.09) suggests that hot water heating alone is not a significant predictor of house prices, and other factors likely play a larger role.""")
        
    if chart == "Air Conditioning vs Price":
        
        fig = air_conditioning_vs_price(housing)

        st.plotly_chart(fig, use_container_width=True)

        correlation = housing_encoded["airconditioning"].corr(housing_encoded["price"])

        col1, col2 = st.columns([1,4])

        with col1:
            with st.container(border=True):
                st.metric(
                    "Correlation Coefficient",
                    f"{correlation:.2f}"
                )

        with col2:
            st.info("""
                **Insight:**
                - Houses equipped with air conditioning generally have higher selling prices, as indicated by the higher median and upward shift in the overall price distribution. 
                - The moderate positive correlation (r = 0.45), considerable overlap between the two groups and several high-priced outliers among houses without air conditioning, indicate that other factors may have a stronger influence on selling price.""")
        
    if chart == "Correlation Matrix":

        fig = correlation_matrix(housing_encoded)

        st.plotly_chart(fig, use_container_width=True)

        st.info("""
                **Insight:**
                - The correlation matrix indicates that house area has the strongest positive relationship with selling price (r = 0.54), followed by air conditioning (r = 0.45) and the number of bedrooms (r = 0.37). 
                - In contrast, hot water heating exhibits only a very weak positive correlation with price (r = 0.09), suggesting that it has little independent association with house prices.
                - The correlations among the independent variables are relatively low, indicating limited linear relationships between the predictors. This suggests that the variables provide distinct information and are unlikely to suffer from severe multicollinearity, making them suitable candidates for inclusion in a multiple regression model.""")

elif page == "Regression Results":
    st.title("Regression Results")

    st.write("""
    This section evaluates the performance of the multiple linear regression model
    used to predict residential house prices.
    """)

    st.subheader("Model Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.metric("R² Score", "0.481")

    with col2:
        with st.container(border=True):
            st.metric("Adjusted R²", "0.477")

    with col3:
        with st.container(border=True):
            st.metric("RMSE", "₹1.35M")
        

    st.info("""
**Interpretation**

• The model explains approximately **48%** of the variation in house prices.

• On average, predictions differ from actual prices by around **₹1.35 million**.
""")
    
    coef_df = pd.DataFrame({
        "Notation": ["X₁", "X₂", "D₁", "D₂"],
        "Variable": [
            "Area (sq. ft.)",
            "Bedrooms",
            "Hot Water",
            "Air Conditioning"
        ],
        "Coefficient": [
            "366.89",
            "613,000",
            "1,158,000",
            "1,352,000"
        ]
    })

    st.subheader("Regression Coefficients")

    st.dataframe(coef_df, use_container_width=True)

    st.subheader("Estimated Multiple Linear Regression Equation")

    st.latex(r'''
    \hat{Price}
    =
    579700
    +
    366.89X_1
    +
    613000X_2
    +
    1158000D_1
    +
    1352000D_2
    ''')

        # Define predictor variables
    X = housing_encoded[["area", "bedrooms", "hot water", "airconditioning"]]

    # Add intercept
    X = sm.add_constant(X)

    # Define target variable
    y = housing_encoded["price"]

    # Train regression model
    model = sm.OLS(y, X).fit()

    # Generate predictions
    housing_encoded["predicted_price"] = model.predict(X)

    # Calculate residuals
    housing_encoded["residuals"] = (
        housing_encoded["price"] -
        housing_encoded["predicted_price"]
    )

    st.subheader("Actual vs Predicted Prices")
    fig = actual_vs_predicted(
        housing_encoded["price"],
        housing_encoded["predicted_price"]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
            **Insight:**
            The scatter plot shows that the predicted prices generally follow the trend of the actual prices, indicating that the model captures the overall relationship between the predictors and house prices. However, there is noticeable dispersion around the diagonal line, suggesting that the model's predictions are not perfect and that other unaccounted factors may influence house prices.""")

    st.info("""
            **Key Findings:**

- **House area is the strongest predictor of house prices.** It exhibited the highest positive correlation with price (r = 0.54), indicating that larger houses generally command higher market values.

- **Air conditioning and hot water heating contribute significantly to property value.** The regression model estimated that houses with air conditioning and hot water heating were associated with average price premiums of approximately ₹1.35 million and ₹1.16 million, respectively, after controlling for other variables.

- **The number of bedrooms positively influences house prices**, although its relationship with price is weaker than that of house area. This suggests that total living space is a more informative predictor than bedroom count alone.

- **The multiple linear regression model was statistically significant** (p < 0.001) and explained approximately **48.1% of the variation** in house prices (R² = 0.481), indicating that the selected variables capture a substantial portion of the pricing differences.

- **Model diagnostics indicated an acceptable overall fit.** Residuals were centered around zero with no strong systematic patterns, although prediction errors increased slightly for higher-priced houses.

- **The model achieved an RMSE of approximately ₹1.35 million**, meaning that predicted prices differed from actual selling prices by about ₹1.35 million on average.

- **The remaining unexplained variation is likely due to omitted factors**, such as property location, construction quality, furnishing, parking availability, neighborhood characteristics, and other amenities that were not included in the dataset.""")

elif page == "Price Predictor":
    st.title("House Price Predictor")

    st.write("""
    Use the interactive form below to input property characteristics and predict the selling price of a house.
    """)

    with st.form("price_predictor_form"):
        area = st.number_input(
            "Enter the area of the house (in sq. ft.):",
            min_value=100,
            max_value=10000,
            value=1500,
            step=50
        )

        bedrooms = st.slider(
            label="Select the number of bedrooms:",
            min_value=1,
            max_value=10,
            value=3,
            step=1
        )

        hot_water = st.selectbox(
            "Does the house have hot water heating?",
            options=["yes", "no"]
        )

        air_conditioning = st.selectbox(
            "Does the house have air conditioning?",
            options=["yes", "no"]
        )

        submitted = st.form_submit_button("Predict Price")

        if submitted:
            hot_water = 1 if hot_water == "yes" else 0
            air_conditioning = 1 if air_conditioning == "yes" else 0

            # Predict price using the trained model
            predicted_price = (
            579700
            + 366.89 * area
            + 613000 * bedrooms
            + 1158000 * hot_water
            + 1352000 * air_conditioning
            )
            st.success(
            f"Estimated Selling Price: ₹{predicted_price:,.0f}"
            )

            st.info(f"""
            ### Prediction Summary

            Based on the selected features, the estimated selling price is
            **₹{predicted_price:,.0f}**.

            This prediction is generated using the multiple linear regression model
            developed from the housing dataset.
            """)