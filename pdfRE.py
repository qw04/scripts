import sys
import re
from pypdf import PdfReader
import os

def getAllTextPDF(filePath): # just gonna ocr initially then transition it to pyPDF2 for some text
  text = ""
  reader = PdfReader(stream = filePath)
  for page in reader.pages:
    text += " " + page.extract_text()

  return text

def specificRE(text, pattern):
    prog = re.compile(f"\w.*{pattern}")
    result = prog.search(text)
    if result:
        return result.group()
    else:
        return "No match"


def main(src, func, *args):
  with open("fileToWrite.txt", "w") as f:
    for pattern in args:
      f.write(f"Pattern: {pattern}\n")
      for file in os.listdir(src):
        text = getAllTextPDF(os.path.join(src, file))    
        newPara = ""
        for line in text.split("\n") + [""]:
          l = line.strip()
          if l:
            newPara += l
          elif newPara:
            if func(newPara, pattern) != "No match":
              f.write(f"{file}: {func(newPara, pattern)}\n")
            newPara = ""
      f.write("\n")
    f.close()
          


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python pdfRE.py <path to folder> <pattern1> <pattern2> ...")
  else:
    # Usage main(<path to folder>, specificRE, <pattern1>, <pattern2>, ...)
    main(sys.argv[1], specificRE, "K23", "S23")