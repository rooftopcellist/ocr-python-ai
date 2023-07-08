import pytesseract
from PIL import Image

def extract_text(image):
    # Convert the image to PIL Image object
    image = Image.fromarray(image)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    return text
