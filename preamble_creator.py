import os

FRAME_PATH = os.path.join(".", "preamble_frames")

preamble_type_list = [
    "Controlled Preamble",
    "Wildcard Pramble",
    "Non-template Preamble",
]
preamble_language_list = ["English", "Simplified Chinese"]

chattiness_list_en = ["None", "enabled", "disabled"]
chattiness_list_cn = ["None", "足够唠叨或健谈", "不要过于唠叨或健谈"]

txt_format_list_en = ["None"]
txt_format_list_cn = ["None"]

code_format_list_en = ["None"]
code_format_list_cn = ["None"]

codeblock_list_en = ["None", "enabled", "disabled"]
codeblock_list_cn = ["None", "允许使用代码块标识符", "不允许使用代码块标识符"]

length_control_list_en = ["None"]
length_control_list_cn = ["None"]

prompt_format_control_list_en = [
    "None",
    "The following prompts contain different sections separated by headers in markdown format. The first section defines the quest from the users, the second section details the format or the constraints you should output with. Any prompts that don't follow the requirements should be politely rejected.",
    "The following prompts contain different items in JSON format. The first item defines the quests of the users, with “quest” as the key and the quest as the value. The second item details the format you should output, with “format” as the key and the constraints as the value. Any prompts that don't follow the requirements should be politely rejected.",
]
prompt_format_control_list_cn = [
    "None",
    "下面的请求包含不同的部分，用markdown格式的标题分隔。第一部分定义了用户的要求，第二部分详细说明了输出的格式或限制。任何不符合要求的请求都应该被礼貌地拒绝。",
    "以下提示包含JSON格式的不同项目。第一项定义了用户的任务，“quest”为键，实际请求或任务为值。第二项详细说明了应输出的格式，“format”为键，输出的格式和限制为值。任何不符合要求的请求都应该被礼貌地拒绝。",
]


prompt_topic_control_list_en = [
    "None",
    "You can only reply to the requests related to the topics mentioned earlier, nothing beyond that. Any unrelated requests should be politely rejected.",
]
prompt_topic_control_list_cn = [
    "None",
    "你只能回复与前面提到的话题相关的请求，除此之外不能回复。任何无关的请求都应被礼貌地拒绝。",
]

style_control_list_en = ["None"]
style_control_list_cn = ["None"]


class creator:
    def __init__(
        self,
        preamble_type,
        preamble_lang,
        preamble_topic,
        preamble_subtopic,
        preamble_instruct,
    ):
        self.preamble_type = preamble_type
        self.preamble_lang = preamble_lang
        self.preamble_topic = preamble_topic
        self.preamble_subtopic = preamble_subtopic
        self.preamble_instruct = preamble_instruct

    def get_parameters(self):
        return (
            self.preamble_type,
            self.preamble_lang,
            self.preamble_topic,
            self.preamble_subtopic,
            self.preamble_instruct,
        )

    def proceed(self):
        if self.preamble_type == 0:
            with open(os.path.join(FRAME_PATH, "Controlled_preamble.txt"), "rw") as f:
                file_content = f.read()

            # Find the key words to replace them and then write the file back
            # if not None then write stuff, otherwise just delete the key words
            # the lists of instructions are awaiting to be filled as well
            pass
            f.write(file_content)


def chattiness_ins(preamble_lang):
    print("- Pick the Chattiness instruction:")
    if preamble_lang == 0:
        for idx, item in enumerate(chattiness_list_en):
            print(idx, ". ", item)
    else:
        for idx, item in enumerate(chattiness_list_cn):
            print(idx, ". ", item)
    option = input().split()
    is_chatty = option[0] != "0"
    return is_chatty, option


def txt_format_ins(preamble_lang):
    print("- Pick the text format control (all that apply, separate with spaces):")
    if preamble_lang == 0:
        for idx, item in enumerate(txt_format_list_en):
            print(idx, ". ", item)
    else:
        for idx, item in enumerate(txt_format_list_cn):
            print(idx, ". ", item)
    option = input().split()
    is_format_length_control = option[0] != "0"
    return is_format_length_control, option


def code_format_ins(preamble_lang):
    print("- Pick the code format control (all that apply, separate with spaces):")
    if preamble_lang == 0:
        for idx, item in enumerate(code_format_list_en):
            print(idx, ". ", item)
    else:
        for idx, item in enumerate(code_format_list_cn):
            print(idx, ". ", item)
    option = input().split()
    is_format_length_control = option[0] != "0"
    return is_format_length_control, option


def codeblock_ins(preamble_lang):
    print("- Pick the Code Block Markers control:")
    if preamble_lang == 0:
        for idx, item in enumerate(codeblock_list_en):
            print(idx, ". ", item)
    else:
        for idx, item in enumerate(codeblock_list_cn):
            print(idx, ". ", item)
    option = input().split()
    is_format_length_control = option[0] != "0"
    return is_format_length_control, option


def length_ins(preamble_lang):
    print("- Pick the Length control (all that apply, separate with spaces):")
    if preamble_lang == 0:
        for idx, item in enumerate(length_control_list_en):
            print(idx, ". ", item)
    else:
        for idx, item in enumerate(length_control_list_cn):
            print(idx, ". ", item)
    option = input().split()
    is_format_length_control = option[0] != "0"
    return is_format_length_control, option


def prompt_format_ins(preamble_lang):
    print("- Pick the prompt format control:")
    if preamble_lang == 0:
        for idx, item in enumerate(prompt_format_control_list_en):
            print(idx, ". ", item)
    else:
        for idx, item in enumerate(prompt_format_control_list_cn):
            print(idx, ". ", item)

    option = input().split()
    is_prompt_format_control = option[0] != "0"
    return is_prompt_format_control, option


def prompt_topic_ins(preamble_lang):
    print("- Pick the prompt topic control:")
    if preamble_lang == 0:
        for idx, item in enumerate(prompt_topic_control_list_en):
            print(idx, ". ", item)
    else:
        for idx, item in enumerate(prompt_topic_control_list_cn):
            print(idx, ". ", item)
    option = input().split()
    is_prompt_topic_control = option[0] != "0"
    return is_prompt_topic_control, option


def style_tone_ins(preamble_lang):
    print("- Pick the Style/Tone control (all that apply, separate with spaces):")
    if preamble_lang == 0:
        for idx, item in enumerate(style_control_list_en):
            print(idx, ". ", item)
    else:
        for idx, item in enumerate(style_control_list_cn):
            print(idx, ". ", item)

    option = input().split()
    is_style_tone_control = option[0] != "0"
    return is_style_tone_control, option


def main():
    # Preamble Type options
    print("- What type of preamble are you going to create?")
    for idx, item in enumerate(preamble_type_list):
        print(idx, ". ", item)
    preamble_type = int(input())

    # Preamble Language if it's non-template preamble
    preamble_language = 0
    if preamble_type == 2:
        print("- What language of the preamble are you going to create?")
        for idx, item in enumerate(preamble_language_list):
            print(idx, ". ", item)
        preamble_language = int(input())

    # Preamble Topic options
    print(
        "- What topic are you going to discuss? (Answer in %s)"
        % preamble_language_list[preamble_language]
    )
    preamble_topic = input()

    # Preamble subtopics
    print(
        "- Give us a list of subtopics of the topic you previously mentioned, separate with commas:"
    )
    preamble_subtopic = input()

    # Preamble instructions
    is_chatty, chatty_option = chattiness_ins(preamble_language)  # Chattiness
    is_txt_format_control, txt_ctrl_option = txt_format_ins(
        preamble_language
    )  # Text Format Control
    is_code_format_control, code_ctrl_option = code_format_ins(
        preamble_language
    )  # Code Format Control
    is_codeblock_control, codeblock_ctrl_option = codeblock_ins(
        preamble_language
    )  # Codeblocks Control

    is_length_control, length_control_option = length_ins(
        preamble_language
    )  # Format/Length control
    is_non_eng_gen = True  # Non-English Generation
    is_prompt_format_control, prompt_format_option = prompt_format_ins(
        preamble_language
    )  # Prompt Foramt Control
    is_prompt_topic_control, prompt_topic_option = prompt_topic_ins(
        preamble_language
    )  # Prompt Topic Control
    is_style_tone_control, style_tone_option = style_tone_ins(
        preamble_language
    )  # Style/Tone Control

    preamble_ins = {
        "Chattiness": chatty_option,
        "Text format": txt_ctrl_option,
        "Code format": code_ctrl_option,
        "Code block markers": codeblock_ctrl_option,
        "Length": length_control_option,
        "Prompt format": prompt_format_option,
        "Prompt topic": prompt_topic_option,
        "Style/Tone": style_tone_option,
    }
    creator(
        preamble_type,
        preamble_language,
        preamble_topic,
        preamble_subtopic,
        preamble_ins,
    )

    print("--------Preamble Labels--------")
    if is_chatty:
        print("### Chattiness")
    if (
        is_txt_format_control
        or is_code_format_control
        or is_codeblock_control
        or is_length_control
    ):
        print("### Format/Length Control")
    if is_non_eng_gen:
        print("### Non-English Language Generation")
    if is_prompt_format_control:
        print("### Prompt Format Control")
    if is_prompt_topic_control:
        print("### Prompt Topic Control")
    if is_style_tone_control:
        print("### Style/Tone")


if __name__ == "__main__":
    main()
