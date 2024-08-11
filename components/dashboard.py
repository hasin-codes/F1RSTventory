import streamlit as st
import pandas as pd
import plotly.express as px

def get_dashboard_data():
    # Placeholder function - will be replaced with actual data fetching later
    return pd.DataFrame({
        'Category': ['Electronics', 'Clothing', 'Books', 'Food'],
        'Inventory': [100, 200, 150, 300],
        'Sales': [50, 100, 75, 200]
    })

def show():
    st.header("Dashboard")

    # Overview
    st.subheader("Overview")
    col1, col2, col3 = st.columns(3)
    data = get_dashboard_data()
    
    with col1:
        st.metric("Total Inventory", data['Inventory'].sum())
    with col2:
        st.metric("Total Sales", data['Sales'].sum())
    with col3:
        st.metric("Categories", len(data))

    # Key Metrics
    st.subheader("Key Metrics")
    fig = px.bar(data, x='Category', y=['Inventory', 'Sales'], barmode='group')
    st.plotly_chart(fig)

    # Recent Activity
    st.subheader("Recent Activity")
    st.table(pd.DataFrame({
        'Date': ['2024-08-10', '2024-08-09', '2024-08-08'],
        'Action': ['New Order', 'Restocked', 'Product Added'],
        'Details': ['Order #1234', 'Electronics +50', 'New Book: "Python Mastery"']
    }))

if __name__ == "__main__":
    show()