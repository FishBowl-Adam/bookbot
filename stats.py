def word_count(book):
    book_count =  len(book.split())
    return book_count

def char_count(book):
    letter_counts = {}
    char_count_l = book.lower()
    for char in char_count_l:
        if char.isalpha():
            # Increment the count if the letter exists, otherwise set it to 1
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts    

