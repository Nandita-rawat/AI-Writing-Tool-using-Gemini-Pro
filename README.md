# AI Writing Tool using Goggle Gemini✍️🤖

## Overview
The **AI Assistance Writing Tool** is a smart content generation application powered by **Gemini Pro**, designed to help users effortlessly create high-quality, engaging, and informative blog posts. The tool generates text-based content based on user input.

## Features
- **AI-Powered Content Generation**: Automatically generates blog posts based on user input.
- **Customizable Word Count**: Allows users to set the desired word limit.
- **Keyword Integration**: Ensures generated content includes user-defined keywords.
- **Interactive UI**: Built with Streamlit for a user-friendly interface.

## Tech Stack ⚙️
- **Frontend**: Streamlit
- **Backend**: Python, Google Gemini Pro API

## Installation & Setup 🚀
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Virtual environment (optional but recommended)

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ai-assistance-writing-tool.git
   cd ai-assistance-writing-tool
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your Google Gemini API key:
   - Create a file named `api_key.py` in the project folder.
   - Add the following line:
     ```python
     google_gemini_api_key = "your_api_key_here"
     ```
5. Run the application:
   ```sh
   streamlit run app.py
   ```




