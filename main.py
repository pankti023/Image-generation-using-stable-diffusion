import streamlit as st
import requests
import base64

url = "http://127.0.0.1:7860"
endpoint = "txt2img"

st.title("Generative Image Editing")

user_prompt = st.text_input("Enter a prompt:")
nsteps = st.slider("Steps", min_value=1, max_value=150, value=20)

referenceImage = st.checkbox("Generate using reference image?")

payload = {
        "prompt": user_prompt,
        "steps": nsteps,
    }
if referenceImage:
    endpoint = "img2img"
    referenceImageFile = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if referenceImageFile:
        st.image(referenceImageFile)
        image_bytes = referenceImageFile.getvalue()
        encodedImage = base64.b64encode(image_bytes).decode()
    denoise = st.slider("Denoise Strength", min_value = 0.0, max_value=1.0, value=0.75)
    payload["init_images"] = [encodedImage]
    payload["denoising_strength"] = denoise
    
else:
    payload.pop("init_images", None)

generateButton = st.button("Generate Image")

if generateButton:
    if user_prompt:
        response = requests.post(url=f'{url}/sdapi/v1/{endpoint}', json=payload)
        r = response.json()
        st.session_state.generatedImage = "data:image/png;base64,"+r['images'][0]
if st.session_state.get("generatedImage", False):
    st.image(st.session_state.generatedImage)