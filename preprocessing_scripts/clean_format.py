#import libraries
import re
from datetime import date
from time import ctime

def open_file(file_path):
    file_lst = []
    #opens file
    file = open(file_path, 'r')
    #strips of whitespace & adds to list
    for line in file.readlines():
        line = line.strip()
        file_lst.append(line)
    return file_lst

#any cleaning

#change to TMX format
def turn_into_tmx(en_lst, cor_lst, file_name):
    current_time = date(2022, 9, 7).ctime()
    print(current_time)
    tmx_file = open(f"{file_name}.tmx", "a+")
    #add header elements to tmx file
    tmx_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>" + "\n" + "<tmx version=\"1.4\">" + "\n")
    tmx_file.write("<header creationdate=")
    tmx_file.close()




if __name__ == "__main__":
    #opens cornish and english raw_dataset file
    cornish_file = open_file('/Users/ionacarslaw/Desktop/Cor-En/raw_datasets/1_COR.txt')
    english_file = open_file('/Users/ionacarslaw/Desktop/Cor-En/raw_datasets/1_ENG.txt')
    turn_into_tmx(cornish_file, english_file, "test")
    print("FINISH")
