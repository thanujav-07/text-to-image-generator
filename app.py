import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

st.set_page_config(page_title="Text to Image Generator")
st.title("🎨 Text to Image Generator")

prompt = st.text_area(
    "Enter image prompt",
    placeholder="A student studying with a laptop, digital art"
)

@st.cache_resource
def load_client():
    return InferenceClient(
        model="stabilityai/stable-diffusion-xl-base-1.0",
        token=HF_TOKEN
    )

client = load_client()

if st.button("Generate Image"):
    if not prompt.strip():
        st.error("Please enter a prompt")
    else:
        with st.spinner("Generating image..."):
            image = client.text_to_image(prompt)

        image.save("output.png")
        st.image(image, caption="Generated Image", width=700)

