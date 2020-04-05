# Check and Rename
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
```<rootdir> <subdir> <STUD_NUM> <Surname, name>.filetype```

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
│   ├── EEE3095S EEE3096S Practical 2 - Benchmarking STDNUM001 Number, Student.pdf
│   ├── EEE3095S EEE3096S Practical 2 - Benchmarking STDEXA001 Student, Example STDDMM001 Student, Dummy.pdf
└── IrrelevantFile.filetype
```
The program uses student numbers that are alphabetised as unique identifiers, hence their inclusion.

#### Processing Submissions
This can be performed on renamed or not submissions.
The application uses the names.csv file and goes through each folder. 
It creates an output csv called ```names_processed.csv``` which contains an column for each folder in the root directory. 
If a student number is found to be submitted, the program will mark that column with a "Y". 