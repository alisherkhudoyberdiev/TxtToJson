import json

# Replace with the name of your input and output files
input_file = "input.txt"
output_file = "output.json"

# Read words from input file and create a dictionary
words_dict = {}
with open(input_file, "r") as f:
    for i, line in enumerate(f):
        words_dict[f"word_{i+1}"] = {"word": line.strip()}

# Write dictionary to JSON file
with open(output_file, "w") as f:
    json.dump({"key_word": list(words_dict.values())}, f, indent=4)
