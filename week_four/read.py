# File Read & Write Challenge 🖋️

# Read content from input file
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (convert to uppercase for demo)
modified_content = content.upper()

# Write modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ File has been modified and saved as output.txt")

