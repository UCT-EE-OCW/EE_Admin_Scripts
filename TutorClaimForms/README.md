# Tutor Claim Forms
A script for auto-populating tutor claim forms, based on two CSVs (tutor details, and claims).  
There is currently no support for tutors involved with multiple courses.

 
## Requirements
 - Python 3+
 - Required Python libraries (requirements.csv)
 - PDFtk https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/
 - A CSV file containing tutor details (see example folder for formatting)
    - Filename expected is "tutors.csv"
 - A CSV containing the claims for each student (see example folder for formatting)
    - Filename expected is "[coursecode]_[courseconvenor]_[teachingassistant].csv"
 
## Use
Place the CSV files in the root directory, and run `python tutor_claim_forms` from a CLI.  
The script will return an output pdf for each tutor, named  
"[Tutor Surname] [Tutor Initial] [Course Convenor] [Course Code] Tutor Claim [Month] [Year].pdf"
