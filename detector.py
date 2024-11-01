import re
import os
import opencc
import string
from nltk import ngrams
from collections import Counter

RELA_PATH = "."  # Path of the file
FILE_NAME = "response.txt"  # Name of the file


def read_file(path):
    """
    read the file into a string
    """
    with open(path, "r", encoding="utf-8") as f:
        input_chinese = f.read()
    return input_chinese


def NTLDetector(text):
    """
    Detect non-Chinese characters, specifically English letters and punctuation.
    """
    count_en_letter = 0
    count_en_punc = 0

    en_letter = []
    en_punc = []
    flag_dash = 0
    for idx, chara in enumerate(text):
        if "A" <= chara <= "Z" or "a" <= chara <= "z":
            en_letter.append(chara)
            count_en_letter = count_en_letter + 1
        if chara in ":;,.?!'\"()":
            en_punc.append(chara)
            count_en_punc = count_en_punc + 1
        if (
            chara == "-"
            and text[idx - 1] in "1234567890"
            and text[idx + 1] in "1234567890"
            and flag_dash == 0
        ):
            print(
                "WARNING--- [Suspicious dash] detected! Check if it is legal! --- WARNING\n"
            )
            flag_dash = 1

    if count_en_letter:
        print("WARNING--- [English letter] detected: ---WARNING")
        print(en_letter)
    if count_en_punc:
        print("WARNING--- [English punctuation] detected: ---WARNING")
        print(en_punc)
    if count_en_letter + count_en_punc:
        print(
            "SUM--- The amount of English letters and English punc is: ",
            count_en_letter + count_en_punc,
            "\n",
        )


def other_non_cn(text):
    """
    Detect other non-Chinese characters, such as numbers and emojis.
    """
    count = 0
    other_non_cn = []
    for chara in text:
        if (
            not "A" <= chara <= "Z"
            and not "a" <= chara <= "z"
            and chara not in ":;,.?!'\"()"
            and chara not in "12345677890"
        ):
            if not "\u4e00" <= chara <= "\u9fff":
                other_non_cn.append(chara)
                count = count + 1

    if count:
        print(
            "WARNING--- [Other Non-Simplified Chinese] characters detected: ---WARNING"
        )
        print(other_non_cn)
        print(
            "SUM--- The amount of other non-Simplified Chinese characters is: ",
            count,
            "\n",
        )


def traditional_chinese_detect(text):
    """
    Detect Traditional Chinese.
    """
    converter = opencc.OpenCC("t2s.json")
    converted_chinese = converter.convert(text)
    trad_cn = []

    if text != converted_chinese:
        print(
            "WARNING--- [Traditional Chinese] Detected! Check if they are legal: ---WARNING"
        )
        for idx, _ in enumerate(text):
            if text[idx] != converted_chinese[idx]:
                trad_cn.append(text[idx])
        print(trad_cn)
        print(
            "SUM--- The amount of Traditional Chinese characters is: ",
            len(trad_cn),
            "\n",
        )


def count_emoji(content):
    """
    Count the number of emojis so that it's more accurate when counting characters
    [one emoji = one character]
    """
    try:
        # Wide UCS-4 build
        cont = re.compile(
            "[" "\U0001f300-\U0001f64f" "\U0001f680-\U0001f6ff" "\u2600-\u2b55]+"
        )
    except re.error:
        # Narrow UCS-2 build
        cont = re.compile(
            "("
            "\ud83c[\udf00-\udfff]|"
            "\ud83d[\udc00-\ude4f\ude80-\udeff]|"
            "[\u2600-\u2b55])+"
        )

    return len(content) - len(cont.sub("", content))


def tone_consistent(text):
    """
    The appellation 你 and 您 should not exist at the same time.
    """
    if (text.find("你") != -1) and (text.find("您") != -1):
        print(
            "WARNING--- Inconsistent Tone (你vs您) detected, check if it/they is/are legal! ---WARNING"
        )


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

    print(
        "COUNT--- Characters (without whitespaces) in total: ",
        len(text),
    )
    print(
        "COUNT--- Emojis in total: ",
        count_emoji(text),
    )
    if len_before_eli != len(text):
        print(
            "WARNING--- [Space(s)] detected, check if it/they is/are legal! ---WARNING"
        )
        print("SUM--- Number of spaces: ", len_before_eli - len(text), "\n")

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
            "；": "",
            "、": "",
            "（": "",
            "）": "",
            "《": "",
            "》": "",
            "【": "",
            "】": "",
        }
    )
    translator.update(str.maketrans("", "", string.punctuation))  # type: ignore

    len_before_eli_punc = len(text)
    text = text.translate(translator)
    num_of_punc = len_before_eli_punc - len(text)

    other_non_cn(text)
    traditional_chinese_detect(text)

    count = 0
    for a in text:  # Chinese Characters range in between 4e00 and 9fff
        if "\u4e00" <= a <= "\u9fff":
            count = count + 1

    print("COUNT--- 汉字 in total: ", count)
    print("COUNT--- 汉字 and 标点 in total: ", count + num_of_punc, "\n")

    return text


def seg_char(text):
    """
    Tokenize Chinese characters
    """

    # Note: English words won't be separated char-by-char after updating.
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


def show_repeat(in_list, r_type, k=3):
    """
    Show all the repeated segments, 3 times of occurrence by default
    """
    b = dict(Counter(in_list))

    # Set up value >= 3 cuz only when the times of appearance is >= 3, we count it as repetition
    output_dict = {key: value for key, value in b.items() if value >= k}
    if len(output_dict):
        print("WARNING--- Repetition of", r_type, "type detected: ---WARNING")
        for key, value in output_dict.items():
            print(
                key, ": ", value, "times!"
            )  # show the repeated elements and the correspinding times
    else:
        print("SUM--- No", r_type, "repetition found!")


def main():
    input_chinese = read_file(os.path.join(RELA_PATH, FILE_NAME))
    cleaned_text = clean_text(input_chinese)
    tone_consistent(cleaned_text)
    tokenized_text = seg_char(cleaned_text)
    # short but a lot repetition
    len_repe_short_but_many = 4  # Minimum length to be counted as repetition, default=3
    times_repe_short_but_many = (
        4  # Minimum times of occurrence to be counted as repetition, default=3
    )
    three_grams = ngram_analysis(tokenized_text, len_repe_short_but_many)
    show_repeat(three_grams, "short", times_repe_short_but_many)

    # few but long repetition
    len_repe_few_but_long = 8  # Minimum length to be counted as repetition, default=3
    times_repe_few_but_long = (
        2  # Minimum times of occurrence to be counted as repetition, default=3
    )
    three_grams = ngram_analysis(tokenized_text, len_repe_few_but_long)
    show_repeat(three_grams, "long", times_repe_few_but_long)


if __name__ == "__main__":
    main()
