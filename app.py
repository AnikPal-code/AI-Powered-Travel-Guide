import streamlit as st
from langchain.schema import HumanMessage
from your_travel_module import (
    input_city, input_interests, input_budget,
    input_duration, input_location, create_itinerary
)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main-container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            max-width: 700px;
            margin: auto;
        }
        h1 {
            color: #ff5a5f;
            text-align: center;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #ddd;
            background-color: #fff;
            color: black !important;  /* Ensures black text when typing */
            caret-color: black !important;  /* Keeps the cursor visible */
        }
        .stTextInput input::placeholder {
            color: #888 !important; /* Slightly darker placeholder */
            font-style: italic;
        }
        .stButton>button {
            background-color: #ff5a5f;
            color: white;
            font-weight: bold;
            padding: 12px;
            border-radius: 8px;
            border: none;
            width: 100%;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #e0484e;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1>🌍 AI Travel Planner</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #555;'>Plan your perfect trip with AI!</p>", unsafe_allow_html=True)

# Main Container for UI
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# User Input Fields
city = st.text_input("🏙️ Enter the city you want to visit:", placeholder="e.g., Mumbai")
budget = st.text_input("💰 Enter your budget (₹):", placeholder="e.g., ₹50000")
duration = st.text_input("📅 Enter trip duration (in days):", placeholder="e.g., 5")
starting_location = st.text_input("📍 Enter your starting location:", placeholder="e.g., Delhi")
interests = st.text_input("🎯 Enter your interests (comma-separated):", placeholder="e.g., beaches, food, adventure")

# Generate Itinerary Button
if st.button("✨ Generate Itinerary"):
    if city and interests and budget and duration and starting_location:
        st.write("📌 **Processing your request...**")

        # Initialize state
        state = {
            "messages": [HumanMessage(content=f"Planning a trip to {city}")],
            "city": city,
            "interests": [i.strip() for i in interests.split(",")],
            "budget": budget,
            "duration": duration,
            "starting_location": starting_location,
            "itinerary": "",
        }

        # Process each step
        state = input_city(state)
        state = input_interests(state)
        state = input_budget(state)
        state = input_duration(state)
        state = input_location(state)
        state = create_itinerary(state)

        # Display itinerary
        st.subheader("✈️ Your AI-Generated Itinerary:")
        st.write(state["itinerary"])

    else:
        st.warning("⚠️ Please fill in all fields to continue.")

st.markdown("</div>", unsafe_allow_html=True)
