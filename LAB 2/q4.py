# //////////////// STUDENT INFO /////////////////

# Student Name : Anurag Das
# Student ID   : 126031228
# Email        : adas35@myseneca.ca

# ///////////////////////////////////////////////


def stats_decorator(func):
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        print("Numbers read:", numbers)
        print("Count:", len(numbers))
        print("Average:", sum(numbers) / len(numbers) if numbers else 0)
        print("Maximum:", max(numbers) if numbers else "N/A")
    return wrapper

@stats_decorator
def readNumbers(t):
    numbers_list = []
    try:
        with open(t, 'r') as file:
            for line in file:
                numbers = [float(num) for num in line.strip().split()]
                numbers_list.extend(numbers)
    except FileNotFoundError:
        print(f"Error: File '{t}' not found.")
    except ValueError:
        print(f"Error: Invalid numeric data in file '{t}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return numbers_list

# Example usage:
file_path = 'numbers_file.txt'  # Replace with the actual path to your text file
readNumbers(file_path)
