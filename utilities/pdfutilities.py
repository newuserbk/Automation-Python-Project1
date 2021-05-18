import PyPDF2

class PDFUtilities:

    @staticmethod
    def read_pdf_content_of_page(pdf_location_path,page_index=0):
        # Open File in read binary mode
        file = open(pdf_location_path, "rb")

        # pass the file object to PdfFileReader
        reader = PyPDF2.PdfFileReader(file)

        # getPage will accept index
        page = reader.getPage(page_index)

        # extractText will return the text
        pdf_data = page.extractText()

        return pdf_data

    @staticmethod
    def get_count_of_pdf_pages(pdf_location_path):
        # Open File in read binary mode
        file = open(pdf_location_path, "rb")

        # pass the file object to PdfFileReader
        reader = PyPDF2.PdfFileReader(file)

        # numPage will return number of pages in pdf
        no_of_pages=reader.numPages
        print(reader.numPages)

        return no_of_pages


