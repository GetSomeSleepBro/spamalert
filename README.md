# 📷 (SMS / Email) Spam Detector 🤖
![image](https://github.com/user-attachments/assets/18d79358-971c-460d-a3e7-cb6c30ca77dd)
> A simple app that detects spam in images by extracting text with OCR and classifying it using a pre-trained machine learning model.

<br>

# 📦 About This Project

This project, **SpamAlert**, is a lightweight tool that detects spam content in text extracted from images. It's powered by OCR (Optical Character Recognition) and a machine learning model trained on real-world email and SMS data.  
You can test messages captured from physical media (like flyers or spammy screenshots), and the app will extract the text and classify it as **Spam** or **Not Spam**.

<br>

## 📄 Overview

- Upload an image with text (e.g. flyers, ads, screenshots).
- The app extracts text using OCR (`Optical Character Recognition`).
- It predicts if the content is **Spam** or **Not Spam** using a trained model.

| Spam | Ham |
|-|-|
| ![image](https://github.com/user-attachments/assets/742b14b8-0b55-497d-9098-05c1722a1cee) | ![image](https://github.com/user-attachments/assets/fc511add-2b18-4e6c-9c60-f2cbd62475da) |

<br>

## 📂 How to Use

1. Clone the repository `git clone https://github.com/GetSomeSleepBro/spamalert` and navigate into the project folder `cd spamalert`
2. Install dependencies using `pip install -r requirements.txt`  
3. Run the app with `python3 app.py`  
4. Open your browser and go to `http://localhost:7860`  
5. Upload an image to get a prediction and view the extracted text  

<br>

## 🖼️ Demo Images

To quickly try out the app, you can use these sample images from the repo:

- ✅ **Ham (Not Spam):** [ham.png](./spam_ham/ham.png)  
- 🚫 **Spam:** [spam.png](./spam_ham/spam.png)

Download them and upload through the interface to see the predictions in action.

<br>

## 🧠 Model Training
The model was trained using a labeled dataset of email and SMS messages. You can find the dataset used for training here:  

📊 [spam_ham_dataset.csv](./spam_ham/spam_ham_dataset.csv)  

It contains a mix of spam and legitimate (ham) messages, which were vectorized using TF-IDF and used to train a classification model (stored as `model.pkl`).  

<br>

## 📑 Presentation

A detailed breakdown of the model architecture, data processing pipeline, and performance metrics can be found in the attached PDF:  

🔗 [Email and SMS Spam Detection – Full Report (PDF)](./Email-and-SMS-Spam-Detection.pdf)  

<br>

## 🔧 Components

- **EasyOCR** for extracting text from uploaded images
- **TF-IDF Vectorizer** to preprocess textual data
- **Scikit-learn** model trained on real-world messages
- **Gradio** for a user-friendly browser interface

## 🧪 Try It Out

Launch the app locally and upload an image. It’ll display the extracted text and tell you if the message is spam — right in your browser.

