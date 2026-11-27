"""
Key Question 1: Why and when do negative day-ahead electricity prices occur in Germany,
and how did their frequency evolve from 2022 to 2025?

Diagnostic Angle:
- Isolate all hourly intervals where `day_ahead_price < 0` across 2022–2025.
- Compare `renewable_share` (Solar + Wind) and `actual_consumption` during negative vs. positive price hours.
- Track year-over-year growth in negative price hours (2022 vs. 2023 vs. 2024 vs. 2025) to diagnose whether accelerating solar/wind capacity is outpacing grid flexibility.
- Test hypothesis: Negative prices cluster on sunny/windy weekends and holidays when industrial demand drops while renewable supply peaks.

Planned Charts:
- Heatmap: Frequency of negative prices by Hour of Day vs. Day of Week (or Month), filterable by year (2022–2025).
- Box Plot: Distribution of Renewable Share (%) and Demand (MWh) for Negative vs. Positive price hours.
"""

import streamlit as st

st.title("2. Why Do Negative Electricity Prices Happen? (2022–2025)")
st.info("Work in progress — Diagnostic analysis of negative day-ahead prices across 2022–2025.")