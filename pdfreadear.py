import PyPDF2

# abrir el archivo pdf
with open('Microprocesadores intel - Barry B. Brey.pdf', 'rb') as file:
    # crear un objeto pdf reader
    pdf_reader = PyPDF2.PdfFileReader(file)

    # obtener el número de páginas
    num_pages = pdf_reader.numPages

    # iterar sobre las páginas
    for page_num in range(52,57):
        # obtener la página
        page = pdf_reader.getPage(page_num)

        # extraer el texto de la página
        text = page.extractText()

        # imprimir el texto
        print(text)