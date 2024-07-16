# Agent_Helper
## Updates
### July 16, 2024
- Adding the function of only counting 汉字.
- Adding "few but long repetition" detections.
- Distinguishing "short but many repetition" detections and "few but long repetition" detectuions.
### June 28, 2024
- Detecting suspicious spaces.
- The new file ```preamble_creator.py``` can show the labels of the preambles.
### June 11, 2024
- Showing the number of characters in the text, excluding whitespaces only.
- Importing text from a file, not a variable anymore.
- Showing English letters and punctuation.

## Requirements
- re
- nltk
## Run
### For response analysis：
  ```
  python detector.py
  ```
### For preamble creating:
  ```
  python preamble_creator.py
  ```
## Parameters
- **RELA_PATH**: the path to the file.
- **FILE_NAME**: the name of the file, "Chinese_detector.txt" by default.
- **len_repe**: minimum length to be counted as repetition, default=3.
- **times_repe**: minimum times of occurrence to be counted as repetition, default=3.

## To-do
- Complete ```preamble_creator.py```
  - Complete the class ```creator```
  - Complete the instruction lists
