def file_read_write():
    try:
        # step 1: Ask the user for the input file name
        input_filename = input("Enter the filename to read from:").strip()

        #step 2: Try to open the file for reading
        with open('Mydata.txt', 'r') as infile:

            #step 3: Read file content
            content = infile.readlines()

        print(f"File '{input_filename}' read successfully!")

        #step 4: Process content (e.g, uppercase transformation)
        modified_content = [line.upper() for line in content]

        #step 5: Ask for an output filename
        output_filename = input("Enter the filename to write the modified content to: ").strip()

        #step 6: Write the modified content to the new file 
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print("Error: The file you specified does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read or write to the specified file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#Call the function to test
file_read_write()
