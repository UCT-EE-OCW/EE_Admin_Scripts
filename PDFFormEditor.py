from PyPDF2 import PdfFileWriter, PdfFileReader
from fdfgen import forge_fdf
from subprocess import Popen, PIPE
import csv


def get_fields(file_in):
    """
    Gets all the editable fields in a PDF and writes it to a .csv
    :param file_in:
    :return:
    """
    file = open(file_in, "rb")
    pdf_reader = PdfFileReader(file)
    dictionary = pdf_reader.getFormTextFields()
    print(dictionary)
    file.close()
    return


def populate_form(pdf_in, csv_in):
    # load in the CSV
    reader = csv.DictReader(open(csv_in))

    students = []
    for row in reader:
        students.append(row)

    # Create the PDFs
    for student in students:
        fields = list(student.items())
        print(fields)
        fdf = forge_fdf("", fields, [], [], [])
        pdftk = ["pdftk", pdf_in, "fill_form", "-",
                 "output", student["student-name"] +"out.pdf", "flatten"]
        proc = Popen(pdftk, stdin=PIPE)
        output = proc.communicate(input=fdf)
        if output[1]:
            raise IOError(output[1])




