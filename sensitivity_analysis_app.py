import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to perform Monte Carlo simulation
def monte_carlo_simulation(revenue_mean, revenue_sd, turnover_mean, turnover_sd, morale_mean, morale_sd, leadership_mean, leadership_sd, n_simulations):
    # Generate random samples
    client_revenue_gain = np.random.normal(revenue_mean, revenue_sd, n_simulations)
    employee_turnover_cost = np.random.normal(turnover_mean, turnover_sd, n_simulations)
    morale_impact = np.random.normal(morale_mean, morale_sd, n_simulations)
    leadership_pipeline_impact = np.random.normal(leadership_mean, leadership_sd, n_simulations)

    # Calculate total impact
    total_impact = (
        client_revenue_gain +
        employee_turnover_cost +
        morale_impact +
        leadership_pipeline_impact
    )
    
    return total_impact

# Streamlit app UI
st.title("Interactive Sensitivity Analysis Dashboard")
st.sidebar.header("Simulation Parameters")

# Input sliders for sensitivity parameters
n_simulations = st.sidebar.slider("Number of Simulations", 1000, 10000, 5000, step=1000)
revenue_mean = st.sidebar.slider("Mean Revenue Gain (M)", 1.0, 10.0, 5.0, step=0.1)
revenue_sd = st.sidebar.slider("Revenue Gain SD (M)", 0.5, 5.0, 2.0, step=0.1)
turnover_mean = st.sidebar.slider("Mean Turnover Cost (M)", -5.0, 0.0, -2.0, step=0.1)
turnover_sd = st.sidebar.slider("Turnover Cost SD (M)", 0.5, 3.0, 1.0, step=0.1)
morale_mean = st.sidebar.slider("Mean Morale Impact (M)", -3.0, 0.0, -1.0, step=0.1)
morale_sd = st.sidebar.slider("Morale Impact SD (M)", 0.1, 1.0, 0.5, step=0.1)
leadership_mean = st.sidebar.slider("Mean Leadership Impact (M)", -2.0, 0.0, -0.5, step=0.1)
leadership_sd = st.sidebar.slider("Leadership Impact SD (M)", 0.1, 1.0, 0.3, step=0.1)

# Run Monte Carlo simulation
total_impact = monte_carlo_simulation(
    revenue_mean, revenue_sd,
    turnover_mean, turnover_sd,
    morale_mean, morale_sd,
    leadership_mean, leadership_sd,
    n_simulations
)

# Display results
st.subheader("Simulation Results")
mean_impact = np.mean(total_impact)
std_impact = np.std(total_impact)
st.write(f"**Mean Total Impact:** {mean_impact:.2f}M")
st.write(f"**Standard Deviation:** {std_impact:.2f}M")

# Plot histogram of total impact
st.subheader("Distribution of Total Impact")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(total_impact, bins=50, kde=True, color='skyblue', ax=ax)
ax.axvline(mean_impact, color='red', linestyle='dashed', linewidth=1.5, label=f"Mean: {mean_impact:.2f}M")
ax.set_title("Monte Carlo Simulation: Total Financial Impact", fontsize=14)
ax.set_xlabel("Total Financial Impact (M)", fontsize=12)
ax.set_ylabel("Frequency", fontsize=12)
ax.legend()
st.pyplot(fig)

# Heatmap Example (Optional)
st.subheader("Sensitivity Heatmap (Optional)")
heatmap_data = {
    "Revenue Mean (M)": [revenue_mean],
    "Turnover Mean (M)": [turnover_mean],
    "Mean Total Impact (M)": [mean_impact],
}
heatmap_df = pd.DataFrame(heatmap_data)
st.table(heatmap_df)

