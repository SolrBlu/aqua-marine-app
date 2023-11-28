import os
import sys
from parse_aqua_file import parse_aqua
from generate_html import generate_nextjs_code

def write_nextjs_file(nextjs_code, output_path):
    directory = output_path[:-7]
    if not os.path.exists(directory): # Check if the directory exists, and create it if it doesn't
        os.makedirs(directory)

    with open(output_path, 'w') as file:
        file.write(nextjs_code)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        aqua_file_path = sys.argv[1] # Get the file path from the command line argument 'aqua-language/src/pages/HelloWorld.aqua'
        nextjs_output_path = sys.argv[2] # Get nextjs output location nextjs-app/src/app/HelloWorld/page.js
        aqua_file_name = sys.argv[3].capitalize() # Get aqua file name HelloWorld (without .aqua)
        print(f"Parsing: {aqua_file_name}")
        page_content = parse_aqua(aqua_file_path, aqua_file_name) # Parsing the Aqua file
        nextjs_code = generate_nextjs_code(page_content) # Generating Next.js code
        write_nextjs_file(nextjs_code, nextjs_output_path) # Writing to the Next.js file
        print("Next.js file generated successfully.")
    else:
        print("No file path provided.")

print("")