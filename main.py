import argparse
from utils.image_processing import process_image
from utils.ocr_engine import extract_text
import os
from PIL import Image

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Extract text from an image")

    # Add arguments
    parser.add_argument("filepaths", nargs='+', help="Path to the image file")
    parser.add_argument("--to-file", action='store_true', help="Write output to file")

    # Parse arguments
    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    if args.to_file and not os.path.exists("output"):
        os.mkdir("output")

    # Loop over each file path
    for filepath in args.filepaths:

        # Validate the file path
        if not os.path.isfile(filepath):
            print(f"The file {filepath} does not exist.")
            continue

        # Check if the file is an image
        def get_image_type(filepath):
            try:
                image = Image.open(filepath)
                return image.format.lower()
            except Exception as e:
                print(f"Error: {e}")
                return None
        image_type = get_image_type(filepath)
        if image_type:
            print(f"The image type is: {image_type}")

        # # Print error if image format is not valid
        # if not image_type:
        #     print(f"The file {filepath} is not a valid image.")
        #     continue

        # Process the image
        processed_image = process_image(filepath)

        # Create an output file path if --to-file is set
        output_file = None
        if args.to_file:
            base_name = os.path.basename(filepath)
            file_name, _ = os.path.splitext(base_name)
            output_file = os.path.join("output", f"{file_name}.txt")

        # Use pytesseract to extract text and write it to a file or print it
        extract_text(processed_image, output_file)

        if output_file:
            print(f"Extracted text written to {output_file}")

if __name__ == "__main__":
    main()
