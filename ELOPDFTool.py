from PyPDF2 import PdfFileWriter, PdfFileReader
import os

# Define your options here


def rotate(input, direction, degrees, output):
    """

    :param input: The file to rotate
    :param direction: Clockwise or anticlockwise
    :param degrees: Amount of degrees to rotate
    :param output: File to save to
    :return:
    """
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
            print((i*pages)+j)
            output.addPage(inputpdf.getPage((i*pages)+j))
        with open(os.getcwd() + "/{}/document-page{}-{}.pdf".format(output_dir, (i*pages)+1, (i*pages)+pages), "wb") as outputStream:
            output.write(outputStream)
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



