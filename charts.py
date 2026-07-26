import plotly.express as px

def price_distribution(df):

    fig = px.histogram(
        df,
        x="price",
        nbins=20,
        color_discrete_sequence=["#c0cff1"]
    )

    return fig

def area_vs_price(df):

    fig = px.scatter(
        df,
        x="area",
        y="price",
        trendline="ols",
        color_discrete_sequence=["#c0cff1"]
    )

    fig.update_traces(marker=dict(size=8))

    fig.data[1].update(
    line=dict(
        color="#0B3D91",
        width=2))

    fig.update_layout(
        xaxis_title="Area (sq. ft.)",
        yaxis_title="Price (₹)"
    )

    return fig

def bedrooms_vs_price(df):

    fig = px.box(
        df,
        x="bedrooms",
        y="price",
        color_discrete_sequence=["#c0cff1"]
    )

    fig.update_layout(
        xaxis_title="Number of Bedrooms",
        yaxis_title="Price (₹)"
    )

    return fig

def hot_water_vs_price(df):
    
    fig = px.box(
        df,
        x="hot water",
        y="price",
        color_discrete_sequence=["#c0cff1"]
    )

    fig.update_layout(
        xaxis_title="Water Heating",
        yaxis_title="Price (₹)"
    )

    return fig


def air_conditioning_vs_price(df):

    fig = px.box(
        df,
        x="airconditioning",
        y="price",
        color_discrete_sequence=["#c0cff1"]
    )

    fig.update_layout(
        xaxis_title="Air Conditioning",
        yaxis_title="Price (₹)"
    )

    return fig

def correlation_matrix(df):
    corr_matrix = df.corr()

    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        color_continuous_scale="Blues"
    )

    return fig

def actual_vs_predicted(actual, predicted):

    fig = px.scatter(
        x=actual,
        y=predicted,
        labels={
            "x": "Actual Price",
            "y": "Predicted Price"
        },
        color_discrete_sequence=["#c0cff1"]
    )

    fig.add_shape(
        type="line",
        x0=actual.min(),
        y0=actual.min(),
        x1=actual.max(),
        y1=actual.max(),
        line=dict(color="red", dash="dash")
    )

    return fig
