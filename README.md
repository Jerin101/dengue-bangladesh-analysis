# Dengue in Bangladesh: Regional Trends and Climate Impact (2020-2025)

## Problem
Dengue cases in Bangladesh are rising and spreading beyond the usual monsoon season. This project analyzes which divisions are hit hardest, when cases peak, and how climate factors relate to outbreaks.

## Dataset
Monthly Division-Level Dengue Cases & Mortality with Climate and Environmental Indicators in Bangladesh (2020-2025), Mendeley Data.
Link: https://data.mendeley.com/datasets/cgwjshkx5k
576 rows: 8 divisions x 72 months.

## Tools
Python (pandas, matplotlib, seaborn), SQL (SQLite), Google Colab

## Live Dashboard
https://dengue-bangladesh-analysis-9nbqrfd7r7gsmg8dz6k8hc.streamlit.app/

## Key Findings
- Dhaka alone accounts for 55.4% of all recorded dengue cases (344,039 of 621,309).
- Dhaka has the highest death rate (0.63%), followed by Barishal (0.44%). Sylhet has the lowest (0.09%).
- About 81% of cases occur in just four months (August to November); October is the peak.
- 2023 was the worst year in the dataset (323,971 cases, 1,697 deaths).
- Temperature and humidity show only weak same-month correlation with cases (0.11 and 0.04), so they do not explain outbreaks on their own.

## Limitations
- Pollution level is fixed per division, so its effect cannot be separated from division/population effects.
- Two Dhaka months in 2023 show identical case counts (40,615); this may be a data entry issue and should be verified against the source.
- Correlation does not imply causation.

## Project Structure
- data/ : raw dataset and cleaned CSV
- notebooks/ : 01_cleaning.ipynb (data cleaning), 02_analysis.ipynb (analysis and charts)
- sql/ : queries.sql (8 SQL queries)
- images/ : charts

## How to Run
1. Open the notebooks in Google Colab.
2. Upload the files from the data/ folder.
3. Run the cells from top to bottom.
