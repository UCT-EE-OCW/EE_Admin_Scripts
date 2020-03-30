"""
Tutor Claim Forms
Auto populates claim forms based on  a provided CSV

Source PDF provided by Rachmat Harris, converted to PDF by Keegan Crankshaw


"""

from PyPDF2 import PdfFileReader
from fdfgen import forge_fdf
from subprocess import Popen, PIPE
import csv

pdf_fields = {'student_no': None, 'date_of_birth': None, 'email': None, 'first_names': None, 'surname': None,
          'cell_no': None, 'year': None, 'from': None, 'to': None,

          # A tasks
          'course_code_a': None, 'convenor_name_A': None, 'ta_name_A': None,

          'day_A': None, 'date_A': None, 'description_A': None, 'time_start_A': None, 'time_stop_A': None, 'duration_A': None,
          'day_A_1': None, 'date_A_1': None,  'description_A_1': None, 'time_start_A_1': None,  'time_stop_A_1': None, 'duration_A_1': None,
          # Repeat to 13

          'course_code_b': None, 'convenor_name_B': None, 'ta_name_B': None,
          'day_B': None, 'date_B': None, 'description_B': None, 'time_start_B': None, 'time_stop_B': None, 'duration_B': None,
          'day_B_1': None, 'date_B_1': None,  'description_B_1': None, 'time_start_B_1': None,  'time_stop_B_1': None, 'duration_B_1': None,
          #
          'sign_date': None,
          }


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


def load_csv(in_file):
    info = []
    csv_in = open(in_file)
    reader = csv.DictReader(csv_in)
    data = list(reader)
    for row in data:
        info.append(list(row.items()))
    csv_in.close()
    return info


def process(tutor_info, course, source_pdf):
    tutor_info = load_csv(tutor_info)
    hour_info = load_csv(course)

    # For each tutor in info
    for tutor in tutor_info:
        # iterate over all the courses and create the pdf dict
        print(hour_info)
        # save the pdf


if __name__ == "__main__":
    process("Tutors.csv", "EEE4120F.csv", "ClaimFormSource.pdf")
