
def create_file():
    try:
        # Create a new text file and write initial content
        with open("my_file.txt", 'w') as file:
            file.write("This is line 01: Welcome to file handling.\n")
            file.write("This is line 02: This is at 2024.\n")
            file.write("This is line 03: Python is definately super easy !\n")
        print("File  has been created and written successfully.")
    except (PermissionError, Exception) as e:
        print(f"Error in creating file: {e}")

def read_file():
    try:
        # Read the contents of the file
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("\nContents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError:
        print("Error: 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file():
    try:
        # Append additional lines to the existing content
        with open("my_file.txt", 'a') as file:
            file.write("This is line 04: look forward for  more content.\n")
            file.write("This is line 05: Learning file handling was fun!\n")
            file.write("This is line 06: Let's  continue with the  practice.\n")
            file.write("The end .\n ")
        print("Content appended successfully.")
    except (PermissionError, Exception) as e:
        print(f"Error appending to file: {e}")

def main():
    create_file()      # Create and write to the file
    read_file()        # Read and display the file contents
    append_to_file()   # Append more content to the file
    read_file()        # Read and display the updated file contents

if __name__ == "__main__":
    main()
