"""
Tutor Claim Forms
Auto populates claim forms based on  a provided CSV

Source PDF provided by Rachmat Harris, converted to PDF by Keegan Crankshaw


"""

from PyPDF2 import PdfFileReader
from fdfgen import forge_fdf
from subprocess import Popen, PIPE
import csv
from helpers import populate_pdf


def get_fields(file_in):
    """
    Gets all the editable fields in a PDF and writes it to a .csv
    :param file_in:
    :return:
    """
    file = open(file_in, "rb")
    pdf_reader = PdfFileReader(file, strict=False)
    dictionary = pdf_reader.getFormTextFields()
    print(dictionary)
    file.close()
    return


def load_csv_dict(in_file):
    csv_in = open(in_file)
    info = list(csv.DictReader(csv_in))
    csv_in.close()
    return info


def reduce_claim_csv(tutor_info, course_csv):
    """ Monolithic function due to not being able to have a dictreader without file open"""
    processed_data = {}

    for t in tutor_info:
        processed_data[t["student_no"]] = []

    f = open(course_csv)
    reader = csv.DictReader(f)

    for row in reader:
        for tutor in tutor_info:
            if row[tutor["student_no"]] != "0":
                data = [row["Day"], row['Date'], row["Task"], row["Start"], row["End"], row[tutor["student_no"]]]
                processed_data[tutor["student_no"]].append(data)
    f.close()
    # At this point, we have a dict with {studnum: [Activities]}
    return processed_data


def print_pdf(tutor_info, raw_data, pdf_source):
    for tutor in tutor_info:
        pdf_fields = populate_pdf(tutor, raw_data[tutor["student_no"]])
        fdf = forge_fdf("", pdf_fields, [], [], [])
        fn = "{} {} {} {} {} {}.pdf".format(pdf_fields["surname"], pdf_fields["first_names"][0], pdf_fields["convenor_name_A"], pdf_fields["course_code_A"], "month", "year")
        pdftk = ["pdftk", pdf_source, "fill_form", "-", "output", fn, "flatten"]
        proc = Popen(pdftk, stdin=PIPE)
        output = proc.communicate(input=fdf)
        if output[1]:
           raise IOError(output[1])


def main():
    # get_fields("ClaimFormSource.pdf")
    tutor_info = load_csv_dict("Tutors.csv")
    raw_data = reduce_claim_csv(tutor_info, "EEE4120F.csv")
    print_pdf(tutor_info, raw_data, "ClaimFormSource.pdf")

    # print(raw_data)


if __name__ == "__main__":
    main()
