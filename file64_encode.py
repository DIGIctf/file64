#FILE64
#Send any file instantly to someone after you get the base64 string of a file
#Created by Digi Jeff
import base64
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 file64.py <input_file>")
        return

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print("Error: Input file not found.")
        return

    output_base_name = 'file64_'
    output_number = 1
    output_file = f"{output_base_name}{output_number:05}.txt"

    while os.path.exists(output_file):
        output_number += 1
        output_file = f"{output_base_name}{output_number:05}.txt"

    with open(input_file, 'rb') as file:
        encoded_string = base64.b64encode(file.read())

    base64_string = encoded_string.decode('utf-8')

    with open(output_file, 'w') as file:
        file.write(base64_string)

    print(f"Base64 content saved to: {output_file}")

if __name__ == "__main__":
    main()

