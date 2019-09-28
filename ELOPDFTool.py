from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import glob
import csv
from shutil import copyfile


def rotate(in_file,  degrees, output_dir):
    """
    Rotates an input PDF <degrees> degrees clockwise and safes it to output_dir/<input>_rotated.pdf
    :param in_file: The file to rotate
    :param degrees: Amount of degrees to rotate
    :param output_dir: The output directory
    :return:
    """
    print("Rotating {}".format(in_file))

    # TODO: Ensure input exists

    # ensure the output directory exists
    if not os.path.exists(os.getcwd() + '/' + output_dir):
        os.makedirs(os.getcwd() + '/' + output_dir)

    pdf_in = open(os.getcwd() + '/' + in_file, 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    pdf_writer = PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(degrees)
        pdf_writer.addPage(page)
    pdf_out = open(os.getcwd() + '/' + output_dir + '/' + in_file[in_file.index('/')+1:-4] + '_rotated.pdf', 'wb')
    print("Saved {} as {}".format(in_file, os.getcwd() + '/' + output_dir + '/' + in_file[:-4] + '_rotated.pdf'))
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
    return


def rotate_batch(input_dir, degrees, output_dir):
    count = len(glob.glob1(input_dir, "*.pdf"))
    print("Found {} pdf files in directory {}".format(count, input_dir))
    for x in os.listdir(input_dir):
        if not x.endswith('.pdf'):
            continue
        rotate(input_dir + x,  degrees, output_dir)


def split(in_file, pages, output_dir):
    """
    :param in_file: The input file
    :param pages: The amount of pages per output document
    :param output_dir:
    :return:
    """
    print("Splitting {} in to {} page segments".format(in_file, pages))
    # TODO: Add a check if the file exists
    inputpdf = PdfFileReader(open(in_file, "rb"))

    # TODO: Add a check to see if the number of pages works out

    # ensure the output directory exists
    if not os.path.exists(os.getcwd() + '/' + output_dir):
        os.makedirs(os.getcwd() + '/' + output_dir)

    # Split the PDF
    for i in range(int(inputpdf.numPages / pages)):
        output = PdfFileWriter()
        for j in range(pages):
            output.addPage(inputpdf.getPage((i*pages)+j))
        file_string = os.getcwd() + '/' + output_dir + '/' + in_file[in_file.index('/') + 1:-4]
        file_string += '_split {} to {}.pdf'.format((i*pages)+1, (i*pages)+pages)
        with open(file_string, 'wb') as outStream:
            output.write(outStream)
    print("Saved split pages to files named similarly to {}".format(file_string))
    return


def split_batch(input_dir, pages, output_dir):
    """
    Performs the same function as split, but on a directory.
    :param input_dir: Input Directory with PDFs
    :param pages:
    :param output_dir:
    :return:
    """
    count = len(glob.glob1(input_dir, "*.pdf"))
    print("Found {} pdf files in directory {}".format(count, input_dir))

    for x in os.listdir(input_dir):
        if not x.endswith('.pdf'):
            continue
        split(input_dir + '/' + x,  pages, output_dir)
    return


def rename(in_file, new_name):
    """
    Renames a file
    :param input: Input file
    :param output: Name of output file
    :return:
    """
    # Save the filename
    copyfile(in_file, new_name)
    return


def rename_batch(input_dir, title, csv_file, output_dir):
    """
    :param input_dir: Directory of PDFs to rename
    :param title: The primary title for each file, e.g. "EEE3096S_Prac1
    :param csv_file: A list of student names in the csv format
    :param output_dir:
    :return:
    """
    if not os.path.exists(os.getcwd() + '/' + output_dir):
        os.makedirs(os.getcwd() + '/' + output_dir)

    count = len(glob.glob1(input_dir, "*.pdf"))
    print("Found {} pdf files in directory {}".format(count, input_dir))

    names = []

    # Load in the CSV
    file = open(csv_file, "r")
    reader = csv.reader(file)
    for line in reader:
        names.append(line[0])

    # print(names)

    if not count == len(names):
        print("Different number of rows and PDFs")
        return

    # Rename the files
    print(sorted(glob.glob('{}/*.pdf'.format(input_dir))))
    for index, in_pdf in enumerate(sorted(glob.glob('{}/*.pdf'.format(input_dir)))):
        if not in_pdf.endswith('.pdf'):
            continue
        print(in_pdf)
        print(output_dir + title + str(names[index]) + '.pdf')
        rename(in_pdf, output_dir + '/' + title + str(names[index]) + '.pdf')

    return



