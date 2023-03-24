import cv2
import os 
import frame_editor as takeScreenshot

# assign directory
directory = r"Video location path" 

#This code is designed to find MP4 files within a directory structure that has a depth of 4 folders. 
#It has limitations and may not work if the directory structure is different.
#To use the code, ensure that your MP4 files are located in a directory structure with a depth of 4 folders, with the files located in the last folder. 
# Alternatively, modify the code to search for MP4 files in a different directory structure.
#Although the code may not be optimal, it functions correctly within its intended parameters.

currentFrame = 0
def process_files(directory, current_frame):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            # Recurse into subdirectory
            process_files(filepath, current_frame)
        elif os.path.isfile(filepath) and filepath.endswith('.mp4'):
            print("File: " + filepath)
            print("Current frame: " + str(current_frame))
            current_frame += 1
            takeScreenshot.take_screenshot_func(filepath, current_frame, directory)

# Call the function with the initial directory and current frame count
process_files(directory, currentFrame)
                
