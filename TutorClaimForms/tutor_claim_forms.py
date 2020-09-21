"""
Tutor Claim Forms
Auto populates claim forms based on  a provided CSV

Source PDF provided by Rachmat Harris, converted to PDF by Keegan Crankshaw

TODO:
    - Cater for multiple courses
    - Enable threading (perhaps on a per-tutor basis)

"""

from fdfgen import forge_fdf
from subprocess import Popen, PIPE
import csv
from helpers import populate_pdf
from datetime import datetime
import os


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
            try:
                if int(row[tutor["student_no"]]) > 0:
                    data = [row["Day"], row['Date'], row["Task"], row["Start"], row["End"], row[tutor["student_no"]]]
                    processed_data[tutor["student_no"]].append(data)
            except:
                # No claim for this tutor
                pass

    f.close()
    # At this point, we have a dict with {studnum: [Activities]}
    return processed_data


def print_pdf(tutor_info, raw_data, pdf_source, coursedata):
    if not os.path.exists('output'):
        os.makedirs('output')

    d = datetime.now()
    month = d.strftime("%b")
    year = d.strftime("%Y")

    # Create the summary csv and write the heading
    filename = "output/{} {} {} Tutor Spreadhseet - TA {}.csv".format(coursedata[0], month, year, coursedata[2])
    with open(filename, "w+") as file:
        file.write("SURNAME,NAME,STUDENT NUMBER,COURSE CODE,TOTAL HOURS CLAIMED-{} {},Teaching Assistant \n".format(month, year))

    # populate the csv
    for tutor in tutor_info:
        print("Creating form for {}".format(tutor["student_no"]))
        pdf_fields = populate_pdf(tutor, raw_data[tutor["student_no"]])
        pdf_fields["course_code_A"] = coursedata[0]
        pdf_fields["convenor_name_A"] = coursedata[1]
        pdf_fields["ta_name_A"] = coursedata[2]
        fdf = forge_fdf("", pdf_fields, [], [], [])
        fn = "{} {} {} {} {} {}.pdf".format(pdf_fields["surname"], pdf_fields["first_names"][0],
                                            pdf_fields["convenor_name_A"], pdf_fields["course_code_A"],
                                            month, year)
        pdftk = ["pdftk", pdf_source, "fill_form", "-", "output", "output/{}".format(fn), "flatten"]
        proc = Popen(pdftk, stdin=PIPE)
        output = proc.communicate(input=fdf)
        if output[1]:
            raise IOError(output[1])

        # add their details to the summary csv
        surname = pdf_fields["surname"]
        name = pdf_fields["first_names"]
        studnum = tutor["student_no"]
        course_code = pdf_fields["course_code_A"]
        total_hours = pdf_fields["total_A"]
        ta = pdf_fields["ta_name_A"]
        with open(filename, "a+") as file:
            file.write("{}, {}, {}, {}, {}, {}\n".format(surname, name, studnum, course_code, total_hours, ta))


def main(coursefiles):
    print("=== Creating claim forms ===")
    tutor_info = load_csv_dict("Tutors.csv")
    for file in coursefiles:
        raw_data = reduce_claim_csv(tutor_info, file)
        coursedata = file[:-4].split('_')
        print_pdf(tutor_info, raw_data, "ClaimFormSource.pdf", coursedata)
    print("=== Completed claim forms ===")


if __name__ == "__main__":
    coursefiles = ["EEE1111W_CName CSurname_TAName TASurname.csv"]
    main(coursefiles)
