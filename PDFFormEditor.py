from PyPDF2 import PdfFileReader
import pandas
import csv


def get_fields(file_in):
    """
    Gets all the editable fields in a PDF and writes it to a .csv
    :param file_in:
    :return:
    """
    pdf_reader = PdfFileReader(open(file_in, "rb"))
    dictionary = pdf_reader.getFormTextFields()
    print(dictionary)
    for i in dictionary:
        print(i)
    return


def populate_form(pdf_in, csv_in):
    reader = csv.DictReader(open(csv_in))
    for row in reader:
        print(row)

