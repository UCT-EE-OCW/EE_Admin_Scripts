# PDF Manipulator
Options to split, rotate, reverse and rename PDFs.   
Created with the intention to easily process bulk scans of assignments, tests, etc.   
Suggested use:
- Order documents by class number
- Scan to a single PDF
- Process in PDFManipulator

The simplest way to process a PDF is to put it in a file (eg "Quiz1") alongside a "names.csv" file, where the csv contains the names (no headings) in the order that the submissions are done.  
Then, edit the last line of pdf_manipulator.py with the correct options, and run `python pdf_manipulator.py`.