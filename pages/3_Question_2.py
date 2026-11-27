"""
Key Question 2: How strongly do low-renewable periods (Dunkelflaute) drive fossil fuel
generation and price spikes?

Diagnostic Angle:
- Compute `residual_load = actual_consumption - (solar + wind_onshore + wind_offshore)`.
- Quantify the correlation (Pearson r / R²) between residual load, fossil dispatch (Gas + Coal), and `day_ahead_price` across 2022–2025 (controlling for the 2022 energy crisis).
- Drill down into the top 3–5 extreme price spike events in 2022–2025 to explain what happened on those exact dates.

Planned Charts:
- Scatter Plot + Trendline: Residual Load (MWh) vs. Day-Ahead Price (€/MWh), colored by year or season.
- Dual-Axis Time Series: Zoom-in on a specific Dunkelflaute week showing renewable drop, gas/coal ramp-up, and price surge.
"""

import streamlit as st

st.title("3. Dunkelflaute, Fossil Fuels & Price Spikes")
st.info("Work in progress — Correlation between residual load, fossil dispatch, and wholesale prices (2022–2025).")