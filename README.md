# AI Image to Text Extractor

This project uses Optical Character Recognition (OCR) to extract text from images.

## Setup

1. Install Tesseract on your machine. For instructions, see: https://github.com/tesseract-ocr/tessdoc#installation

For Fedora, I needed to follow this guide: https://blog.mdda.net/oss/2016/08/10/tesseract-and-python-on-fedora and run the following:

```bash
sudo dnf install tesseract-devel
pip install tesserocr
```

2. Create a virtual environment (optional, but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the script, simply execute the following from a terminal:

```bash
python main.py
```




The script expects a file named input.png in the same directory. You can replace it with your image file. Please replace 'input.png' with the path to your image in `main.py`.

The extracted text will be printed on the console.

This tool accepts multiple image formats since OpenCV's cv2.imread() function supports a variety of image formats including .bmp, .jpg, .jpeg, .png, .tif, .tiff, etc.

> Remember, Tesseract does a good job when the image is of high quality and the text is horizontal. For complex cases involving rotations, skewness, different languages or noisy backgrounds, you might have to use additional image processing techniques or different OCR tools.


## Additional Info

For more information on how to use this tool and how it works, see the following documentation:

* [Code Explanation](code-explanation.md)
