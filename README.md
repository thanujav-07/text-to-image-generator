# 🎨 Text to Image Generator using Stable Diffusion & Streamlit

This project is a **Text-to-Image Generator web application** built using **Streamlit** and **Hugging Face’s Stable Diffusion XL** model.  
Users can enter a natural language prompt, and the system generates a high-quality image based on the description.

---

## 🚀 Features
- 📝 Convert text prompts into images
- 🎨 Powered by **Stable Diffusion XL**
- ⚡ Fast inference using **Hugging Face Inference API**
- 🖥️ Clean and interactive **Streamlit UI**
- 🔐 Secure API key handling using `.env`

---

## 🧠 How It Works

1. User enters a **text prompt** describing the image.
2. The prompt is sent to **Stable Diffusion XL** via Hugging Face’s inference API.
3. The model generates an image based on the prompt.
4. The image is displayed in the web interface and saved locally.

---

## 🏗️ Architecture Overview

- **Frontend**: Streamlit
- **Model**: `stabilityai/stable-diffusion-xl-base-1.0`
- **Inference**: Hugging Face `InferenceClient`
- **Secrets Management**: `python-dotenv`

---

## 📂 Project Structure

├── app.py # Main Streamlit application

├── .env # Stores Hugging Face API token (not committed)

├── README.md # Project documentation

└── output.png # Generated image (created at runtime)


---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/text-to-image-generator.git
cd text-to-image-generator

2️⃣ Create and Activate Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows

3️⃣ Install Dependencies
pip install streamlit python-dotenv huggingface-hub

4️⃣ Set Up Hugging Face Token
HF_TOKEN=your_huggingface_api_token_here

▶️ Running the Application
streamlit run app.py
Open your browser at:
http://localhost:8501

✨ Example Prompts
* A student studying with a laptop, digital art
* A futuristic city at night, cyberpunk style
* A robot reading books in a library

📈 Future Improvements
* Add image download button
* Support multiple image generations
* Add prompt history
* Deploy on Streamlit Cloud

👨‍💻 Author
Developed as a Generative AI mini project using Hugging Face and Streamlit.
