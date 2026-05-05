import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import UnivariateSpline

@st.cache_data
def generate_crew_data():
    """Generates synthetic Artemis II proxy data for 4 crew members"""
    time_idx = pd.date_range("2026-06-01 08:00", periods=240, freq="1min")
    crew_data = {}
    
    for crew_id in ["CDR", "PLT", "MS1", "MS2"]:
        base_hr = np.random.normal(80, 5, 240) + np.linspace(0, 40, 240)
        gcr_rad = np.random.uniform(0.1, 0.5, 240)
        apm = np.random.normal(150, 10, 240) - np.linspace(0, 50, 240)
        
        spline_hr = UnivariateSpline(range(240), base_hr, s=100)
        smoothed_hr = spline_hr(range(240))
        
        cumulative_tax = np.cumsum(gcr_rad * 0.5) + (smoothed_hr * 0.1)
        risk_score = np.interp(cumulative_tax, (cumulative_tax.min(), cumulative_tax.max()), (0, 100))
        
        df = pd.DataFrame({
            "Timestamp": time_idx,
            "Heart_Rate_FDA": smoothed_hr,
            "Radiation_GCR": gcr_rad,
            "APM": apm,
            "Risk_Score": risk_score
        })
        crew_data[crew_id] = df
        
    return crew_data

st.set_page_config(page_title="Artemis II CDSS", layout="wide")
st.title("🚀 REX-Orbital Governor: Crew Health & Countermeasure AI")
st.markdown("Multimodal functional data analysis for Artemis II operational support.")

data = generate_crew_data()

st.sidebar.header("Mission Telemetry Controls")
selected_crew = st.sidebar.selectbox("Select Crew Member", ["CDR", "PLT", "MS1", "MS2"])
df = data[selected_crew]

col1, col2, col3 = st.columns(3)
current_risk = df["Risk_Score"].iloc[-1]
col1.metric("Current Risk Score", f"{current_risk:.1f}%", f"{current_risk - df['Risk_Score'].iloc[-2]:.1f}%")
col2.metric("FDA Smoothed HR", f"{df['Heart_Rate_FDA'].iloc[-1]:.0f} BPM")
col3.metric("Cognitive APM", f"{df['APM'].iloc[-1]:.0f}")

if current_risk > 75:
    st.error("⚠️ **CRITICAL ALARM:** Immune & Cognitive homeostasis failing. Initiate Optimized Nutritional Support Window immediately.")
else:
    st.success("✅ Crew homeostasis stable.")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Timestamp"], y=df["Risk_Score"], name="Risk Score", line=dict(color="red", width=3)))
fig.add_trace(go.Scatter(x=df["Timestamp"], y=df["Heart_Rate_FDA"], name="FDA Heart Rate", line=dict(color="blue", dash='dot')))
fig.add_trace(go.Scatter(x=df["Timestamp"], y=df["APM"], name="Cognitive APM", yaxis="y2", line=dict(color="green")))

fig.update_layout(
    title=f"Multimodal Fusion Telemetry: {selected_crew}",
    yaxis=dict(title="Biometrics & Risk"),
    yaxis2=dict(title="Cognitive Actions", overlaying="y", side="right"),
    template="plotly_dark",
    hovermode="x unified"
)
st.plotly_chart(fig, use_container_width=True)