input_file = "/Users/zhihanli/Desktop/cleaned.txt"
output_file = "/Users/zhihanli/Desktop/cleanedFinal.txt"
remove_words_file = "/Users/zhihanli/Desktop/geners_culture.txt"


with open(remove_words_file, "r") as file:
    remove_words = [line.strip() for line in file.readlines()]

# Read from the input file and write to the output file
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Remove lines that match exactly with any of the words in the remove_words list
        if line.strip() not in remove_words:
            outfile.write(line)

print("Cleaning complete. Check the output file.")