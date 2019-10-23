"""
Provide:
- a directory, containing subdirectories all holding a submission,
- a csv of names and student numbers.
The program will check all submissions and rename them
The student will be marked if they have a submission
"""

import csv # handles CSV operations
import os # handles directory access and renaming
import re # regex for finding student numbers

# load in the CSV

# check submissions in the primary directory

# for each submission dir, rename (whether file or folder) the submission text


def replace(studnum, lookup_dict):
    pass


def process(root_dir):

    # Get practicals
    entries = os.listdir(root_dir)
    print("Found {} folders in directory {}".format(len(entries), root_dir))
    print("The following tasks will be processed:")
    for entry in entries:
        if os.path.isdir(root_dir + '/' + entry):
            print(" - {}".format(entry))

    # Load the CSV
    for entry in entries:
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

    # print(stud_nums)

    print("_____________________________________________________")

    # open a subdirectory
    for entry in entries:
        print("Working with submission {}".format(entry))
        if os.path.isdir(root_dir + '/' + entry):
            print("Now working with {}".format(entry))
            for item in os.listdir(root_dir + '/' + entry):
                #new_name = regex.sub(replace(stud_num, ), item)
                s_new = item
                # Build a regex string to find all occurences of a subtstring
                studnums_found = re.findall(pattern=re.compile(r"[a-zA-Z]{6}[0-9]{3}"), string=item)
                for i in studnums_found:
                    # try:
                    s_new = s_new.replace(i, stud_nums[i.upper()])
                    # except:
                    #     print("STUDNUM {} NOT FOUND".format(i))

                os.rename(root_dir + '/' + entry + '/' + item, root_dir + '/' + entry + '/' + s_new)

    # write out the file
    csv_out = open(csv_name[:-4] + "_processed.csv", 'w')
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csv_out, fieldnames=fieldnames)

    # Finally, close the file
    csv_out.close()
    csv_in.close()

    return


if __name__ == "__main__":
    process("RenamingTest")