# Tutor Claim Forms
A script for auto-populating tutor claim forms, based on two CSVs (tutor details, and claims).  
There is currently no support for tutors involved with multiple courses.

 
## Requirements
 - Python 3+
 - Required Python libraries (requirements.csv)
 - PDFtk https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/
 - A CSV file containing tutor details (see example folder for formatting)
    - Filename expected is "Tutors.csv"
 - A CSV containing the claims for each student (see example folder for formatting)
    - Filename expected is "[coursecode]_[courseconvenor]_[teachingassistant].csv"

## Files
- tutor_claim_forms.py  
    Contains the primary logic for creating a pdf from the two csvs
- helpers.py  
    Contains additional/"assistive" logic, mainly dealing with the PDF fields. Removed from the primary python script for readability.
- Example/  
    Contains the following example files to generate mock claim forms or use as a formatting guide:
    - EEE1111W_CName CSurname_TAName TASurname.csv
    - Tutors.csv  
    
## CSV Layout Requirements
### Tutors.csv
Columns in Tutors.csv:
- student_no: Used as a primary key. Must match case used in the claims file. 
- date_of_birth: Formatted as DD/MM/YYYY 
- email: 
- first_names: 
- surname: 
- cell_no:
- current_degree: must be one of [UG, MSc, PhD] (Case sensitive)
- year: how far into the degree the tutor is
 
 ### coursecode_courseconvenor_teachingassistant.csv
 Naturally
 - coursecode: The 8 character alphanumeric course code
 - couseconvenor: The course convenor for the course
 - teachningassistant: The TA for the course
 
 Columns in this csv:
 - Day: Day of the week, Monday through Sunday
 - Date: The date
 - Task: A description of the task completed by the tutors
 - Start: The start time.
 - End: The end time.
 - Tutor1: Column title is tutor's student_no, matching the case used in `Tutors.csv`. If a tutor didn't work this specific task, assign them 0 hours.
 - Tutor2: A second tutor. 
 - ...
 - TutorN: Continue for as many tutors as you need, ensuring each one can be found in `Tutors.csv`
 
## Use
Place the CSV files in the root directory, and run `python tutor_claim_forms` from a CLI.  
The script will return an output pdf for each tutor, named appropriately.
The second last line needs to be changed to the claims form source file (coursecode_courseconvenor_teachingassistant.csv) - see the example.
"[Tutor Surname] [Tutor Initial] [Course Convenor] [Course Code] Tutor Claim [Month] [Year].pdf"

