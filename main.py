from PyPDF2 import PdfReader
import fitz
import ocrmypdf

def main():
  try:

    ocrmypdf.ocr('sample.pdf', 'output.pdf', deskew=True)
    reader = PdfReader("output.pdf")
    page = reader.pages[0]
    text = page.extract_text()

    with open('output.txt', 'w') as f:
      f.write(text)
  
  except Exception as e:
    print(f'Something went wrong: {e}')

if __name__ == "__main__":
    main()

