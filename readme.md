
# Gemini Health App

The Gemini Health App is a Streamlit-based application that utilizes the Google Gemini Pro Vision API to analyze images of food items, calculate their total calories, and provide details of each food item along with their calorie intake.

## Features

- **Image Upload:** Upload an image of food items.
- **Input Prompt:** Provide an input prompt for a more accurate analysis.
- **Calorie Calculation:** Get the total calories of the food items in the image.
- **Detailed Analysis:** Receive detailed information on each food item and their respective calorie counts.

## Requirements

- Python 3.7+
- Streamlit
- google-generativeai
- python-dotenv
- Pillow

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/gemini-health-app.git
   cd gemini-health-app
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   - Create a `.env` file in the root directory of the project.
   - Add your Google API key in the `.env` file:

     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`.

3. **Use the sidebar** to input a prompt and upload an image of food items.

4. **Click on the "Tell me the total calories" button** to get the analysis.

## File Structure

```
gemini-health-app/
│
├── app.py                 # Main application file
├── requirements.txt       # Required packages
├── .env                   # Environment variables file
└── README.md              # This README file
```

## Example

1. **Input a prompt** in the sidebar.
2. **Upload an image** of food items.
3. **Click the button** to get a detailed analysis of the food items and their calorie counts.

## Deployment

The Gemini Health App is deployed and can be accessed at the following link:

[Gemini Health App](https://nutrition-appgi-tlkog4ddbf8fve2pdbynqv.streamlit.app/)

---

