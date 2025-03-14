import streamlit as st
import pandas as pd
import pickle


# Load the trained model using pickle
from sklearn.utils import _safe_indexing

with open("GBSales9.pkl", "rb") as model_file:
    model = pickle.load(model_file, fix_imports=True)

# Title of the ap
st.title("🛒 Sales Prediction App")

# Sidebar for user input
st.sidebar.header("Enter Item Details")

# User input fields
Item_Weight = st.sidebar.number_input("Item Weight", min_value=0.0, max_value=50.0, step=0.1)
Item_Fat_Content = st.sidebar.selectbox("Item Fat Content", ["Lf", "Low fat", "rg", "regular"])
Item_Visibility = st.sidebar.number_input("Item Visibility", min_value=0.0, max_value=1.0, step=0.01)
Item_Type = st.sidebar.text_input("Item Type", "Snack Foods")
Item_MRP = st.sidebar.number_input("Item MRP", min_value=0.0, max_value=500.0, step=0.1)
Outlet_Establishment_Year = st.sidebar.number_input("Outlet Establishment Year", min_value=1985, max_value=2025, step=1)
Outlet_Size = st.sidebar.selectbox("Outlet Size", ["Supermarket Type 1", "Supermarket Type 2", "Supermarket 3", "Grocery Store"])
Outlet_Location_Type = st.sidebar.selectbox("Outlet Location Type", ["Tier1", "Tier 2", "Tier3"])
Outlet_Type = st.sidebar.text_input("Outlet Type", "Supermarket")

# Convert input into DataFrame
input_data = pd.DataFrame({
    "Item_Weight": [Item_Weight],
    "Item_Fat_Content": [Item_Fat_Content],
    "Item_Visibility": [Item_Visibility],
    "Item_Type": [Item_Type],
    "Item_MRP": [Item_MRP],
    "Outlet_Establishment_Year": [Outlet_Establishment_Year],
    "Outlet_Size": [Outlet_Size],
    "Outlet_Location_Type": [Outlet_Location_Type],
    "Outlet_Type": [Outlet_Type]
})

# Predict button
if st.sidebar.button("Predict Sales"):
    prediction = model.predict(input_data)[0]  # Predict sales
    st.success(f"Predicted Sales: **${prediction:.2f}**")
