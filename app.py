import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt

st.title("⚡ Smart Electricity Usage Monitor")
st.sidebar.header("Add New Appliance")

name = st.sidebar.text_input("Appliance Name")
power = st.sidebar.number_input("Power (W)", min_value=1)
hours = st.sidebar.number_input("Hours per day", min_value=1)

if st.sidebar.button("Add Appliance"):
    new_row = {"Appliance": name, "Power(W)": power, "Hours_per_day": hours}
    data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)

data = pd.read_csv("data.csv")

st.subheader("Appliance Data")
st.write(data)

data["Daily_Consumption_kWh"] = (data["Power(W)"] * data["Hours_per_day"]) / 1000

total_daily = data["Daily_Consumption_kWh"].sum()
monthly_units = total_daily * 30

st.subheader("Energy Consumption")
st.write(f"Daily Consumption:{total_daily:.2f} kWh")
st.write("Monthly Consumption:", monthly_units, "units")

rate = st.slider("Electricity Rate (₹ per unit)", 1, 15, 6)
bill = monthly_units * rate

st.subheader("Estimated Monthly Bill")
st.write("₹", bill)

st.subheader("Consumption by Appliance")
st.bar_chart(data.set_index("Appliance")["Daily_Consumption_kWh"])

if monthly_units > 300:
    st.warning("High usage! Reduce AC usage ⚠️")
else:
    st.success("Good usage! ⚡")