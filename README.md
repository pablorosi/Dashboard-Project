
# German Electricity Market Analytics Dashboard (2022–2025)

An interactive descriptive and diagnostic analytics dashboard exploring Germany's wholesale electricity market using official data from the Federal Network Agency (*Bundesnetzagentur* — **SMARD.de**), built following the **CRISP-DM** methodology.

🔗 **Live Dashboard:** [Launch Streamlit App](https://dashboard-project-52gv8suykrux8dfmyzdjz2.streamlit.app/)



## Key Diagnostic Questions
1. **Negative Electricity Prices:** Why and when do negative day-ahead prices occur, and how did their frequency evolve from 2022 to 2025?
2. **Dunkelflaute & Price Spikes:** How strongly do low-renewable periods drive fossil fuel dispatch (gas & coal) and wholesale price surges?
3. **Post-Nuclear Shift:** How did Germany's generation mix and price volatility change after the April 15, 2023 nuclear phase-out (comparing 2022 vs. 2024–2025)?


## Dataset
* **Source:** [SMARD.de — Bundesnetzagentur](https://www.smard.de/en/downloadcenter/download-market-data/) (Actual Generation, Actual Consumption, and Day-Ahead Prices).
* **Timeframe & Grain:** `01/01/2022 – 12/31/2025` at hourly resolution (~35,064 rows).
* **Documentation:** Full schema, units, ranges, and licensing details are available in [`DATA_DICTIONARY.md`](./DATA_DICTIONARY.md).



## Tech Stack

* **Web Framework:** [Streamlit](https://streamlit.io/) (Multipage app)
* **Query Engine:** [DuckDB](https://duckdb.org/) (in-process SQL over Parquet)
* **Storage Format:** [Apache Parquet](https://parquet.apache.org/)
* **Visualizations:** [Plotly](https://plotly.com/python/)



## Project Structure
```text
app.py                  # Main Streamlit entry point
pages/                  # Multipage dashboard views (Overview + 3 Key Questions)
src/                    # Shared DuckDB data loader & Plotly chart helpers
notebooks/              # EDA & data preparation (CRISP-DM Phases 2–3)
data/processed/         # Cleaned, compressed Parquet dataset
DATA_DICTIONARY.md      # Column definitions, units, and source metadata
requirements.txt        # Python dependencies
```


## Run Locally

1. **Clone the repository:**
```bash
git clone https://github.com/pablorosi/Dashboard-Project.git
cd YOUR-REPO
```

2. **Create a virtual environment and install dependencies:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Launch the Streamlit app:**
```
streamlit run app.py
```
