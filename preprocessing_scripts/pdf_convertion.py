#turns pdf cornish dict to useable version

#import libraries
from PyPDF2 import PdfReader

#opens pdf file and reads
reader = PdfReader("./cornish_dict.pdf")
number_of_pages = len(reader.pages)


#read each page and appends to lst
lst_of_page = []
for i in range(number_of_pages):
    if i == 20:
        lst = []
        page = reader.pages[i]
        text = page.extract_text()
        lst.append(text)
        lst_of_page.append(lst)
        print(lst)
    else:
        pass

print(lst_of_page)
