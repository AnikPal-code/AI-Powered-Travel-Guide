from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Initialize LLM
llm = ChatGroq(
    temperature=0,
    groq_api_key="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",  # Replace with your actual key
    model_name="llama-3.3-70b-versatile"
)

# Itinerary Prompt
itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel assistant. Create a {duration}-day trip itinerary for {city} based on user preferences: {interests}. Budget: {budget}. Starting from {starting_location}. Provide structured recommendations."),
    ("human", "Generate an itinerary for my trip."),
])

# Define Functions
def input_city(state):
    user_message = state["city"]
    return {**state, "messages": state["messages"] + [HumanMessage(content=user_message)]}

def input_interests(state):
    return {**state, "messages": state["messages"] + [HumanMessage(content=", ".join(state["interests"]))]}

def input_budget(state):
    return {**state, "messages": state["messages"] + [HumanMessage(content=state["budget"])]}

def input_duration(state):
    return {**state, "messages": state["messages"] + [HumanMessage(content=state["duration"])]}

def input_location(state):
    return {**state, "messages": state["messages"] + [HumanMessage(content=state["starting_location"])]}

def create_itinerary(state):
    response = llm.invoke(
        itinerary_prompt.format_messages(
            city=state["city"],
            interests=", ".join(state["interests"]),
            budget=state["budget"],
            duration=state["duration"],
            starting_location=state["starting_location"]
        )
    )
    return {**state, "itinerary": response.content, "messages": state["messages"] + [AIMessage(content=response.content)]}
