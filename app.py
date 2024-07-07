from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()  # Load all the environment variables

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

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Health App", layout="wide")

# Sidebar for user inputs
st.sidebar.header("Gemini Health App")
input = st.sidebar.text_input("Input Prompt:", key="input")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

submit = st.sidebar.button("Tell me the total calories")

# Main area for displaying content
st.title("Gemini Health App")
st.write("Upload an image of food items and provide an input prompt to get the total calories and details of each food item.")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

input_prompt = """
You are an expert nutritionist. You need to see the food items from the image
and calculate the total calories. Also, provide the details of each food item with calorie intake
in the following format:

1. Item 1 - number of calories
2. Item 2 - number of calories
----
----
"""

# If submit button is clicked
if submit:
    with st.spinner("Processing..."):
        try:
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input)
            st.subheader("The Response is:")
            st.write(response)
        except FileNotFoundError:
            st.error("No file uploaded. Please upload an image.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

