# Agent_Helper
## Updates
### July 18, 2024
- seg_char() function no longer separates English letters character by character, it takes English words as a whole now.
### July 16, 2024
- Adding the function of only counting 汉字.
- Adding "few but long repetition" detections.
- Distinguishing "short but many repetition" detections and "few but long repetition" detections.
- Adding the function of detecting other non-Chinese characters.
- Adding the function of counting the number of English characters and other non-Chinese characters.
### June 28, 2024
- Detecting suspicious spaces.
- The new file ```preamble_creator.py``` can show the labels of the preambles.
### June 11, 2024
- Showing the number of characters in the text, excluding whitespaces only.
- Importing text from a file; it is no longer a variable.
- Showing English letters and punctuation.

## Requirements
- re
- nltk
## Run
### For response analysis：
  ```
  python detector.py
  ```

## Parameters
- **RELA_PATH**: the path to the file.
- **FILE_NAME**: the name of the file, "response.txt" by default.
- **len_repe_short_but_many**: minimum length to be counted as short repetition, default=3.
- **times_repe_short_but_many**: minimum times of occurrence to be counted as short repetition, default=3.
- **len_repe_few_but_long**: minimum length to be counted as long repetition, default=3.
- **times_repe_few_but_long**: minimum times of occurrence to be counted as long repetition, default=3.

## To-do
- Complete ```preamble_creator.py```
  - Complete the class ```creator```
  - Complete the instruction lists
