#import libraries
import re

def open_file(file_path):
    file_lst = []
    #opens file
    file = open(file_path, 'r')
    #strips of whitespace
    for line in file.readlines():
        line = line.strip()
        file_lst.append(line)
    return file_lst

#any cleaning



#change to TMX format





if __name__ == "__main__":
    cornish_file = open_file('/Users/ionacarslaw/Desktop/Cor-En/raw_datasets/1_COR.txt')
    print(cornish_file)
    print("FINISH")
