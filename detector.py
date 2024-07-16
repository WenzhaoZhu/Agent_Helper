import re
import os
import string
from nltk import ngrams
from collections import Counter

RELA_PATH = "." # Path of the file
FILE_NAME = "response.txt" # Name of the file

def read_file(path):
    """
    read the file into a string
    """
    with open(path, "r", encoding='utf-8') as f:
        input_chinese = f.read()
    return input_chinese

def NTLDetector(text):
    for chara in text:
        if 'A' <= chara <= 'Z' or 'a' <= chara <= 'z':
            print("English letter --", chara, "-- detected!")
        if chara in ":;,.?!'\"()":
            print("English punctuation --", chara, "-- detected!")
    
def clean_text(text):
    """
    Clean up the punctuations and whitespaces that may appear in the text

    """
    # print("Length before eliminate white changelines: ", len(text))

    # Detele extra changelines
    text = re.sub(r"\n+", "", text).strip()
    len_before_eli = len(text)

    # Detele extra spaces
    text = re.sub(r" +", "", text).strip()

    # Show the number of characters in the text, without any whitespace
    # print("Text: ", text)
    print("Characters in total: ", len(text))
    if len_before_eli != len(text):
        print("There is/are -- space(s) -- in the response, check if it/they is/are legal!")
        print("Number of spaces: ", len_before_eli - len(text))

    # Eliminate HTML lables and entities
    text = re.sub(r"<.*?>", "", text)

    # Detect if English and some punctuation exists
    NTLDetector(text)

    # Subtract punctuations, including unicode characters
    translator = str.maketrans(
        {
            "\u2018": "",
            "\u2019": "",  # Single quotes
            "\u201c": "",
            "\u201d": "",  # Double quotes
            "\u2026": "",
            "\u2013": "",
            "\u2014": "",  # Ellipsis and dashes
            "，": "",
            "。": "",
            "！": "",
            "？": "",
            "：": "",
            "、": "",
        }
    )
    translator.update(str.maketrans("", "", string.punctuation)) # type: ignore
    text = text.translate(translator)
    print("汉字 in total: ", len(text))

    return text


def seg_char(text):
    """
    Tokenize Chinese characters
    """

    # Note: English words will be separated char-by-char as well
    pattern = re.compile(r"([\u4e00-\u9fa5])")
    chars = pattern.split(text)
    chars = [w for w in chars if len(w.strip()) > 0]
    return chars


def ngram_analysis(tokens, n=3):
    """
    Get all the segments that the length is of n, 3 by default
    """
    # Using ngrams API to get the sets of length 3
    three_grams = ngrams(tokens, n)

    # Merge each set into one string
    tri_grams = []
    for item in three_grams:
        a = "".join(word for word in list(item))
        tri_grams.append(a)
    return tri_grams


def show_repeat(in_list, k=3):
    """
    Show all the repeated segments, 3 times of occurrence by default
    """
    b = dict(Counter(in_list))

    # Set up value >= 3 cuz only when the times of appearance is >= 3, we count it as repetition
    output_dict = {key: value for key, value in b.items() if value >= k}
    if len(output_dict):
        print("Repetition Detected:")
        for key, value in output_dict.items():
            print(key, ": ", value, "times!") # show the repeated elements and the correspinding times
    else:
        print("This text doesn't contain any repetition!")

    
def main():

    input_chinese = read_file(os.path.join(RELA_PATH, FILE_NAME))
    cleaned_text = clean_text(input_chinese)
    tokenized_text = seg_char(cleaned_text)

    # short but a lot repetition
    len_repe_short_but_many = 4  # Minimum length to be counted as repetition, default=3
    times_repe_short_but_many = 3  # Minimum times of occurrence to be counted as repetition, default=3
    three_grams = ngram_analysis(tokenized_text, len_repe_short_but_many)
    show_repeat(three_grams, times_repe_short_but_many)

    # few but long repetition
    len_repe_few_but_long= 6  # Minimum length to be counted as repetition, default=3
    times_repe_few_but_long = 2  # Minimum times of occurrence to be counted as repetition, default=3
    three_grams = ngram_analysis(tokenized_text, len_repe_few_but_long)
    show_repeat(three_grams, times_repe_few_but_long)

if __name__ == "__main__":
    main()
