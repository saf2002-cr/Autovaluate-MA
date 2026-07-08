import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Mock internal evaluation metrics for visual dashboard generation

np.random.seed(42)

y_actual = np.random.exponential(scale=100000, size=300) + 30000
y_pred = y_actual * np.random.normal(loc=1.0, scale=0.18, size=300)


def generate_actual_vs_pred():

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=y_actual,
            y=y_pred,
            mode="markers",
            marker=dict(
                color="#6366F1",
                opacity=0.6,
                size=7,
                line=dict(width=1, color="#1E293B"),
            ),
            name="Data Observations",
        )
    )

    min_val = min(y_actual.min(), y_pred.min())
    max_val = max(y_actual.max(), y_pred.max())

    fig.add_trace(
        go.Scatter(
            x=[min_val, max_val],
            y=[min_val, max_val],
            line=dict(color="#EF4444", width=2, dash="dash"),
            name="Identity Baseline (Ideal)",
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=10, b=20),
        height=300,
        xaxis=dict(
            gridcolor="rgba(255,255,255,0.05)",
            title="Actual Real Price (MAD)",
        ),
        yaxis=dict(
            gridcolor="rgba(255,255,255,0.05)",
            title="Model Prediction Target",
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
    )

    return fig


def generate_price_dist():

    fig = px.histogram(
        x=y_actual,
        nbins=40,
        color_discrete_sequence=["#10B981"],
        marginal="box",
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=10, b=20),
        height=300,
        xaxis=dict(
            gridcolor="rgba(255,255,255,0.05)",
            title="Price Ranges (MAD)",
        ),
        yaxis=dict(
            gridcolor="rgba(255,255,255,0.05)",
            title="Total Volume Sample Density",
        ),
    )

    return fig


def generate_brand_dist():

    brands = [
        "Dacia",
        "Renault",
        "Peugeot",
        "Volkswagen",
        "Citroen",
        "Ford",
        "Hyundai",
        "Fiat",
        "Mercedes-Benz",
        "BMW",
    ]

    volumes = [3400, 2900, 2100, 1850, 1200, 950, 800, 550, 400, 350]

    fig = px.bar(
        x=brands,
        y=volumes,
        color=volumes,
        color_continuous_scale="Purples",
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=10, b=20),
        height=300,
        coloraxis_showscale=False,
        xaxis=dict(title="Manufacturer Category Label"),
        yaxis=dict(
            gridcolor="rgba(255,255,255,0.05)",
            title="Active Scrape Records",
        ),
    )

    return fig


def generate_city_dist():

    cities = [
        "Casablanca",
        "Rabat",
        "Marrakech",
        "Tanger",
        "Agadir",
        "Fes",
    ]

    proportions = [45, 18, 12, 10, 8, 7]

    fig = px.pie(
        names=cities,
        values=proportions,
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hole=0.4,
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=10, b=10),
        height=300,
        showlegend=False,
    )

    return fig