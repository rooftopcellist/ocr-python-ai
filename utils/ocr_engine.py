import pytesseract
from PIL import Image

def extract_text(image, output_file):
    # Convert the image to PIL Image object
    image = Image.fromarray(image)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # Write the text to a file
    with open(output_file, 'w') as file:
        file.write(text)

    # Optionally write the text to the console
    print('-----------------------------------------')
    print(text)
    print('-----------------------------------------')
