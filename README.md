#  Skin Disease Detector 

A simple and basic Python, artificial intelligence and machine learning project that shows the skin disease detection using image file details. The model analyse the image URl path and predicts the type of skin disease it has along with basic information and precautions. This project is built mainly for learning purposes.

---

## About the Project

This program takes an image file as input and tries to predict a possible skin disease based on:

- The **image filename** (keywords like acne, rash, etc.)
- The **image size** (used to simulate detection confidence)

It then provides:
- Detected disease name  
- Suggested cure  
- Detection method  

---

## Features

-  Accepts image file input from the user. 
-  Detects disease using filename keywords. 
-  Uses random logic if no keyword is found. 
-  Gives the disease name on the basis of the information provided.
-  Suggests basic care tips.
-  Give some precautions as well.

---

## Technologies Used

- Python 3  
- libraries used :
  -os
  -random

---

## How It Works

1. User enters the image file path  
2. Program checks:
   - If file exists  
   - If it is a valid image format  
3. Extracts:
   - File name  
   - File size  
4. Detection happens in two steps:
   - **Step 1:** Keyword matching from filename  
   - **Step 2:** If no match then weighted random detection  
5. Displays:
   - Disease name  
   - Detection method  
   - Suggested cure  
