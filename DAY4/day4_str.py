'''Create a Streamlit dashboard using the vehicles.csv datafile that allows users to 
explore vehicle data dynamically. Filter the data by car manufacturer. 
*Imp - Understand the data and columns present in the data. 
1. User should be able to select the car manufacturer with the help of a 
select-box 
2. Filter the data based on the selected manufacturer and plot 4 types of 
graphs. 
3. The graphs should be relevant and should make sense. 
1. For ex. Plot a scatterplot of Engine size v/s fuel efficiency.'''
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv('./cars_clus.csv')  
# Pie Chart: Market Share by Manufacturer
st.subheader('Market Share by Manufacturer')
sales_by_manufacturer = df.groupby('manufact')['sales'].sum().sort_values(ascending=False)
top_n = 7
top_manufacturers = sales_by_manufacturer.head(top_n)
other_sales = sales_by_manufacturer[top_n:].sum()
top_manufacturers['others'] = other_sales
fig, ax = plt.subplots(figsize=(10,5))
ax.pie(top_manufacturers, labels=top_manufacturers.index, autopct='%1.1f%%')
ax.set_title('TOP 7 Market Share by Manufacturer')
st.pyplot(fig)

# Function to filter data by manufacturer
def filter_by_manufacturer(manufacturer):
    return df[df['manufact'] == manufacturer]

# Function to plot graphs
def plot_graphs(filtered_df):
    

    # Scatterplot: Engine size vs. Fuel efficiency
    st.subheader('Engine Size vs. Fuel Efficiency')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(filtered_df['engine_s'], filtered_df['mpg'])
    ax.set_title('Engine Size vs. Fuel Efficiency')
    ax.set_xlabel('Engine Size')
    ax.set_ylabel('Miles per Gallon')
    st.pyplot(fig)

    # Bar Chart: Average price by model
    st.subheader('Average Price by Model')
    avg_price = filtered_df.groupby('model')['price'].mean()
    fig, ax = plt.subplots(figsize=(10, 5))
    avg_price.plot(kind='bar', ax=ax)
    ax.set_title('Average Price by Model')
    ax.set_xlabel('Model')
    ax.set_ylabel('Average Price')
    st.pyplot(fig)

    # Line Chart: Resale value vs. Sales
    st.subheader('Resale Value vs. Sales')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(filtered_df['sales'], filtered_df['resale'])
    ax.set_title('Resale Value vs. Sales')
    ax.set_xlabel('Sales')
    ax.set_ylabel('Resale Value')
    st.pyplot(fig)

    # Histogram: Distribution of horsepower
    st.subheader('Distribution of Horsepower')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(filtered_df['horsepow'], bins=10, edgecolor='black')
    ax.set_title('Distribution of Horsepower')
    ax.set_xlabel('Horsepower')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    

# Streamlit UI elements
st.title('Car Data Analysis')

# Dropdown for selecting manufacturer
selected_manufacturer = st.selectbox('Select a Manufacturer:', df['manufact'].unique())

# Filter the dataframe based on the selected manufacturer
filtered_df = filter_by_manufacturer(selected_manufacturer)

# Plot the graphs
plot_graphs(filtered_df)
