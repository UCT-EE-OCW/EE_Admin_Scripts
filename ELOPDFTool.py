"""
Developed by Keegan Crankshaw to simplify ELO document renaming

Special thanks to these Stackoverflow posts/users:

rotate: https://stackoverflow.com/questions/46921452/python-batch-rotate-pdf-with-pypdf2
split: https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import os



def rotate(input,  degrees, output_dir):
    """
    Rotates an input PDF <degrees> degrees clockwise and safes it to output_dir/<input>_rotated.pdf
    :param input: The file to rotate
    :param degrees: Amount of degrees to rotate
    :param output_dir: The output directory
    :return:
    """

    # TODO: Ensure input exists

    # ensure the output directory exists
    if not os.path.exists(os.getcwd() + '/' + output_dir):
        os.makedirs(os.getcwd() + '/' + output_dir)

    pdf_in = open(os.getcwd() + '/' + input, 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    pdf_writer = PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(degrees)
        pdf_writer.addPage(page)
    pdf_out = open(os.getcwd() + '/' + output_dir + '/' + input[:-4] + '_rotated.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
    return


def split(input_document, pages, output_dir):
    """

    :param input_document: The input file
    :param pages: The amount of pages per output document
    :param output_dir:
    :return:
    """
    # TODO: Add a check if the file exists
    inputpdf = PdfFileReader(open(input_document, "rb"))

    # TODO: Add a check to see if the number of pages works out

    # ensure the output directory exists
    if not os.path.exists(os.getcwd() + '/' + output_dir):
        os.makedirs(os.getcwd() + '/' + output_dir)

    # Split the PDF
    for i in range(int(inputpdf.numPages / pages)):
        output = PdfFileWriter()
        for j in range(pages):
            output.addPage(inputpdf.getPage((i*pages)+j))
        with open(os.getcwd() + "/{}/document-page{}-{}.pdf".format(output_dir, (i*pages)+1, (i*pages)+pages), "wb") as outputStream:
            output.write(outputStream)
    return


def batch_split(input_dir, title, list, output_dir):
    return


def rename(input, output):
    """
    Renames a file
    :param input: Input file
    :param output: Name of output file
    :return:
    """
    return


def batch_rename(input_dir, title, list, output_dir):
    """

    :param input_dir: Directory of PDFs to rename
    ;param title: The primary title for each file, e.g. "EEE3096S_Prac1
    :param list: A list of student names in the format
    :param output_dir:
    :return:
    """
    return



