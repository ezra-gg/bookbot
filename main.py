from stats import word_count, char_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def generate_report(book_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_file}...")
    
    total_words = word_count(book_file)
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    
    char_counts = char_count(book_file)
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    
    print("============= END ===============")

generate_report(sys.argv[1])