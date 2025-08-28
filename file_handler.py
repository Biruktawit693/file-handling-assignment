def modify_content(content):
    """
    Modify the file content in some way.
    For this example, we'll convert text to uppercase.
    You can change this to any modification you want.
    """
    return content.upper()


def main():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Try opening the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the file content
        modified_content = modify_content(content)

        # Create a new filename for output
        output_filename = "modified_" + input_filename

        # Write modified content to new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File successfully modified! Saved as '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
