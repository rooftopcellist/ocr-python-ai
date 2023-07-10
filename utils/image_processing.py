import os
import cv2
import numpy as np
import pydicom
from PIL import Image

def process_image(filepath):
    # Check the image extension
    _, ext = os.path.splitext(filepath)

    if ext.lower() == '.dcm':
        # Load the DICOM image
        dicom = pydicom.dcmread(filepath)
        image = dicom.pixel_array

        # Normalize to 0-255 and convert to uint8
        image = cv2.normalize(image, None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8U)

        # Check if the image is colored (PhotometricInterpretation == 'RGB')
        # Convert the image to grayscale if it's colored
        if dicom.PhotometricInterpretation == 'RGB':
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        # Load the image (for non-DICOM images)
        image = cv2.imread(filepath)

        # Convert the image to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Otsu's thresholding method to improve OCR accuracy
    thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    return thresholded
