"""
Provide:
- a directory, containing subdirectories all holding a submission,
- a csv of names and student numbers.
The program will check all submissions and rename them
The student will be marked if they have a submission
"""

import csv  # handles CSV operations
import os   # handles directory access and renaming
import re   # regex for finding student numbers


def process_submissions(root_dir):
    entries = os.listdir(root_dir)
    print("Found {} folders in directory {}".format(len(entries), root_dir))
    print("The following tasks will be processed:")
    for entry in entries:
        if os.path.isdir(root_dir + '/' + entry):
            print(" - {}".format(entry))

    # Load the CSV
    for entry in entries:
        if entry[-4:] == ".csv":
            if not "processed" in entry:
                csv_name = root_dir + '/' + entry
                break
    print("Found {} as the source names file".format(csv_name))

    csv_in = open(csv_name)
    reader = csv.DictReader(csv_in)

    students = []
    for s in reader:
        students.append(s)

    # construct a dict of only student {numbers : student name}
    stud_nums = {}
    for s in students:
        stud_nums[s["Student ID"].upper()] = "\"" + s["Student Name"] + "\""

    fieldnames = [] + reader.fieldnames

    # open a subdirectory
    for entry in entries:
        if os.path.isdir(root_dir + '/' + entry):
            print("Now working with {}".format(entry))
            fieldnames.append(entry)
            for item in os.listdir(root_dir + '/' + entry):
                studnums_found = re.findall(pattern=re.compile(r"[a-zA-Z]{6}[0-9]{3}"), string=item)
                studnums_found = [x.upper() for x in studnums_found]  # uppercase everything now
                studnums_found = sorted(studnums_found)

                # Dictionaries can't have duplicate keys so it auto-magically removes duplicates
                studnums_found = list(dict.fromkeys(studnums_found))

                for i in studnums_found:
                    # manage the renaming
                    # State that the student has submitted
                    for s in students:
                        if s["Student ID"].upper() == i.upper():
                            s[entry] = 'Y'

    # write out the file
    csv_out = open(csv_name[:-4] + "_processed.csv", 'w', newline='')
    writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

    # Finally, close the file
    csv_out.close()
    csv_in.close()

    return


def rename_submissions(root_dir):
    """
    Renames submissions according to <rootdir>_<subdir>_<STUD_NUM>_<Surname, name>.filetype
    For example, if you process a folder caleld "EEE3096S" and it contains a sub folder called "Prac 1", outputs will be
    'EEE3096S_Prac 1_STDNUM001_Number, Student.pdf
    :param root_dir:
    :return:
    """
    # Get practicals
    entries = os.listdir(root_dir)
    print("Found {} folders in directory {}".format(len(entries), root_dir))
    print("The following tasks will be processed:")
    for entry in entries:
        if os.path.isdir(root_dir + '/' + entry):
            print(" - {}".format(entry))
        if entry[-4:] == ".csv":
            csv_name = root_dir + '/' + entry
            break

    print("Found {} as the source names file".format(csv_name))

    csv_in = open(csv_name)
    reader = csv.DictReader(csv_in)

    students = []
    for s in reader:
        students.append(s)

    # construct a dict of only student {numbers : student name}
    stud_nums = {}
    for s in students:
        stud_nums[s["Student ID"].upper()] = s["Student Name"]

    # open a subdirectory
    for entry in entries:
        if os.path.isdir(root_dir + '/' + entry):
            print("Now working with {}".format(entry))
            for item in os.listdir(root_dir + '/' + entry):
                # Build a regex string to find all occurences of a subtstring
                studnums_found = re.findall(pattern=re.compile(r"[a-zA-Z]{6}[0-9]{3}"), string=item)
                studnums_found = [x.upper() for x in studnums_found]  # uppercase everything now
                studnums_found = sorted(studnums_found)

                # Dictionaries can't have duplicate keys so it auto-magically removes duplicates
                studnums_found = list(dict.fromkeys(studnums_found))
                s_new = "{} {}".format(root_dir, entry)
                fileformat = item[-4:]
                for i in studnums_found:
                    try:
                        s_new += " {} {}".format(i, stud_nums[i])
                    except:
                        s_new += " [{}]".format(i)
                        print("Could not find student number {}".format(i))
                s_new += fileformat
                try:
                    os.rename(root_dir + '/' + entry + '/' + item, root_dir + '/' + entry + '/' + s_new)
                except FileExistsError:
                    s_new = s_new.replace(fileformat, " DUPLICATE") + fileformat
                    os.rename(root_dir + '/' + entry + '/' + item, root_dir + '/' + entry + '/' + s_new)
                    print("Duplciate entry for {}".format(studnums_found))

    # Finally, close the file
    csv_in.close()

    return


if __name__ == "__main__":
    entries = os.listdir(".")
    for entry in entries:
        if os.path.isdir("." + '/' + entry):
            print("Now working with {}".format(entry))
            rename_submissions(entry)
            process_submissions(entry)