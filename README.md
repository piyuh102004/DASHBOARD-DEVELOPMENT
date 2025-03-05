# Iris Dataset Dashboard

## Description
This project is an interactive dashboard built using Dash and Plotly to visualize the Iris dataset. The dashboard includes various visualizations to explore the relationships between different features of the Iris flowers.

## Installation Instructions
To run this dashboard, you need to have Python installed on your machine. You also need to install the required libraries. You can do this by running the following command:

```bash
pip install dash plotly pandas
```

## Usage Instructions
To start the dashboard, run the following command in your terminal:

```bash
python task_3/dashboard.py
```

Once the server is running, open your web browser and navigate to `http://127.0.0.1:8050/` to view the dashboard.

## Visualizations
The dashboard includes the following visualizations:
- **Scatter Plot**: Sepal length vs Sepal width, colored by species.
- **Scatter Plot**: Petal length vs Petal width, colored by species.
- **Box Plot**: Distribution of Sepal Length by Species.

## Detailed Explanation of the Code
The code in `dashboard.py` effectively creates an interactive dashboard that visualizes the Iris dataset, allowing users to explore relationships between different features of the flowers. The use of scatter plots and box plots provides actionable insights into the data.

### 1. Importing Libraries
The code begins by importing necessary libraries:
- `dash`: The main library for creating the dashboard.
- `dash_core_components` and `dash_html_components`: These are used to create interactive components and HTML elements in the dashboard.
- `plotly.express`: A high-level interface for creating visualizations easily.
- `pandas`: A library for data manipulation and analysis, used here to load and handle the dataset.

### 2. Loading the Dataset
The Iris dataset is loaded directly from a URL using `pd.read_csv()`. This dataset contains measurements of iris flowers, including sepal length, sepal width, petal length, petal width, and species.

### 3. Creating Visualizations
Three visualizations are created using Plotly Express:
- **Scatter Plot (Sepal Length vs Sepal Width)**: This plot helps visualize the relationship between sepal length and width, with points colored by species. It allows users to see how different species are distributed in terms of these two features.
- **Scatter Plot (Petal Length vs Petal Width)**: Similar to the first plot, this one visualizes the relationship between petal length and width, providing insights into how these features vary among species.
- **Box Plot (Distribution of Sepal Length by Species)**: This plot shows the distribution of sepal length for each species, highlighting the median, quartiles, and potential outliers. It provides a clear comparison of sepal lengths across different species.

### 4. Defining the Dashboard Layout
The layout of the dashboard is defined using `html.Div()`, which contains:
- A header (`html.H1`) for the title of the dashboard.
- A description of the dashboard.
- Three `dcc.Graph` components, each displaying one of the visualizations created earlier.

### 5. Running the App
The app is set to run with `app.run_server(debug=True)`, which starts the Dash server. The `debug=True` option allows for automatic reloading and provides helpful error messages during development.

## License
This project is licensed under the MIT License.
