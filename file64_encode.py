import base64
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 file64_encode.py <input_file>")
        return

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print("Error: Input file not found.")
        return

    # Extract the original filename
    original_file_name = os.path.basename(input_file)

    with open(input_file, 'rb') as file:
        input_bytes = file.read()

    base64_string = base64.b64encode(input_bytes).decode('utf-8')

    # Construct the output file name for the encoded content with .file64 extension
    output_file = f"{original_file_name}.file64"

    # Write original file name, divider, and base64 string to the output file
    with open(output_file, 'w') as file:
        file.write(f"{original_file_name}|||{base64_string}")

    print(f"Your file64 has been encoded here: {output_file}")

if __name__ == "__main__":
    main()
