import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set up the title and description of the dashboard
st.title("Custom Rehabilitation Plan Dashboard")
st.write("This dashboard customizes rehabilitation plans based on patient profiles. Adjust the parameters in the sidebar to see tailored recommendations and progress projections.")

# Sidebar inputs for user data
st.sidebar.header("Patient Information")
age = st.sidebar.slider("Age", 18, 80, 30)
injury_type = st.sidebar.selectbox("Injury Type", ["Knee", "Shoulder", "Back"])
pain_level = st.sidebar.slider("Pain Level (1-10)", 1, 10, 5)
mobility_range = st.sidebar.slider("Mobility Range (%)", 0, 100, 50)

# Function to generate a mock recommendation based on user inputs
def generate_recommendation(age, injury_type, pain_level, mobility_range):
    if injury_type == "Knee":
        exercise = "Low-impact leg exercises"
    elif injury_type == "Shoulder":
        exercise = "Arm and shoulder mobility drills"
    else:
        exercise = "Core stability exercises"
        
    # Construct a recommendation dictionary based on the inputs
    recommendation = {
        "exercise": exercise,
        "frequency": f"{3 + (pain_level // 3)} times a week",
        "duration": f"{20 + (mobility_range // 5)} minutes per session",
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
recommendation = generate_recommendation(age, injury_type, pain_level, mobility_range)

# Display the rehabilitation plan recommendation
st.subheader("Recommended Rehabilitation Plan")
st.write("**Exercise Type:**", recommendation['exercise'])
st.write("**Frequency:**", recommendation['frequency'])
st.write("**Duration per Session:**", recommendation['duration'])

# Visualization of the projected mobility improvement over time
st.subheader("Expected Progress Over Time")
progress_data = recommendation['progress_data']
plt.figure(figsize=(8, 4))
plt.plot(progress_data['weeks'], progress_data['mobility_improvement'], marker='o', linestyle='-', color='b')
plt.xlabel("Weeks")
plt.ylabel("Mobility Improvement (%)")
plt.title("Projected Mobility Improvement")
st.pyplot(plt)
