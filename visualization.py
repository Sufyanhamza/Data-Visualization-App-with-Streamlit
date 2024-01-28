import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import inspect

# Function to load CSV file
def load_data(file):
    df = pd.read_csv(file)
    return df

# Function to create Countplot
def create_countplot(data, column):
    fig, ax = plt.subplots()
    sns.countplot(data=data, x=column, ax=ax)
    st.pyplot(fig)
    
    # Button to display code
    if st.button("Show Code", key=f"countplot_{column}"):
        st.code(inspect.getsource(create_countplot))

# Function to create Pie Chart
def create_pie_chart(data, column):
    fig, ax = plt.subplots()
    data[column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)
    
    # Button to display code
    if st.button("Show Code", key=f"pie_chart_{column}"):
        st.code(inspect.getsource(create_pie_chart))

# Function to create Histogram
def create_histogram(data, column):
    fig, ax = plt.subplots()
    sns.histplot(data=data, x=column, kde=True, ax=ax)
    st.pyplot(fig)
    
    # Button to display code
    if st.button("Show Code", key=f"histogram_{column}"):
        st.code(inspect.getsource(create_histogram))

# Function to create Distplot
def create_distplot(data, column):
    fig, ax = plt.subplots()
    sns.distplot(data[column], ax=ax)
    st.pyplot(fig)
    
    # Button to display code
    if st.button("Show Code", key=f"distplot_{column}"):
        st.code(inspect.getsource(create_distplot))

# Function to create Boxplot
def create_boxplot(data, x_column, y_column):
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x=x_column, y=y_column, ax=ax)
    st.pyplot(fig)
    
    # Button to display code
    if st.button("Show Code", key=f"boxplot_{x_column}_{y_column}"):
        st.code("""
import seaborn as sns
import matplotlib.pyplot as plt

def create_boxplot(data, x_column, y_column):
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x='{}', y='{}', ax=ax)
    st.pyplot(fig)

create_boxplot(data, '{}', '{}')
        """.format(x_column, y_column, x_column, y_column))

# Function to create Scatterplot
def create_scatterplot(data, x_column, y_column):
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=x_column, y=y_column, ax=ax)
    st.pyplot(fig)
    
    # Button to display code
    if st.button("Show Code", key=f"scatterplot_{x_column}_{y_column}"):
        st.code(inspect.getsource(create_scatterplot))

# Function to create Bar Plot
def create_barplot(data, x_column, y_column):
    fig, ax = plt.subplots()
    sns.barplot(data=data, x=x_column, y=y_column, ax=ax)
    st.pyplot(fig)
    
    # Button to display code
    if st.button("Show Code", key=f"barplot_{x_column}_{y_column}"):
        st.code(inspect.getsource(create_barplot))

# Function to create HeatMap
def create_heatmap(data):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
    fig = plt.gcf()  # Get current figure
    st.pyplot(fig)
    
    # Button to display code
    if st.button("Show Code", key=f"heatmap"):
        st.code(inspect.getsource(create_heatmap))

# Function to create ClusterMap
def create_clustermap(data):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    clustermap_figure = sns.clustermap(numeric_data.corr(), cmap='coolwarm')
    
    # Pass the figure explicitly to st.pyplot()
    st.pyplot(clustermap_figure.fig)
    
    # Button to display code
    if st.button("Show Code", key=f"clustermap"):
        st.code(inspect.getsource(create_clustermap))


# Function to create Pairplot
def create_pairplot(data):
    pairplot_figure = sns.pairplot(data)
    
    # Pass the figure explicitly to st.pyplot()
    st.pyplot(pairplot_figure.fig)
    
    # Button to display code
    if st.button("Show Code", key=f"pairplot"):
        st.code(inspect.getsource(create_pairplot))

# Function to create Lineplot
def create_lineplot(data, x_column, y_column):
    fig, ax = plt.subplots()
    sns.lineplot(data=data, x=x_column, y=y_column, ax=ax)
    st.pyplot(fig)
    
    # Button to display code
    if st.button("Show Code", key=f"lineplot_{x_column}_{y_column}"):
        st.code(inspect.getsource(create_lineplot))

# Main function
def main():
    st.title('Data Visualization App')

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

    if uploaded_file is not None:
        data = load_data(uploaded_file)

        # Choose visualization option
        visualization_option = st.selectbox("Select Visualization", ["Countplot", "Pie Chart", "Histogram", "Distplot", "Boxplot", "Scatterplot", "Bar Plot", "HeatMap", "ClusterMap", "Pairplot", "Lineplot"])

        if visualization_option == "Countplot":
            column = st.selectbox("Select Column", data.columns)
            create_countplot(data, column)

        elif visualization_option == "Pie Chart":
            column = st.selectbox("Select Column", data.columns)
            create_pie_chart(data, column)

        elif visualization_option == "Histogram":
            column = st.selectbox("Select Column", data.columns)
            create_histogram(data, column)

        elif visualization_option == "Distplot":
            column = st.selectbox("Select Column", data.columns)
            create_distplot(data, column)

        elif visualization_option == "Boxplot":
            x_column = st.selectbox("Select X Column", data.columns)
            y_column = st.selectbox("Select Y Column", data.columns)
            create_boxplot(data, x_column, y_column)

        elif visualization_option == "Scatterplot":
            x_column = st.selectbox("Select X Column", data.columns)
            y_column = st.selectbox("Select Y Column", data.columns)
            create_scatterplot(data, x_column, y_column)

        elif visualization_option == "Bar Plot":
            x_column = st.selectbox("Select X Column", data.columns)
            y_column = st.selectbox("Select Y Column", data.columns)
            create_barplot(data, x_column, y_column)

        elif visualization_option == "HeatMap":
            create_heatmap(data)

        elif visualization_option == "ClusterMap":
            create_clustermap(data)

        elif visualization_option == "Pairplot":
            create_pairplot(data)

        elif visualization_option == "Lineplot":
            x_column = st.selectbox("Select X Column", data.columns)
            y_column = st.selectbox("Select Y Column", data.columns)
            create_lineplot(data, x_column, y_column)

# Run the app
if __name__ == '__main__':
    main()
