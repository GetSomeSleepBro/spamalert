import gradio as gr
import pickle
from PIL import Image
import easyocr
import numpy as np  # Import numpy

# Load pre-trained model, TF-IDF vectorizer, and other necessary files
with open("models/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("models/tfidf.pkl", "rb") as tfidf_file:
    tfidf_vectorizer = pickle.load(tfidf_file)

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])  # You can add other languages if needed

# Function to extract text from an image using OCR
def extract_text_from_image(image):
    try:
        # Convert PIL Image to numpy array
        image_np = np.array(image)
        
        # Now use easyocr to read the text from the image
        result = reader.readtext(image_np)
        
        # Extract and concatenate the text from the result
        extracted_text = ' '.join([text[1] for text in result])
        print("Extracted Text from Image: ", extracted_text)  # Debugging print
        return extracted_text
    except Exception as e:
        return f"Error extracting text from image: {str(e)}"

# Function to predict if text input is spam
def is_spam(input_data):
    try:
        # Initialize extracted_text as an empty string
        extracted_text = ""
        
        # Check if input is an image
        if isinstance(input_data, Image.Image):
            # Extract text from the image using OCR
            extracted_text = extract_text_from_image(input_data)
            if not extracted_text:
                return "No text found in the image.", "No text extracted"
            input_data = extracted_text  # Use the extracted text for prediction

        # If the input is a string (text), process it normally
        if isinstance(input_data, str):
            print("Received input text: ", input_data)  # Debugging print
            # Transform the text input using the TF-IDF vectorizer
            text_vectorized = tfidf_vectorizer.transform([input_data])
            # Predict using the pre-trained model
            prediction = model.predict(text_vectorized)[0]
            
            # Return whether it's spam or not along with extracted text
            return "Spam" if prediction == 1 else "Not Spam", extracted_text
        
        else:
            return "Invalid input. Please provide either text or an image.", ""

    except Exception as e:
        return f"Error: {str(e)}", ""


# Create Gradio interface with both text input and image upload
iface = gr.Interface(
    fn=is_spam,
    inputs=gr.Image(label="Upload image", type="pil"),  # Updated to `gr.Image`
    outputs=[gr.Textbox(label="Prediction"), gr.Textbox(label="Extracted Text")],  # Updated to `gr.Textbox`
    live=True,
)

# Launch the interface on your local machine
iface.launch(share=False)  # Use share=False for local deployment
