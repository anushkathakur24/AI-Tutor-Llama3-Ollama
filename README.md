# My Personalized AI Tutor

This is a local AI tutor application built with Python, Streamlit, and Ollama/Llama 3.

## Features:
- Interactive chat interface
- Utilizes local Llama 3 model via Ollama
- David Goggins persona for tutoring (configurable)

## Setup and Running:

### Prerequisites:
- **Ollama:** Download and install Ollama from [ollama.ai](https://ollama.ai/).
- **Llama 3 Model:** Download the Llama 3 model by running `ollama run llama3` in your terminal.
- **Python 3.x:** Installed on your system.

### Installation:
1. Clone this repository:
   `git clone https://github.com/your-username/AI-Tutor-Llama3-Ollama.git`
2. Navigate into the project directory:
   `cd AI-Tutor-Llama3-Ollama`
3. Create and activate a virtual environment:
   `python -m venv .venv`
   `./.venv/Scripts/activate` (Windows) or `source ./.venv/bin/activate` (macOS/Linux)
4. Install required Python packages:
   `pip install -r requirements.txt`

### Running the Application:
1. Ensure your Ollama server is running in the background.
2. Activate your virtual environment (if not already active).
3. Run the Streamlit application:
   `streamlit run streamlit_app.py`
4. The app will open in your web browser.

## Files:
- `app.py`: Contains the core logic for communicating with Ollama.
- `streamlit_app.py`: Builds the Streamlit web interface.
- `requirements.txt`: Lists Python dependencies.
- `.env`: (Ignored) For sensitive configuration (e.g., API keys, if you were using external services).

---
*Built by [Anushka Thakur/anushkathakur24]*
