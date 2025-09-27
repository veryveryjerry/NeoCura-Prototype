import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="NeoCura Health Chatbot",
    page_icon="🏥",
    layout="centered"
)

# Initialize OpenAI client with Hugging Face endpoint
@st.cache_resource
def get_openai_client():
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        st.error("HF_TOKEN environment variable is not set. Please set your Hugging Face token.")
        st.stop()
    
    return OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=hf_token,
    )

def get_chat_response(messages):
    """Get response from the health chatbot model."""
    try:
        client = get_openai_client()
        completion = client.chat.completions.create(
            model="m42-health/Llama3-Med42-70B:featherless-ai",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error getting response from the model: {str(e)}")
        return None

def main():
    st.title("🏥 NeoCura Health Chatbot")
    st.write("Welcome to NeoCura, your AI health assistant. Ask me health-related questions!")
    
    # Add disclaimer
    st.warning("⚠️ **Disclaimer**: This chatbot is for informational purposes only and should not replace professional medical advice. Always consult with healthcare professionals for medical concerns.")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful medical AI assistant. Provide accurate, helpful health information while always emphasizing the importance of consulting healthcare professionals for serious medical concerns."}
        ]
        st.session_state.chat_history = []
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me a health-related question..."):
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_chat_response(st.session_state.messages)
                
                if response:
                    st.markdown(response)
                    # Add assistant response to chat history
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Sidebar with information
    with st.sidebar:
        st.markdown("### About NeoCura")
        st.write("NeoCura is an AI-powered health assistant built using:")
        st.write("- **Streamlit** for the web interface")
        st.write("- **Hugging Face** Llama3-Med42-70B model")
        st.write("- **OpenAI-compatible API** for model interaction")
        
        st.markdown("### How to use")
        st.write("1. Type your health-related question in the chat input")
        st.write("2. Wait for the AI to provide a response")
        st.write("3. Continue the conversation as needed")
        
        if st.button("Clear Chat History"):
            st.session_state.messages = [
                {"role": "system", "content": "You are a helpful medical AI assistant. Provide accurate, helpful health information while always emphasizing the importance of consulting healthcare professionals for serious medical concerns."}
            ]
            st.session_state.chat_history = []
            st.rerun()

if __name__ == "__main__":
    main()