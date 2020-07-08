import csv
import os

# WE need a field called "studnums" in each?

def process(csv_name):
    # load in the CSV
    csv_in = open(csv_name)
    reader_main = csv.DictReader(csv_in)

    # create the output csv
    fieldnames = reader_main.fieldnames
    fieldnames = ["studnum", "partners"] + fieldnames
    fieldnames.remove("studnums")

    csv_out = open("{}_processed.csv".format(csv_name[:-4]), 'w', newline='')
    writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
    writer.writeheader()

    temp_arr = []

    # Split and add
    for i, row in enumerate(reader_main):
        studnums = row["studnums"].replace(" ", "").split(",")
        for s in studnums:
            if s is not None and s != "":
                cpy = studnums.copy()
                cpy.remove(s)
                tmp = {
                    "studnum": s,
                }
                tmp.update(row)
                tmp.pop("studnums")
                tmp["partners"] = cpy
                temp_arr.append(tmp)

    # sort list by studnum
    temp_arr = sorted(temp_arr, key=lambda i: i["studnum"])

    # write to file
    writer.writerows(temp_arr)

    # Finally, close the files
    csv_out.close()
    csv_in.close()


if __name__ == "__main__":
    root_dir = "."
    entries = os.listdir(root_dir)
    for entry in entries:
        if entry[-4:] == ".csv":
            if "_processed" not in entry:
                csv_name = root_dir + '/' + entry
                print("Working with {}".format(csv_name))
                process(csv_name)
