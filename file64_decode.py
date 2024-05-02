import base64
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 decode_file64.py <output_file>")
        return

    output_file = sys.argv[1]

    if not os.path.isfile(output_file):
        print("Error: Output file not found.")
        return

    # Extract the base name from the output file
    output_base_name, output_extension = os.path.splitext(output_file)

    # Extract the number from the output file
    try:
        output_number = int(output_base_name.split('_')[-1])
    except ValueError:
        print("Error: Invalid output file name format.")
        return

    # Construct the input file name
    input_file = f"{output_base_name}.txt"

    if not os.path.isfile(input_file):
        print("Error: Corresponding input file not found.")
        return

    with open(output_file, 'r') as file:
        base64_string = file.read()

    decoded_bytes = base64.b64decode(base64_string)

    # Determine the extension of the original file
    input_extension = os.path.splitext(input_file)[1]

    # Construct the output file name for the decoded content
    decoded_output_base_name = f"{output_base_name}_decode_"
    decoded_output_file = f"{decoded_output_base_name}{output_number:05}{output_extension}"

    # Check if the output file already exists and increment the number if necessary
    while os.path.exists(decoded_output_file):
        output_number += 1
        decoded_output_file = f"{decoded_output_base_name}{output_number:05}{output_extension}"

    with open(decoded_output_file, 'wb') as file:
        file.write(decoded_bytes)

    print(f"Decoded content saved to: {decoded_output_file}")

if __name__ == "__main__":
    main()
