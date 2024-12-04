import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io

# Set up the title and description of the dashboard
st.title("Custom Rehabilitation Plan Dashboard")
st.write("This dashboard customizes rehabilitation plans based on patient profiles. Adjust the parameters in the sidebar to see tailored recommendations and progress projections.")

# Sidebar inputs for user data
st.sidebar.header("Patient Information")
age = st.sidebar.slider("Age", 18, 80, 30)
injury_type = st.sidebar.selectbox("Injury Type", ["Knee", "Shoulder", "Back"])
pain_level = st.sidebar.slider("Pain Level (1-10)", 1, 10, 5)
mobility_range = st.sidebar.slider("Mobility Range (%)", 0, 100, 50)

# Additional Patient History Input
st.sidebar.subheader("Additional Information")
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Moderately Active", "Very Active"])

# Function to generate a mock recommendation based on user inputs
def generate_recommendation(age, injury_type, pain_level, mobility_range, weight, activity_level):
    if injury_type == "Knee":
        exercise = "Low-impact leg exercises"
    elif injury_type == "Shoulder":
        exercise = "Arm and shoulder mobility drills"
    else:
        exercise = "Core stability exercises"

    activity_factor = 1 if activity_level == "Sedentary" else (1.2 if activity_level == "Moderately Active" else 1.5)
    duration = int((20 + (mobility_range // 5)) * activity_factor)
    
    recommendation = {
        "exercise": exercise,
        "frequency": f"{3 + (pain_level // 3)} times a week",
        "duration": f"{duration} minutes per session",
        "progress_data": {
            "weeks": [1, 2, 3, 4],
            "mobility_improvement": [
                mobility_range * 0.2, 
                mobility_range * 0.4, 
                mobility_range * 0.6, 
                mobility_range * 0.8
            ]
        }
    }
    return recommendation

# Generate the recommendation using the function
recommendation = generate_recommendation(age, injury_type, pain_level, mobility_range, weight, activity_level)

# Display the rehabilitation plan recommendation
st.subheader("Recommended Rehabilitation Plan")
st.write("**Exercise Type:**", recommendation['exercise'])
st.write("**Frequency:**", recommendation['frequency'])
st.write("**Duration per Session:**", recommendation['duration'])

# Visualization of the projected mobility improvement over time
st.subheader("Expected Progress Over Time")
progress_data = recommendation['progress_data']

# User-Reported Progress
st.subheader("Input Your Progress")
user_progress = [
    st.number_input(f"Week {i+1} Mobility Improvement (%)", min_value=0, max_value=100, value=0) 
    for i in range(4)
]

# Create a DataFrame for visualization
df = pd.DataFrame({
    "Weeks": progress_data['weeks'],
    "Projected Mobility": progress_data['mobility_improvement'],
    "User Progress": user_progress
})

# Plot using seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 4))
sns.lineplot(data=df, x="Weeks", y="Projected Mobility", marker='o', label="Projected")
sns.lineplot(data=df, x="Weeks", y="User Progress", marker='x', label="User Progress")
plt.title("Projected vs Actual Mobility Improvement")
plt.xlabel("Weeks")
plt.ylabel("Mobility Improvement (%)")
st.pyplot(plt)

# Export the rehabilitation plan as text
st.subheader("Export Rehabilitation Plan")
plan_text = f"""
Custom Rehabilitation Plan
--------------------------
Age: {age}
Injury Type: {injury_type}
Pain Level: {pain_level}
Mobility Range: {mobility_range}%

Recommended Plan:
Exercise: {recommendation['exercise']}
Frequency: {recommendation['frequency']}
Duration per session: {recommendation['duration']}
"""
st.download_button(
    label="Download Plan",
    data=plan_text,
    file_name="rehabilitation_plan.txt",
    mime="text/plain"
)
