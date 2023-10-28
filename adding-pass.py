# Python script to add password protection to a PDF
import PyPDF2
def add_password_protection(input_path, output_path, password):
    with open(input_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)
            pdf_writer.encrypt(password)
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)









