# Agent_Helper
## Updates
### Oct 31, 2024
- Change back the emoji counting to [1 emoji = 1 character]
- Adding function to detect inconsistent appellations.
### Sept 24, 2024
- Numbers will no longer be detected as NTL.
- Fixing the issue of repeatedly presenting warnings for detecting dashes.
### Sept 19, 2024
- Adding the function of counting emojis so that 1 emoji = 2 characters can be applied.
### Sept 7, 2024
- Adding function: detecting suspicious dash "-", only when the previous character and the later character are both numbers can the "-" be taken as suspicious.
### Aug 25, 2024
- Fixing the issue of not being able to show the Traditional Chinese in ```detector.py```
- Fixing the issue of not being able to show the Simplified Chinese in ```detector_tc.py```
### Aug 24, 2024
- Optimizing the output format for the detectors.
  - Adding labels for outputs:
    - WARNING
    - COUNT
    - SUM
- Updating the demo response for the test.
### Aug 20, 2024
- Bugs fixing in ```detector_tc.py```
### Aug 19, 2024
- Bugs fixing.
- Now there won't be any warning if there is no English character or other non-Chinese character in the response.
- Traditional Chinese detecting for ```detector.py```.
- Creating a Traditional-Chinese-Agent-Oriented detector ```detector_tc.py```.
  - Way of using is completely the same as ```detector.py```.
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
### June 11, 2024
- Showing the number of characters in the text, excluding whitespaces only.
- Importing text from a file; it is no longer a variable.
- Showing English letters and punctuation.

## Requirements
- re
- nltk
- opencc
## Run
### For Simplified Chinese agents：
  ```
  python detector.py
  ```
### For Traditional Chinese agents:
  ```
  python detector_tc.py
  ```

## Parameters
- **RELA_PATH**: the path to the file.
- **FILE_NAME**: the name of the file, "response.txt" by default.
- **len_repe_short_but_many**: minimum length to be counted as short repetition, default=3.
- **times_repe_short_but_many**: minimum times of occurrence to be counted as short repetition, default=3.
- **len_repe_few_but_long**: minimum length to be counted as long repetition, default=3.
- **times_repe_few_but_long**: minimum times of occurrence to be counted as long repetition, default=3.

## To-do/Feedback from users
- GUI
- Formal/Informal consistency detection
