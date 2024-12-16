import os

output_file = "all-code.txt"
ignore_files = {".DS_Store"}
ignore_dirs = {".git"}

# Open the output file for writing
with open(output_file, "w") as outfile:
    # Walk through all files and subdirectories
    for root, dirs, files in os.walk("."):
        # Remove ignored directories from the search
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for file in files:
            if file in ignore_files:
                continue
            
            file_path = os.path.join(root, file)
            # Write the file path to the output file
            outfile.write(f"File: {file_path}\n")
            # Write the contents of the file
            try:
                with open(file_path, "r") as infile:
                    outfile.write(infile.read())
            except Exception as e:
                outfile.write(f"Error reading file: {e}\n")
            # Add an empty line for separation
            outfile.write("\n")

print(f"All code has been saved to {output_file}")
