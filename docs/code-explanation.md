# AI Image to Text Extractor: Code Explanation

This project uses Optical Character Recognition (OCR) to extract text from images using Python. It mainly relies on the `pytesseract` library which is a Python wrapper for Google's Tesseract-OCR Engine.

## Code Structure

The project consists of 3 main Python scripts: `main.py`, `image_processing.py` and `ocr_engine.py` and they are contained in a package named `utils`.

### main.py

This is the entry point of the application. It contains the `main` function which is called when you run the script. This script uses Python's built-in `argparse` module to parse command-line arguments. The path to the image is taken as a command-line argument.

In the `main` function, first, it creates an `argparse.ArgumentParser` object and defines what command-line options the program is expecting. In this case, it expects an image file path.

```python
parser = argparse.ArgumentParser(description="Extract text from an image")
parser.add_argument("filepath", help="Path to the image file")
```

The `parse_args` function will return some output that looks like `Namespace(filepath='path_to_your_image')`. The 'filepath' property is then passed to the `process_image` and `extract_text` functions, which are imported from `image_processing.py` and `ocr_engine.py` respectively.


### image_processing.py

The `process_image` function uses the `cv2` library to process the image to improve the accuracy of the OCR operation.

The image is first loaded with `cv2.imread(filepath)`, then converted to grayscale using `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`. This is done because OCR works better on grayscale images than colored ones.

Next, the OTSU thresholding method is applied to the grayscale image. This is a way to automatically determine the threshold value of a bimodal image (an image whose histogram has two peaks). The returned thresholded image is better suited for the OCR process.

### ocr_engine.py

The `extract_text` function is where the actual OCR process happens. The function takes a processed image and uses pytesseract to recognize and extract text from it.

The input image is first converted to a PIL Image object because pytesseract works with this object type. Then the `pytesseract.image_to_string(image)` function is called to extract the text from the image.


## Usage
To run the program, navigate to the project directory in your terminal and type the following command:

```bash
python main.py path_to_your_image
```

Please replace "path_to_your_image" with the actual path to your image. The program will print the extracted text from the image.

