import base64
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 file64_decode.py <decode file64>")
        return

    file64 = sys.argv[1]

    if not os.path.isfile(file64):
        print("Error: Output file not found.")
        return

    # Read content from the file64
    with open(file64, 'r') as file:
        file_content = file.read()

    # Split the content into original file name and base64 string
    content_parts = file_content.split("|||")
    if len(content_parts) != 2:
        print("Error: Incorrect file format.")
        return

    original_file_name, base64_string = content_parts

    # Decode the base64 string
    try:
        decoded_bytes = base64.b64decode(base64_string)
    except:
        print("Error: Invalid base64 string.")
        return

    # Construct the output file name for the decoded content
    output_original_file_name = original_file_name.strip()  # Remove leading/trailing whitespace
    output_file_extension = os.path.splitext(output_original_file_name)[1]
    output_file_name = os.path.splitext(output_original_file_name)[0]

    # Check if the output file already exists
    counter = 0
    while True:
        output_file_path = f"{output_file_name}_decoded{counter}{output_file_extension}"
        if not os.path.exists(output_file_path):
            break
        counter += 1

    # Write the decoded content to the output file
    with open(output_file_path, 'wb') as file:
        file.write(decoded_bytes)

    print(f"Your file64 has been built and saved here: {output_file_path}")

if __name__ == "__main__":
    main()
