import re
import string
from nltk import ngrams
from collections import Counter

# The following text is the text you want to see if there is any repetition
input_chinese = """

次日，于桃园中备下乌牛白马祭礼等项。三人焚香再拜而 say誓曰：“念刘备、关羽、张飞，虽然异姓，既结为兄弟，则同心协力，救困扶危，上报国家，下安黎庶。不求同年同月同日生，只愿同年同月同日死。皇天后士，实鉴此心。背义忘恩，天人共戮！”誓毕，拜玄德为兄，关羽次之，张飞为弟。祭罢天地，复宰牛设酒，聚乡中勇士得三百馀人，就桃园中痛饮一醉。...!?你？？？

"""


def clean_text(text):
    """
    Clean up the punctuations and whitespaces that may appear in the text

    """

    # Eliminate HTML lables and entities
    text = re.sub(r"<.*?>", "", text)

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
            "~": "",
        }
    )
    translator.update(str.maketrans("", "", string.punctuation))
    text = text.translate(translator)

    # Detele extra white spaces
    text = re.sub(r"\s+", "", text).strip()

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
    Show all the repeated segments, 3 times of occurance by default
    """
    b = dict(Counter(in_list))

    # Set up value >= 3 cuz only when the times of appearance is >= 3, we count it as repetition
    output_dict = {key: value for key, value in b.items() if value >= k}
    if len(output_dict):
        print(output_dict)  # show the repeated elements and the correspinding times
    else:
        print("This text doesn't contain any repetition!")


def main():
    len_repe = 3  # Minimum length to be counted as repetition, default=3
    times_repe = 2  # Minimum times of occurance to be counted as repetition, default=3
    cleaned_text = clean_text(input_chinese)
    tokenized_text = seg_char(cleaned_text)
    three_grams = ngram_analysis(tokenized_text, len_repe)
    show_repeat(three_grams, times_repe)


if __name__ == "__main__":
    main()
