def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document")
        print("")
        letters = count_letters(file_contents)
        letters_list = []
        for l in letters:
            if l.isalpha():
                letters_list.append({"name": l, "num": letters[l]})
        letters_list.sort(reverse=True, key=sort_on)
        for letter_dict in letters_list:
            print(f"The '{letter_dict['name']}' character was found {letter_dict['num']} times")

def sort_on(dict):
    return dict["num"]

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters
        


main()