from dotenv import load_dotenv
load_dotenv()  # load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Health App", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .title {
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 700;
            color: #4a4a4a;
            text-align: center;
            padding: 20px 0;
        }
        .upload-box {
            border: 2px dashed #4a90e2;
            padding: 20px;
            text-align: center;
            background-color: #fff;
            border-radius: 10px;
        }
        .button {
            background-color: #4a90e2;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #357ab7;
        }
    </style>
""", unsafe_allow_html=True)

# Main app title
st.markdown("<div class='title'><h1>Gemini Health App</h1></div>", unsafe_allow_html=True)

# Input prompt
input = st.text_input("Input Prompt: ", key="input")

# File uploader with styled container
st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
st.markdown("</div>", unsafe_allow_html=True)

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Submit button with custom style
submit = st.button("Tell me the total calories", key="submit")

# Improved input prompt for the API
input_prompt = """
You are a highly skilled nutritionist. Analyze the food items in the provided image
and calculate the total calorie content. Additionally, give a detailed breakdown of each food item 
and its respective calorie count in the following format:

1. Item 1 - number of calories
2. Item 2 - number of calories
----
----
Provide any additional insights about the nutritional value of the food items if possible.
"""

# If submit button is clicked
if submit:
    try:
        with st.spinner('Processing...'):
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input)
        st.success("Processing complete!")
        with st.expander("See the response"):
            st.subheader("The Response is")
            st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
