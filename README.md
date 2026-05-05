# REX-Orbital Governor: Artemis II CDSS
**NASA Artemis II Human Research Data Methodology Challenge - Component 2**
**Team:** FTW Labs / Freethinkers.ai

## 🚀 1. Project Overview
This repository contains the functional code for the **REX-Orbital Governor**, a Clinical Decision Support System (CDSS) designed for deep space human research. 

To satisfy the constraints of the Artemis II challenge (Small N=4 sample size, high-dimensionality, multi-modal fusion), this methodology utilizes **Functional Data Analysis (FDA)** to smooth and align discrete Internet of Things (IoT) telemetry and subjective behavioral data into a continuous risk-prediction model. 

In accordance with **Proxy Data Option 3 (Synthetic Data)**, this codebase generates astronaut-like multi-modal synthetic data to demonstrate the system's end-to-end capabilities.

Architecture details, including the **Thermal Kill-Shot** edge-node and **Biometric Mycelium** protocol, are documented in the REX-Orbital Governor Technical Blueprint submitted to the NASA portal.

## 🛠️ 2. Installation
This software requires **Python 3.10+**. 

1. **Clone the repository:**
   `git clone https://github.com/BruceLee420/REX-Orbital-Governor-Artemis-II.git`
2. **Install dependencies:**
   `pip install pandas numpy streamlit scipy plotly`

## 📊 3. How to Run
1. **Initialize the Data Matrix:**
   `python Component_2_build_matrix.py`
   *This script resamples and aligns the proxy data using FDA to create the `FTW_Artemis_Matrix.csv`.*

2. **Launch the CDSS Dashboard:**
   `streamlit run Component_2_app.py`
   *This launches the interactive dashboard at `localhost:8501` to view crew health telemetry.*
