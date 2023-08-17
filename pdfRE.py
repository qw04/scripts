import sys
import re
from PyPDF2 import PdfReader

def getAllTextPDF(filePath): # just gonna ocr initially then transition it to pyPDF2 for some text
  text = ""
  reader = PdfReader(stream = filePath)
  for page in reader.pages:
    text += " " + page.extract_text()

  return text

def specificRE(text):
    prog = re.compile("\w.*ks[234]")
    result = prog.search(text)
    if result:
        print(result.group())
    else:
        print("No match")


def main(src, func):
    text = getAllTextPDF(src)

    newPara = ""
    for line in text.split("\n") + [""]:
        l = line.strip()
        if l:
            newPara += l
        elif newPara:
           func(" " + newPara)
           newPara = ""
        


if __name__ == "__main__":
  main(sys.argv[1], specificRE)