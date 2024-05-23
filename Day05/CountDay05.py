import sys

# function to count and print file stats
def count_file(filename):
    with open(filename, 'r') as file:
        # get file stats
        text = file.read()
        lines = lines_number (text)
        words = words_number (text)
        chars = chars_number (text)
        
        # printing the file's stats
        print(f"The file {filename} has:")
        print(f"{chars} characters")
        print(f"{len(lines)} lines")
        print(f"{len(words)} words")

def lines_number(text):
    return text.split('\n')

def words_number (text):
    return text.split()

def chars_number (text):
    return len(text)

if __name__ == "__main__":
    # if filename was not input, print usage and exit
    if len(sys.argv) != 2:
        print("Usage: python count.py FILENAME")
        sys.exit(1)

    # else, run the count_file function
    filename = sys.argv[1]
    count_file(filename)
