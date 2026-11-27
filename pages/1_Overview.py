"""
Page 1: Market Overview (Descriptive Analytics)
Goal: Establish the high-level baseline for Germany's electricity market (2022–2025).

Planned KPIs & Charts:
- Global KPIs: Total consumption (TWh), avg. renewable share (%), avg. day-ahead price (€/MWh), # of negative price hours.
- Stacked Area Chart: Generation mix over time (Solar, Wind Onshore/Offshore, Gas, Coal, Nuclear, Biomass, Hydro).
- Interactive Filters: Date range slider, resolution toggle (Hourly / Daily / Monthly).
"""

import streamlit as st

st.title("1. Market Overview (2022–2025)")
st.info("Work in progress — Descriptive baseline & global KPIs.")