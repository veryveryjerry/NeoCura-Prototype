#!/usr/bin/env python3
"""
NeoCura Health Chatbot Launcher
Simple script to launch the Streamlit application with proper configuration.
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if required packages are installed."""
    try:
        import streamlit
        import openai
        from dotenv import load_dotenv
        print("✅ All required packages are installed.")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists and has HF_TOKEN."""
    if not os.path.exists('.env'):
        print("❌ .env file not found.")
        print("Please copy .env.example to .env and add your Hugging Face token.")
        return False
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    hf_token = os.environ.get('HF_TOKEN')
    if not hf_token or hf_token == 'your_huggingface_token_here':
        print("❌ HF_TOKEN not set in .env file.")
        print("Please add your Hugging Face token to the .env file.")
        return False
    
    print("✅ Environment configuration is valid.")
    return True

def main():
    """Main launcher function."""
    print("🏥 NeoCura Health Chatbot Launcher")
    print("=" * 40)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check environment
    if not check_env_file():
        sys.exit(1)
    
    # Launch Streamlit
    print("🚀 Starting NeoCura Health Chatbot...")
    print("The application will open in your default browser.")
    print("Press Ctrl+C to stop the application.")
    print("-" * 40)
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.headless", "false",
            "--server.port", "8501"
        ])
    except KeyboardInterrupt:
        print("\n👋 NeoCura Health Chatbot stopped.")

if __name__ == "__main__":
    main()