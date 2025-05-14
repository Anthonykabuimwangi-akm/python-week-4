#file read and write
def read_and_write_file(input_file, output_file):
    try:
        # Read the content from the input file
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file.")

# Usage
input_filename = 'example.txt'  # replace with your input file name
output_filename = 'modified_example.txt'  # replace with your desired output file name
read_and_write_file(input_filename, output_filename)

# error handling lab
def ask_for_filename():
    filename = input("Please enter the filename you want to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of {filename}:\n{content}")
            
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: Could not read the file {filename}.")

# Usage
ask_for_filename()