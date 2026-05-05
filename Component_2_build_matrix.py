import pandas as pd
import numpy as np

def build_multimodal_matrix():
    # 1. Ingest Proxy Datasets (Simulated or Open-Source)
    try:
        wear = pd.read_csv("wearables.csv", parse_dates=["timestamp"]).set_index("timestamp")
        survey = pd.read_csv("survey.csv", parse_dates=["timestamp"]).set_index("timestamp")
        tele = pd.read_csv("telemetry.csv", parse_dates=["timestamp"]).set_index("timestamp")
        
        # 2. Resample and Align (The FDA approach)
        wear_1m = wear.resample("1min").mean()
        tele_1m = tele.resample("1min").mean()
        survey_1m = survey.resample("1min").ffill()
        
        # 3. Merge into the Time-Aligned Matrix
        df = wear_1m.join([survey_1m, tele_1m], how="outer")
        df = df.interpolate(limit_direction="both")
    except FileNotFoundError:
        print("Mock CSVs not found. Creating a blank matrix shell for testing...")
        time_idx = pd.date_range("2026-06-01 08:00", periods=240, freq="1min")
        df = pd.DataFrame(index=time_idx)
        df["heart_rate"] = np.random.normal(80, 5, 240)
        df["optimism_score"] = 5
    
    # 4. Feature Engineering: The Metabolic Tax & Rolling Stress
    df["hr_rolling_10"] = df["heart_rate"].rolling(10, min_periods=1).mean()
    df["caloric_burn_rate"] = np.where(df["hr_rolling_10"] > 110, 8.5, 1.2) 
    df["cumulative_deficit"] = df["caloric_burn_rate"].cumsum()
    
    # 5. Define the Operational Trigger
    df["intervention_flag"] = np.where(
        (df["hr_rolling_10"] > 120) & 
        (df["optimism_score"] <= 4) & 
        (df["cumulative_deficit"] > 500), 
        1, 0
    )
    
    # FIX: Updated pandas 2.0+ syntax for backfilling missing data
    df.bfill(inplace=True)
    
    df.to_csv("FTW_Artemis_Matrix.csv")
    print("Matrix successfully built. Ready for sequence modeling.")
    return df

if __name__ == "__main__":
    matrix = build_multimodal_matrix()