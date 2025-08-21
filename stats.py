def get_word_count(string):
    words = string.split()
    count = len(words)
    return count

def get_letter_count(string):
    letter_count = {}
    for letter in string:
        lowered = letter.lower()
        if not lowered in letter_count:
            letter_count[lowered] = 0
        letter_count[lowered] += 1
    return letter_count

def report(str_dict):
    str_list = []
    for key in str_dict:
        if key.isalpha():
            tmp_dict = {}
            tmp_dict["char"] = key
            tmp_dict["num"] = str_dict[key]
            str_list.append(tmp_dict)
    str_list.sort(reverse=True,key=sort_to)
    return str_list

def sort_to(list):
    return list["num"]