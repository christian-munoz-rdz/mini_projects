import PyPDF2

def readPdf():
    # abrir el archivo pdf
    with open('archivo2.pdf', 'rb') as file:
        # crear un objeto pdf reader
        pdf_reader = PyPDF2.PdfFileReader(file)

        # obtener el número de páginas
        num_pages = pdf_reader.numPages

        # iterar sobre las páginas
        for page_num in range(num_pages):
            # obtener la página
            page = pdf_reader.getPage(page_num)

            # extraer el texto de la página
            text = page.extractText()

            # imprimir el texto
            print(text)



def main():
    readPdf()

if __name__ == '__main__':
    main()


