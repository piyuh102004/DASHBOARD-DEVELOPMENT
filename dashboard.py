# Import necessary libraries
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the Iris dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Display the first five rows of the dataset
print(df.head())

# Initialize the Dash app
app = dash.Dash(__name__)

# Create visualizations
# Scatter plot: Sepal length vs Sepal width
fig_sepal = px.scatter(df, x='sepal_length', y='sepal_width', color='species',
                       title='Sepal Length vs Sepal Width')

# Scatter plot: Petal length vs Petal width
fig_petal = px.scatter(df, x='petal_length', y='petal_width', color='species',
                       title='Petal Length vs Petal Width')

# Box plot: Distribution of Sepal Length by Species
fig_box = px.box(df, x='species', y='sepal_length', color='species',
                 title='Distribution of Sepal Length by Species')

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Iris Dataset Dashboard'),
    
    html.Div(children='''
        An interactive dashboard for the Iris dataset.
    '''),
    
    dcc.Graph(
        id='sepal-scatter',
        figure=fig_sepal
    ),
    
    dcc.Graph(
        id='petal-scatter',
        figure=fig_petal
    ),
    
    dcc.Graph(
        id='sepal-box',
        figure=fig_box
    ),
    
    # Add more visualizations and components as needed
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
