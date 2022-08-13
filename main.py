import ocrmypdf
import datetime
from PyPDF2 import PdfReader


def main():
  try:
    output_file_name = f'{datetime.datetime.now()}'
    ocrmypdf.ocr('sample.pdf', f'output/{output_file_name}.pdf', deskew=True)
    reader = PdfReader(f'output/{output_file_name}.pdf')
    page = reader.pages[0]
    text = page.extract_text()

    with open(f'output/{output_file_name}.txt', 'w') as f:
      f.write(text)
  
  except Exception as e:
    print(f'Something went wrong: {e}')

if __name__ == "__main__":
    main()

