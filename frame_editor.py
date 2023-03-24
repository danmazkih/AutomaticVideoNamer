import cv2
import os
import color_image_processing

def process_image_rectangles(image, currentFrame, pathTofile, Strpath):
    dimensions = image.shape
    cv2.rectangle(image, (dimensions[1]-375, 0), (dimensions[1],dimensions[0]-200), (0, 0, 0), -1)
    cv2.rectangle(image, (dimensions[1]-200, dimensions[0]-200), (dimensions[1],dimensions[0]), (0, 0, 0), -1)
    cv2.rectangle(image, (0, dimensions[0]-135), (dimensions[1],dimensions[0]), (0, 0, 0), -1)

    stringPath = "./frame/frame" + str(currentFrame) +".jpg"
    cv2.imwrite(stringPath,  image)

    return stringPath

def analyze_image(stringPath, currentFrame, pathTofile, Strpath):
    color_image_processing.process_image_colors(stringPath,currentFrame,pathTofile,Strpath)

def take_screenshot_func(Strpath,currentFrame,pathTofile):
    vid = cv2.VideoCapture(Strpath)
    localFrame = 0
    if not os.path.exists('frame'):
        os.makedirs('frame')

    while(localFrame < 1):
        success, image = vid.read()
        print("Success: " + str(success))
        if success:
            stringPath = process_image_rectangles(image, currentFrame, pathTofile, Strpath)
            vid.release()
            analyze_image(stringPath, currentFrame, pathTofile, Strpath)
            
        localFrame += 1
