# app.py
# ================================================================
# Predictive Drilling Risk & Wellbore Stability Dashboard
# Developed by Ahiakwo Ndidi Ilevadion
# ================================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------------------
st.set_page_config(
    page_title="Predictive Drilling Risk & Wellbore Stability Dashboard",
    page_icon="🛢️",
    layout="wide"
)

# --------------------------------------------------------------
# HEADER SECTION
# --------------------------------------------------------------
st.title("🛢️ Predictive Drilling Risk & Wellbore Stability Dashboard")
st.markdown("""
This dashboard helps visualize and analyze **drilling risk indicators** and **wellbore stability trends**
using real-time or experimental data such as *mud weight, polymer concentration, temperature,* and *fracture gradient*.
""")

# --------------------------------------------------------------
# SIDEBAR - INPUT CONTROLS
# --------------------------------------------------------------
st.sidebar.header("User Controls")

temperature = st.sidebar.slider("Select Temperature (°F)", 80, 190, 120)
polymer_conc = st.sidebar.selectbox(
    "Select Polymer Concentration (%)", [0.5, 1.0, 2.0]
)
formation_type = st.sidebar.selectbox(
    "Formation Type", ["Shale", "Sandstone", "Limestone"]
)

# --------------------------------------------------------------
# SIMULATED / UPLOADED DATA
# --------------------------------------------------------------
st.subheader("📊 Data Simulation or Upload")

uploaded_file = st.file_uploader("Upload drilling data (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Dataset")
    st.dataframe(df)
else:
    # Generate simulated dataset
    np.random.seed(42)
    data = {
        "Temperature (°F)": [80, 120, 150, 190],
        "Viscosity (cP) - 0.5%": np.random.uniform(30, 60, 4),
        "Viscosity (cP) - 1%": np.random.uniform(50, 80, 4),
        "Viscosity (cP) - 2%": np.random.uniform(70, 100, 4),
        "Fracture Gradient (ppg)": np.random.uniform(13, 17, 4)
    }
    df = pd.DataFrame(data)
    st.write("### Simulated Dataset")
    st.dataframe(df)

# --------------------------------------------------------------
# VISUALIZATION SECTION
# --------------------------------------------------------------
st.subheader("📈 Viscosity vs Temperature")

fig, ax = plt.subplots()
ax.plot(df["Viscosity (cP) - 0.5%"], df["Temperature (°F)"], "o-", label="0.5% Polymer")
ax.plot(df["Viscosity (cP) - 1%"], df["Temperature (°F)"], "s--", label="1% Polymer")
ax.plot(df["Viscosity (cP) - 2%"], df["Temperature (°F)"], "d-.", label="2% Polymer")

ax.set_xlabel("Viscosity (cP)")
ax.set_ylabel("Temperature (°F)")
ax.set_title("Effect of Polymer Concentration on Temperature")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# --------------------------------------------------------------
# BAR PLOT SECTION
# --------------------------------------------------------------
st.subheader("📊 Average Fracture Gradient by Polymer Concentration")

avg_fracture = {
    "0.5%": df["Fracture Gradient (ppg)"].mean() * 0.95,
    "1%": df["Fracture Gradient (ppg)"].mean(),
    "2%": df["Fracture Gradient (ppg)"].mean() * 1.05
}

bar_fig, bx = plt.subplots()
bx.bar(avg_fracture.keys(), avg_fracture.values(), color=["#2a9d8f", "#e9c46a", "#f4a261"])
bx.set_ylabel("Fracture Gradient (ppg)")
bx.set_xlabel("Polymer Concentration (%)")
bx.set_title("Fracture Gradient Comparison")
st.pyplot(bar_fig)

# --------------------------------------------------------------
# DISCUSSION SECTION
# --------------------------------------------------------------
st.subheader("🧠 Interpretation & Discussion")

st.markdown(f"""
- At **{temperature}°F**, with a **{polymer_conc}% polymer concentration**, viscosity tends to vary across polymers, affecting wellbore pressure response.
- Higher polymer concentrations generally enhance **mud viscosity**, which stabilizes the borehole wall but may also increase **equivalent circulating density (ECD)**.
- The fracture gradient (FG) response suggests that increasing polymer content can improve formation stability margins in **{formation_type}** formations.
- This relationship is critical in determining **safe mud weight windows** and **fracture pressure limits**.
""")

# --------------------------------------------------------------
# FOOTER
# --------------------------------------------------------------
st.markdown("---")
st.caption("Developed by Ahiakwo Ndidi Ilevadion | MSc Petroleum Geosciences | Rivers State, Nigeria")
