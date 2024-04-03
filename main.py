def main():
    text = read_book("books/frankenstein.txt")
    words_count = count_words(text)
    letters = count_letters(text)
    letters = sort_by_occurence(letters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    print("")
    for l in letters:
        print(f"The '{l["letter"]}' character was found {l["count"]} times")
    print("--- End report ---")


def read_book(book_path:str):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text:str):
    words = text.split()
    return len(words)

def count_letters(text:str):
    text_in_lower_case = text.lower()
    letters = {}
    for letter in text_in_lower_case:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def sort_by_occurence(dictionary:dict):
    result_list = []
    for v in dictionary:
        result_list.append({"letter": v, "count": dictionary[v]})
    result_list.sort(key=sort_on, reverse=True)
    return result_list

def sort_on(dictionary:dict):
    return dictionary["count"]

main()
