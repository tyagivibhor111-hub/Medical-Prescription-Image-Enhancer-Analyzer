import os
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, request, render_template, render_template_string, redirect, url_for

# Load environment variables from .env
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))# Configure Google Generative AI

vision_model = genai.GenerativeModel("gemini-1.5-flash")
text_model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

# Function to generate content
def gen_image(image):
    prompt = """
    You are a medical document analyzer.

    Analyze the uploaded medical prescription or report.

    Tasks:
    - Read all visible text.
    - Identify medicine names.
    - If some medicine names are blurred or partially visible,
      infer them only if you are reasonably confident.
    - Mention whenever something is unreadable instead of guessing.
    - Explain the prescription in simple language.
    - Do not provide false information.
    """

    response = vision_model.generate_content([prompt, image])

    return response.text

def validate(response_text):
    prompt = f"""
    Determine whether the following content is related to medicine,
    healthcare, prescriptions or hospitals.

    Reply ONLY with:

    Yes

    or

    No

    Content:
    {response_text}
    """

    response = text_model.generate_content(prompt)

    return response.text.strip()

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        uploaded_file = request.files.get("file")

    if uploaded_file.filename == "":
        return render_template(
            "index.html",
            response_text="Please upload an image."
        )

    image = Image.open(uploaded_file)

    response_text = gen_image(image)

    validation = validate(response_text)

    if validation.lower() == "yes":
        return render_template(
            "index.html",
            response_text=response_text
        )

    return render_template(
        "index.html",
        response_text="The uploaded image does not appear to be a medical prescription or report."
    )


if __name__ == '__main__':
    app.run(debug=True)