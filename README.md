
# ELO Tools
These tools are badly written and not Pythonic in any way, shape or form.  
I'll put more effort in to it if more people require these tools.

## ELOPDFTool  
Options for rotate, split, reverse and rename.

A lot more work can be done on this (obviously) as it's very janky at the moment.  
Ideally, CLI should be developed to organise this. So if anyone wants to do that and make a PR, please feel free.


#### Thanks to these Stackoverflow posts/users:
- [Rotating a PDF](https://stackoverflow.com/questions/46921452/python-batch-rotate-pdf-with-pypdf2)
- [Split a PDF](https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python)
- [Reverse a PDF](https://stackoverflow.com/questions/5425439/how-do-i-reverse-the-order-of-the-pages-in-a-pdf-file-using-pypdf)

# PDFFormEditor
Populates a PDF Form based on the data provided in a .csv file. Good for generating ECSA forms for each student

# check_rename
Replaces student numbers with student names and creates a csv for each folder. A folder represents a submission. So you can just throw all the prac submissions in one root folder along with a csv, it'll replace all student numbers with student names, and you'll be able to see who is missing any submissions.
