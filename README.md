# Image-generation-using-stable-diffusion
#Generative Image Editing with Stable Diffusion
This Streamlit app allows users to generate and edit images using Stable Diffusion. It provides a user-friendly interface for text-to-image and image-to-image generation.
Features

    Text-to-image generation
    Image-to-image editing with reference images
    Adjustable parameters (steps, denoising strength)
    Real-time image preview

Installation
1. Install Stable Diffusion
Before running this app, you need to install Stable Diffusion locally. Follow these steps:

    Install Python 3.10.6 or later.
    Clone the Stable Diffusion Web UI repository:

    text
    git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

Navigate to the cloned directory:

text
cd stable-diffusion-webui

    Download a Stable Diffusion model (e.g., v1.5) and place it in the models/Stable-diffusion directory.
    Run the WebUI installation script:
        On Windows: webui-user.bat
        On Linux/Mac: ./webui.sh

2. Install Streamlit and dependencies

    Create a virtual environment (optional but recommended):

    text
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required packages:

text
pip install streamlit requests

Usage

    Ensure the Stable Diffusion WebUI is running on http://127.0.0.1:7860.
    Run the Streamlit app:

    text
    streamlit run app.py

    Open your web browser and navigate to the provided local URL (usually http://localhost:8501).
    Enter a prompt, adjust settings, and click "Generate Image" to create or edit images.

Code Structure

    app.py: The main Streamlit application file containing the user interface and API calls to Stable Diffusion.

Notes

    Make sure Stable Diffusion is running before starting the Streamlit app.
    The app uses the Stable Diffusion API endpoints for text-to-image and image-to-image generation.
    Adjust the url variable in the code if your Stable Diffusion instance is running on a different address.
