# //////////////// STUDENT INFO /////////////////

# Student Name : Anurag Das
# Student ID   : 126031228
# Email        : adas35@myseneca.ca

# ///////////////////////////////////////////////


def wordCount(t):
    word_dict = {}

    try:
        with open(t, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.strip().split()
                for word in words:
                    if word in word_dict:
                        word_dict[word].append(line_number)
                    else:
                        word_dict[word] = [line_number]

    except FileNotFoundError:
        print(f"Error: File '{t}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return word_dict

# Using it for counting words
word_counts = wordCount('text_file.txt')
print(word_counts)
