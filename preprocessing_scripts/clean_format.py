#import libraries
import time

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
    #gets current time
    current_time = time.ctime(time.time())
    times_five_tab = "\t" * 5
    tmx_file = open(f"{file_name}.tmx", "a+")
    #add header elements to tmx file
    tmx_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>" + "\n" + "<tmx version=\"1.4\">" + "\n")
    tmx_file.write("<header creationdate=" + str(current_time) + "\n" + times_five_tab + "srclang=\"en\"" + "\n" + times_five_tab + "adminlang=\"en\"" + "\n" + times_five_tab + "o-tmf=\"unknown\"" + "\n" + times_five_tab + "segtype=\"sentence\"" + "\n" + times_five_tab + "creationtool=\"Uplug\"" + "\n" + times_five_tab + "creationtoolversion=\"unknown\"" + "\n" + times_five_tab + "datatype=\"PlainText\" />" + "\n")
    tmx_file.write("  <body>" + "\n")
    #iterates through cornish and english lists and write to file with tmx format
    for i in range(len(cor_lst)):
        tmx_file.write("    <tu>" + "\n" + f"      <tuv xml:lang=\"en\"><seg>{en_lst[i]} </seg></tuv>" + "\n" + f"      <tuv xml:lang=\"kw\"><seg>{cor_lst[i]} </seg></tuv>" + "\n" + "    </tu>" + "\n")
    tmx_file.write("  </body>" +  "\n" + "</tmx>")
    tmx_file.close()



if __name__ == "__main__":
    #opens cornish and english raw_dataset file
    cornish_file = open_file('/Users/ionacarslaw/Desktop/Cor-En/raw_datasets/1_COR.txt')
    english_file = open_file('/Users/ionacarslaw/Desktop/Cor-En/raw_datasets/1_ENG.txt')
    turn_into_tmx(english_file, cornish_file, "test")
    print("FINISH")
