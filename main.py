def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    list_char_dicts = convert_char_dict(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")

    for c_d in list_char_dicts:
        if c_d["char"].isalpha():
            print(f"The '{c_d['char']}' character was found {c_d['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_char_dict(text):
    lower_text = text.lower()
    char_dict = {}
    for c in lower_text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def convert_char_dict(char_dict):
    list_char_dicts = []
    
    for key in char_dict:
        c_d = {"char": key, "num": char_dict[key]}
        list_char_dicts.append(c_d)

    list_char_dicts.sort(reverse=True, key=sort_on)
    return list_char_dicts

def sort_on(dict):
    return dict["num"]


main()