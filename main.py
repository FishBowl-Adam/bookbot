from stats import word_count, char_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
book_path = sys.argv[1]

#filepath = "./books/frankenstein.txt"
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents  # Return the file contents
    # do something with f (the file) here
book = get_book_text(book_path)
total_words = word_count(book)
letter_counts = char_count(book)
#print(word_count(book), "words found in the document")
#print(char_count(book))

sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

# Print the report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")

for char, count in sorted_counts:
    print(f"{char}: {count}")

print("============= END ===============")