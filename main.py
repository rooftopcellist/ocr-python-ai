import argparse
from utils.image_processing import process_image
from utils.ocr_engine import extract_text
import os
import imghdr

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Extract text from an image")

    # Add arguments
    parser.add_argument("filepaths", nargs='+', help="Path to the image file")

    # Parse arguments
    args = parser.parse_args()

    # Loop over each file path
    for filepath in args.filepaths:

        # Validate the file path
        if not os.path.isfile(filepath):
            print(f"The file {filepath} does not exist.")
            continue

        # Check if the file is an image
        image_type = imghdr.what(filepath)
        if not image_type:
            print(f"The file {filepath} is not a valid image.")
            continue

        # Process the image
        processed_image = process_image(filepath)

        # Create an output file path
        base_name = os.path.basename(filepath)
        file_name, _ = os.path.splitext(base_name)
        output_file = f"{file_name}.txt"

        # Use pytesseract to extract text and write it to a file
        extract_text(processed_image, output_file)

        print(f"Extracted text written to {output_file}")

if __name__ == "__main__":
    main()
