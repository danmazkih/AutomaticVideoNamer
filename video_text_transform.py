import os
import time
import psutil

def is_file_in_use(file_path):
    for proc in psutil.process_iter():
        try:
            for item in proc.open_files():
                if item.path == file_path:
                    return "File is in use by another process"
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
    return "File is not in use"

def clean_text(text):

    new_str = ''.join(char for char in text if char.isalpha() or char == ';'  or char == '/' or char == ':')
    new_str = new_str.replace('\n', ' ')
    return new_str


def rename_video_file(pathWithFile, currentFrame, Strpath, new_str):
    old_name = pathWithFile
    new_name = Strpath + "\\" +str(currentFrame) + ".-" +  new_str + ".mp4"
    #is_file_in_use(pathWithFile) //Check if the file is in use by another process
    try:
        print(pathWithFile)
        os.rename(old_name, new_name)
        
    except:
        print("An error has occurred but it's okay, |-__-|")
        os.rename(pathWithFile, Strpath + "\\" +str(currentFrame) + ".-" +  "Error" + ".mp4")
        pass


def save_text_to_file(currentFrame, new_str):
    text_file = open(r'Location of TXT to save the different video names', 'a') #file to save the text, just to check if the text is correct
    text_file.write(str(currentFrame) +"- " + new_str +"\n")
    text_file.close()


def main_rename_video_with_text(currentFrame, Strpath, pathWithFile, frase):
    new_str = clean_text(frase)
    rename_video_file(pathWithFile, currentFrame, Strpath, new_str)
    save_text_to_file(currentFrame, new_str)
