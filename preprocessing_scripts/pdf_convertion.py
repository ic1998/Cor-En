#turns pdf cornish dict to useable version

#import libraries
import pdfplumber
import re


#lst of word type abbrevs
abbrevs = ["abbr", "adj", "adv", "art", "cnj", "contr", "int", "n", "n.coll", "n.dl", "n.f", "n.m", "n.m", "n.f", "n.pl", "num", "part",
"prfx", "prn", "prp", "sffx", "top", "vb"]

#opens pdf and reads it
with pdfplumber.open("./cornish_dict.pdf") as pdf:
    text = pdf.pages[20]
    clean_text = text.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])
    #print(clean_text.extract_text())
    for line in clean_text.extract_text():
        print(line)
