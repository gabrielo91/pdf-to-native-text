import ocrmypdf
import os

from PyPDF2 import PdfReader

ocrmypdf.configure_logging(verbosity= 2)


def executeOCR(inputFilePath, outputFilePath):
    ocrmypdf.ocr(inputFilePath,  f'{outputFilePath}.pdf', output="pdf", sidecar=f'{outputFilePath}.txt', redo_ocr=True)


def main():
  try:
    executeOCR('sample.pdf', 'temp/prefile')
    executeOCR('temp/preFile.pdf', 'output')
    os.remove("temp/prefile.pdf")
    os.remove("temp/prefile.txt")
  
  except Exception as e:
    print(f'Something went wrong: {e}')

if __name__ == "__main__":
    main()

