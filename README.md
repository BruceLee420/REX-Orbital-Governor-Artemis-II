# REX-Orbital Governor: Artemis II CDSS
**NASA Artemis II Human Research Data Methodology Challenge - Component 2**

## 🚀 Overview
This repository contains the functional code for the **REX-Orbital Governor**, a Clinical Decision Support System (CDSS). It utilizes **Functional Data Analysis (FDA)** to transform multi-modal IoT telemetry into a continuous risk-prediction model.

## 🛠️ Installation
This software requires **Python 3.10+**. 

1. **Clone the repository:**
   `git clone [YOUR_GITHUB_URL_HERE]`
2. **Install dependencies:**
   `pip install pandas numpy streamlit scipy plotly`

## 📊 How to Run
1. **Initialize the Data Matrix:**
   `python Component_2_build_matrix.py`
   *This script resamples and aligns the proxy data using FDA to create the `FTW_Artemis_Matrix.csv`.*

2. **Launch the CDSS Dashboard:**
   `streamlit run Component_2_app.py`
   *This launches the interactive dashboard at `localhost:8501` to view crew health telemetry.*

## 🔬 Methodology Note
This demonstration uses **Proxy Data Option 3 (Synthetic Data)** to simulate the high-dimensionality and small sample size (N=4) of the Artemis II mission profile.