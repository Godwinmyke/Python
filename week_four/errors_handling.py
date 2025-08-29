# Error Handling Lab 🧪

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as infile:
        content = infile.read()
        print("📖 File content successfully read!")
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("⚠️ Error: You don’t have permission to read this file.")
else:
    # If no error, write the modified version
    with open("modified_" + filename, "w") as outfile:
        outfile.write(content.upper())
    print(f"✅ Modified file saved as modified_{filename}")

