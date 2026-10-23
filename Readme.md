🩺 Medical Prescription Image Enhancer & Analyzer
Overview

Doctors often write prescriptions by hand, and many times the medicine names become difficult to read because of poor handwriting, blurred photos, low lighting, or camera quality. This creates confusion for patients and pharmacists, increasing the chances of mistakes while purchasing or consuming medicines.

This project was built to solve that problem. It takes an image of a medical prescription, improves its readability, and extracts meaningful medical information using Google's Gemini Vision API. If the uploaded image is not related to the medical domain, the application rejects it instead of producing misleading results.

The goal of this project is to make handwritten prescriptions easier to understand while reducing the possibility of human error caused by unclear images.

The Problem

Medical prescriptions are frequently shared through messaging apps or captured using mobile phones. These images often suffer from:

Blurred or low-quality photographs
Poor lighting conditions
Difficult-to-read handwritten medicine names
Faded ink or partially visible text
Confusion while identifying prescribed medicines

For patients, this can lead to uncertainty. For pharmacists, it increases the time required to interpret prescriptions manually.

Solution

This application processes the uploaded prescription image and generates a detailed medical interpretation using Google's Gemini Vision model.

If image enhancement (OpenCV preprocessing) is enabled, the prescription image is first cleaned to improve visibility before analysis. The application then:

Accepts an uploaded prescription image.
Enhances readability of unclear prescription images.
Uses Gemini Vision to understand the medical content.
Generates a detailed description of the prescription.
Verifies whether the uploaded image belongs to the medical domain.
Prevents responses for unrelated images.

This makes the system useful for educational purposes, medical document understanding, and prescription digitization.

Features
Upload medical prescription images
Improves readability of unclear prescriptions
AI-powered medical image understanding
Medical image validation
User-friendly Flask web interface
Secure API key management using environment variables
Tech Stack
Technology	Purpose
Python	Backend Development
Flask	Web Framework
Google Gemini API	Medical Image Analysis
Pillow (PIL)	Image Processing
OpenCV (Optional if implemented)	Image Enhancement
HTML/CSS	Frontend
python-dotenv	Environment Variable Management
Project Workflow
User Uploads Prescription
            │
            ▼
Image Preprocessing (Optional OpenCV Enhancement)
            │
            ▼
Google Gemini Vision API
            │
            ▼
Medical Content Analysis
            │
            ▼
Medical Image Validation
            │
            ▼
Detailed Medical Description
            │
            ▼
Displayed on Web Interface
Folder Structure
Medical-Prescription-Analyzer/
│
├── app.py
├── .env
├── requirements.txt
├── templates/
│   └── index.html
├── static/
└── README.md
Environment Variables

Create a .env file in the project root.

GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
Installation

Clone the repository

git clone https://github.com/tyagivibhor111-hub/Medical-Prescription-Analyzer.git

Move into the project directory

cd Medical-Prescription-Analyzer

Install dependencies

pip install -r requirements.txt

Run the application

python app.py
Future Improvements
OCR integration for accurate medicine extraction
Automatic medicine database lookup
Drug interaction detection
PDF prescription support
Multi-language prescription recognition
Medicine dosage extraction
Downloadable medical report
Disclaimer

This project is intended for educational and research purposes only. The generated information should not replace professional medical advice. Always consult a qualified healthcare professional before making any medical decisions.

Author

Vibhor Tyagi
