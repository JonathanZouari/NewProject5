import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
print("this is Jonathan")

# נתוני דוגמה לפרח רקפת (cyclamen)
cyclamen_data = {
    "sepal_length": [2.5, 2.7, 2.6, 2.8, 2.9, 2.4, 2.6, 2.7, 2.5, 2.8],
    "sepal_width": [1.1, 1.0, 1.2, 1.2, 1.1, 1.3, 1.1, 1.2, 1.2, 1.1],
    "petal_length": [1.8, 2.0, 1.7, 2.1, 2.0, 1.9, 1.8, 2.1, 1.9, 2.0],
    "petal_width": [0.3, 0.4, 0.2, 0.3, 0.2, 0.4, 0.3, 0.2, 0.2, 0.3],
    "species": ["cyclamen"] * 10,
}
cyclamen_df = pd.DataFrame(cyclamen_data)

# נתוני דוגמה לוורדים (rose)
rose_data = {
    "sepal_length": [5.2, 5.5, 5.1, 5.8, 5.4, 5.6, 5.3, 5.7, 5.0, 5.9],
    "sepal_width": [2.8, 3.0, 2.7, 3.1, 2.9, 3.0, 2.8, 3.2, 2.6, 3.1],
    "petal_length": [5.5, 6.0, 5.2, 6.3, 5.8, 6.1, 5.4, 6.2, 5.0, 6.5],
    "petal_width": [1.8, 2.0, 1.6, 2.2, 1.9, 2.1, 1.7, 2.3, 1.5, 2.4],
    "species": ["rose"] * 10,
}
rose_df = pd.DataFrame(rose_data)

# DataFrame מאוחד: איריס + רקפת + ורדים
df = pd.concat([px.data.iris(), cyclamen_df, rose_df], ignore_index=True)

app = dash.Dash(__name__)

NUMERIC_COLUMNS = [col for col in df.columns if df[col].dtype != "object"]

app.layout = html.Div([
    html.H1("דאשבורד אינטרקטיבי — איריס, רקפת וורדים"),
    html.Label("בחר תכונה לציר X:"),
    dcc.Dropdown(
        id="x-axis",
        options=[{"label": col, "value": col} for col in NUMERIC_COLUMNS],
        value="sepal_width",
    ),
    html.Label("בחר תכונה לציר Y:"),
    dcc.Dropdown(
        id="y-axis",
        options=[{"label": col, "value": col} for col in NUMERIC_COLUMNS],
        value="sepal_length",
    ),
    dcc.Graph(id="scatter-plot"),
    html.Br(),
    dcc.Markdown(
        "בחר תכונות ושחק איתן כדי לראות את הקשר בין מאפייני הפרחים "
        "(איריס, רקפת וורדים)!"
    ),
])


@app.callback(
    Output("scatter-plot", "figure"),
    [Input("x-axis", "value"), Input("y-axis", "value")],
)
def update_graph(x_axis, y_axis):
    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        color="species",
        title=f"{y_axis} לעומת {x_axis} לפי סוג פרח",
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
