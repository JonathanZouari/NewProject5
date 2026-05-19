import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
print("This Is Ram")
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