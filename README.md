
# ELO Tools
This is essentially a collection of tools I developed to make ECSA admin requirements less tedious.
These tools aren't as well written as they could be, and could likely be improved.  
I'll put more effort in to it if more people require these tools, but I'm not really committed to any possible updates/feature additions.


## ELOPDFTool  
Options for rotate, split, reverse and rename.

A lot more work can be done on this (obviously) as it's very janky at the moment.  
Ideally, CLI should be developed to organise this. So if anyone wants to do that and make a PR, please feel free.

Thanks to these StackOverflow posts/users:
- [Rotating a PDF](https://stackoverflow.com/questions/46921452/python-batch-rotate-pdf-with-pypdf2)
- [Split a PDF](https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python)
- [Reverse a PDF](https://stackoverflow.com/questions/5425439/how-do-i-reverse-the-order-of-the-pages-in-a-pdf-file-using-pypdf)

## PDFFormEditor
Populates a PDF Form based on the data provided in a .csv file. Good for generating ECSA forms for each student

## check_rename
Contains two methods:
- rename_submissions
- process_submissions

The following assumptions are made: 
- A root folder containing a csv with names (column called "Student Name") and student numbers (column called "Student ID") is provided. 
- Within the root (course) folder is a folder for each submission.
- Submissions are at top level within that nested folder
- Only one submission per student
- Submission file types only have 3 characters (e.g. .pdf, .rar or .zip)
- Students correctly entered all student numbers on a submission
    - You'd be surprised how often incorrect student numbers are entered
    - The program tells you which folder it's currently working in and what the "unfound" student number is
    - You need to manually change the student number

#### Renaming submissions
Submissions are renamed according to
```<rootdir>_<subdir>_<STUD_NUM>_<Surname, name>.filetype```

Take the following file structure:
```
EEE3095S_EEE3096S/
├── names.csv
├── Practical 2 - Benchmarking
│   ├── Number, Student(stdnum001)_Submission attachment(s)_WhateverTheStudentCalledTheirSubmission.pdf
│   ├── Student, Example(stdexa001)_Submission attachment(s)_Prac2_stdexa001_stddmm001.pdf
└── IrrelevantFile.filetype
```

The program uses names.csv to rename the submissions to the following:
```
EEE3095S_EEE3096S/
├── names.csv
├── Practical 2 - Benchmarking
│   ├── EEE3095S_EEE3096S_Practical 2 - Benchmarking_STDNUM001_Number, Student.pdf
│   ├── EEE3095S_EEE3096S_Practical 2 - Benchmarking_STDEXA001_Student, Example_STDDMM001_Student, Dummy.pdf
└── IrrelevantFile.filetype
```
The program uses student numbers that are alphabetised as unique identifiers, hence their inclusion

#### Processing Submissions
This can be performed on renamed or not submissions.
The application uses the names.csv file and goes through each folder. It creates an output csv called ```names_processed.csv``` which contains an column for each folder in the root directory. If a student number is found to be submitted, it will mark it as found. 