
# EE Admin Scripts
This is essentially a collection of tools developed to make admin requirements less tedious.
These tools can likely be improved, and users 

This code is published under the GNU Affero General Public License v3.0

## Check and Rename
Useful for testing student submissions and getting information for ECSA boxes.  
The script iterates over a collection of submission folders, renaming each file in a specified format, and marking a master csv indicating which students have submitted or not.

See README for more details.

## PDFFormEditor
Populates a PDF Form based on the data provided in a .csv file.
Good for generating ECSA forms for each student.  

Expects an included .csv with a column for each field in an editable PDF.
A good way to generate these forms is in Latex using the hyperref package. An example Latex Source for the ECSA form (used for EEE3096S 2019) is included.

## PDF Manipulator 
This was designed to make scanning and processing of forms and tests easier.  
Options for rotate, split, reverse and rename.  

The output of this script can be fed back in to Check and Rename.
  
This could work well as a CLI. So if anyone wants to do that and make a PR, please feel free.

## Tutor Claim Forms
Generates a pdf claim form for tutors based on two csv files.  
See README for more details.



