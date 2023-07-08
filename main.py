import argparse
from utils.image_processing import process_image
from utils.ocr_engine import extract_text

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Extract text from an image")

    # Add arguments
    parser.add_argument("filepath", help="Path to the image file")

    # Parse arguments
    args = parser.parse_args()

    # Process the image
    processed_image = process_image(args.filepath)
    
    # Use pytesseract to extract text
    text = extract_text(processed_image)

    print("Extracted Text: \n", text)

if __name__ == "__main__":
    main()
