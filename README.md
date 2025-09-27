# NeoCura-Prototype
NeoCura SIH internal Demo - Health Chatbot

A simple health chatbot built with Streamlit and Hugging Face's Llama3-Med42-70B model.

## Features

- 🏥 AI-powered health assistant using medical-specialized Llama3 model
- 💬 Interactive chat interface with message history
- 🔒 Secure API integration with Hugging Face
- ⚠️ Built-in medical disclaimers for user safety
- 🎨 Clean, user-friendly Streamlit interface

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/veryveryjerry/NeoCura-Prototype.git
   cd NeoCura-Prototype
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Copy `.env.example` to `.env`
   - Get your Hugging Face token from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   - Add your token to the `.env` file:
     ```
     HF_TOKEN=your_actual_huggingface_token_here
     ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser:**
   - The app will automatically open at `http://localhost:8501`

## Usage

1. Type health-related questions in the chat input
2. Wait for the AI to process and respond
3. Continue the conversation as needed
4. Use "Clear Chat History" to start a new conversation

## Model Information

This chatbot uses the **m42-health/Llama3-Med42-70B** model from Hugging Face, which is specifically fine-tuned for medical and health-related conversations.

## Important Disclaimer

⚠️ **This chatbot is for informational purposes only and should not replace professional medical advice. Always consult with healthcare professionals for medical concerns.**

## Technical Stack

- **Frontend**: Streamlit
- **AI Model**: Hugging Face Llama3-Med42-70B
- **API**: OpenAI-compatible Hugging Face Inference API
- **Environment Management**: python-dotenv

## Contributing

This is a prototype for SIH (Smart India Hackathon). For contributions, please follow standard GitHub practices.
