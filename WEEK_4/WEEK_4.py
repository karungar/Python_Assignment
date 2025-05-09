def process_file():
    """
    Simple program that reads a file and writes a modified version to a new file.
    """
    # Get filenames from user
    input_filename = input("Enter the input filename: ").strip()
    output_filename = input("Enter the output filename: ").strip()
    
    try:
        # Open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
        # Modify the content (in this example, by capitalizing it)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Success! File was read from '{input_filename}' and the modified version was written to '{output_filename}'")
        
    except Exception as error:
        print(f"An error occurred: {error}")

def read_file_with_error_handling():
    """
    Error handling when reading files.
    Asks the user for a filename and handles various potential errors.
    """
    while True:
        # Ask user for a filename
        filename = input("Enter the filename you want to read: ").strip()
        
        try:
            # Attempt to open and read the file
            with open(filename, 'r') as file:
                content = file.read()
                
            # If successful, print the content
            print("\nFile read successfully!")
            print("-" * 40)
            print(content)
            print("-" * 40)
            
        except FileNotFoundError:
            print(f"ERROR: The file '{filename}' was not found. Please check the filename and try again.")
            
        except PermissionError:
            print(f"ERROR: You don't have permission to access '{filename}'.")
            
        except IsADirectoryError:
            print(f"ERROR: '{filename}' is a directory, not a file.")
            
        except UnicodeDecodeError:
            print(f"ERROR: Unable to decode '{filename}' as text. It might be a binary file or use an unsupported encoding.")
            
        except IOError as e:
            print(f"ERROR: An I/O error occurred while reading '{filename}': {e}")
            
        except Exception as e:
            print(f"ERROR: An unexpected error occurred: {e}")
            
        finally:
            print("\nFile processing complete.")
            
        # Ask if user wants to try another file
        retry = input("\nWould you like to try another file? (y/n): ").strip().lower()
        if retry != 'y':
            print("Thank you for using the Error Handling Lab. Goodbye!")
            break

# Main execution block
if __name__ == "__main__":
    print("File Processing Program")
    print("======================")
    
    # Ask user which function to run
    print("\nPlease select a function:")
    print("1. Process a file (read, modify, write)")
    print("2. Read a file with error handling")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        process_file()
    elif choice == "2":
        read_file_with_error_handling()
    else:
        print("Invalid choice. Exiting program.")