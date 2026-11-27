"""
Key Question 3: How did Germany's generation mix and price volatility evolve after the
April 15, 2023 nuclear phase-out (comparing 2022 vs. 2024–2025)?

Diagnostic Angle:
- Germany shut down its last nuclear power plants on April 15, 2023 (right inside our 2022–2025 dataset).
- Compare full pre-shutdown year (2022) and transition year (2023) against two full post-shutdown years (2024–2025), controlling for seasonality and the 2022 gas crisis.
- Diagnose which energy sources absorbed the missing baseload and whether price volatility (std dev / IQR) increased or decreased post-shutdown.

Planned Charts:
- Grouped Bar / Delta Chart: Year-over-year change in TWh by energy source (2022 vs. 2023 vs. 2024 vs. 2025).
- Violin / Box Plot: Annual & monthly price distribution and volatility before vs. after April 15, 2023.
"""

import streamlit as st

st.title("4. Post-Nuclear Shift & Volatility (2022 vs. 2024–2025)")
st.info("Work in progress — Comparing generation mix and price volatility before and after the April 2023 nuclear phase-out.")