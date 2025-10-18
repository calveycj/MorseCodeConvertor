from morse_code_dict import MORSE_CODE_DICT

def text_to_morse(string):
    answer = ""
    for char in string.upper():
        answer += MORSE_CODE_DICT[char]
    return answer.strip()
