import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
# נוסיף נתוני דוגמה לפרח רקפת (cyclamen), עם מאפיינים דומים
cyclamen_data = {
    "sepal_length": [2.5, 2.7, 2.6, 2.8, 2.9, 2.4, 2.6, 2.7, 2.5, 2.8],
    "sepal_width": [1.1, 1.0, 1.2, 1.2, 1.1, 1.3, 1.1, 1.2, 1.2, 1.1],
    "petal_length": [1.8, 2.0, 1.7, 2.1, 2.0, 1.9, 1.8, 2.1, 1.9, 2.0],
    "petal_width": [0.3, 0.4, 0.2, 0.3, 0.2, 0.4, 0.3, 0.2, 0.2, 0.3],
    "species": ["cyclamen"] * 10
}
cyclamen_df = pd.DataFrame(cyclamen_data)

# צור DataFrame מאוחד של איריס ורקפת
df = pd.concat([px.data.iris(), cyclamen_df], ignore_index=True)

# נתונים לדוגמה
df = px.data.iris()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("דאשבורד אינטרקטיבי - דוגמת פרחי איריס"),
    html.Label("בחר תכונה לציר X:"),
    dcc.Dropdown(
        id='x-axis',
        options=[{'label': col, 'value': col} for col in df.columns if df[col].dtype!='object'],
        value='sepal_width'
    ),
    html.Label("בחר תכונה לציר Y:"),
    dcc.Dropdown(
        id='y-axis',
        options=[{'label': col, 'value': col} for col in df.columns if df[col].dtype!='object'],
        value='sepal_length'
    ),
    dcc.Graph(id='scatter-plot'),
    html.Br(),
    dcc.Markdown("בחר תכונות ושחק איתן כדי לראות את הקשר בין מאפייני פרחי האיריס!")
])

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-axis', 'value'),
     Input('y-axis', 'value')]
)
def update_graph(x_axis, y_axis):
    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        color="species",
        title=f"{y_axis} לעומת {x_axis} לפי סוג פרח"
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)