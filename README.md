# File Handling & Exception Handling Assignment

## Program Description
This Python program reads the content of a file provided by the user, modifies the content (by converting it to uppercase), and writes the modified content into a new file. It also includes error handling to manage cases where the file does not exist or cannot be accessed.

---

## How It Works
1. **Ask for a filename**  
   The program prompts the user to enter the name of the file to read.

2. **Read the file**  
   The program opens the file in read mode and stores its contents.

3. **Modify the content**  
   The text is converted into uppercase letters.

4. **Write to a new file**  
   The modified content is written into a new file prefixed with `modified_`.

5. **Handle errors**  
   The program checks for possible errors:  
   - `FileNotFoundError`: if the file does not exist.  
   - `PermissionError`: if the user has no permission to read the file.  
   - General `Exception`: to catch any other unexpected errors.

---

## Outcome
By running this program, the user learns how to:
- Work with file input/output in Python.
- Apply basic content modification to files.
- Use exception handling to make the program reliable and user-friendly.

This ensures the program is robust, error-free, and meets the assignment requirements.
