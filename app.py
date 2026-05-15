import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["region"] = df["region"].str.lower().str.strip()

app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "background": "linear-gradient(135deg, #fff1f5, #eef6ff)",
        "minHeight": "100vh",
        "padding": "40px",
    },
    children=[
        html.Div(
            style={
                "maxWidth": "1050px",
                "margin": "auto",
                "backgroundColor": "white",
                "padding": "35px",
                "borderRadius": "20px",
                "boxShadow": "0 8px 30px rgba(0,0,0,0.12)",
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Visualiser",
                    style={
                        "textAlign": "center",
                        "color": "#2d3436",
                        "marginBottom": "8px",
                    },
                ),

                html.P(
                    "Explore Pink Morsel sales before and after the price increase on 15 January 2021.",
                    style={
                        "textAlign": "center",
                        "color": "#636e72",
                        "fontSize": "16px",
                        "marginBottom": "30px",
                    },
                ),

                html.Div(
                    children=[
                        html.Label(
                            "Filter by region:",
                            style={
                                "fontWeight": "bold",
                                "fontSize": "17px",
                                "color": "#2d3436",
                                "marginRight": "20px",
                            },
                        ),

                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            style={
                                "display": "inline-block",
                                "fontSize": "16px",
                                "color": "#2d3436",
                            },
                            inputStyle={
                                "marginRight": "6px",
                                "marginLeft": "14px",
                            },
                        ),
                    ],
                    style={
                        "textAlign": "center",
                        "marginBottom": "25px",
                        "padding": "15px",
                        "backgroundColor": "#f8f9fa",
                        "borderRadius": "12px",
                    },
                ),

                dcc.Graph(id="sales-line-chart"),
            ],
        )
    ],
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
        title = "Pink Morsel Sales Across All Regions"
    else:
        filtered_df = df[df["region"] == selected_region]
        title = f"Pink Morsel Sales in {selected_region.title()} Region"

    sales_by_date = (
        filtered_df.groupby("date")["sales"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    fig = px.line(
        sales_by_date,
        x="date",
        y="sales",
        markers=True,
        title=title,
        labels={"date": "Date", "sales": "Total Sales"},
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        hovermode="x unified",
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(size=14),
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
