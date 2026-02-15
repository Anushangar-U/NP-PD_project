# Colombo Climate Volatility & Trend Analyzer

## Project Summary
A comprehensive statistical analysis of 13 years (2010–2023) of historical weather data for Colombo, Sri Lanka. This project focuses on identifying climatic anomalies and long-term temperature shifts by processing a dataset of approximately 150,000 national records.

## Technical Core
* **Data Engineering:** Developed a robust cleaning pipeline using Pandas to handle missing values through sequential imputation (`ffill`/`bfill`) and global statistical means.
* **Vectorized Mathematics:** Leveraged NumPy to calculate the "Volatility Score"—measuring daily temperature deviation from the 13-year average at high computational speed.
* **Time-Series Smoothing:** Implemented a **30-day Rolling Average** to eliminate daily environmental "noise," revealing the underlying seasonal monsoon cycles of Sri Lanka.
* **Temporal Aggregation:** Engineered a Year-over-Year (YoY) comparison model to track the warming rate of Colombo over a decade.

## Tech Stack & Methods
* **Language:** Python 3.14
* **Libraries:** Pandas, NumPy
* **Statistical Logic:** * *Standard Deviation (σ):* Used as the benchmark for weather stability.
    * *Risk Detection:* Identified "Extreme Heat" events where volatility exceeded the 1.0 standard deviation threshold.
    * *Imputation:* Hybrid approach using neighborhood values and population means to ensure zero data loss.

## Project Structure
* `source/`: Contains the primary analysis script (`weather.py`).
* `data/`: Includes the source climate data and generated analytics CSVs.
* `README.md`: Project documentation.

## Key Findings
* **Volatility:** Colombo exhibits a stable temperature profile, but specific "Risk" clusters were identified in recent years using the Z-score logic.
* **Trends:** Successful identification of the hottest years on record by aggregating daily data into yearly averages, proving a measurable warming trend.
