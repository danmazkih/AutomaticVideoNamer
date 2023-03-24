import numpy
import cv2
import pytesseract
from pytesseract import Output
import video_text_transform


pytesseract.pytesseract.tesseract_cmd = r"tesseract path"


def preprocess_image(stringPath):
    image = cv2.imread(stringPath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh, im_bw = cv2.threshold(image, 245, 250, cv2.THRESH_BINARY)
    inverted_image = cv2.bitwise_not(im_bw)
    image2 = inverted_image.copy()

    kernel = numpy.ones((2, 2), numpy.uint8)
    image2 = cv2.dilate(image2, kernel, iterations=2)
    kernel = numpy.ones((3, 3), numpy.uint8)
    image2 = cv2.erode(image2, kernel, iterations=3)
    image2 = cv2.morphologyEx(image2, cv2.MORPH_CLOSE, kernel)
    image2 = cv2.medianBlur(image2, 3)

    return image2


def extract_text_and_annotate_image(image, stringPath, currentFrame, pathTofile, pathWithFile):
    image_data = pytesseract.image_to_data(image, output_type=Output.DICT)
    frase = ""
    for i, word in enumerate(image_data['text']):
        if word != "":
            x, y, w, h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, word, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            frase += word + " "

    cv2.imwrite(stringPath, image)
    video_text_transform.main_rename_video_with_text(currentFrame, pathTofile, pathWithFile, frase)


def process_image_colors(stringPath, currentFrame, pathTofile, pathWithFile):
    image = preprocess_image(stringPath)
    extract_text_and_annotate_image(image, stringPath, currentFrame, pathTofile, pathWithFile)
    
    cv2.destroyAllWindows()
