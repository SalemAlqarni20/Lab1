

file_name = "lab_sample.txt"

with open(file_name, mode="w", encoding="utf-8") as file:
    file.write("Line 1: Introduction to Python File Handling.\n")
    file.write("Line 2: Python makes managing files straightforward.\n")
print(f"File '{file_name}' created and populated successfully.")

with open(file_name, mode="r", encoding="utf-8") as file:
    content = file.read()
    print("--- Reading Entire Content ---")
    print(content)

with open(file_name, mode="r", encoding="utf-8") as file:
    print("--- Reading Line by Line ---")
    for line_num, line in enumerate(file, start=1):
        print(f"{line_num}: {line.strip()}")

with open(file_name, mode="a", encoding="utf-8") as file:
    file.write("Line 3: Appended entry at the end of the file.\n")

missing_file = "non_existent_file.txt"
try:
    with open(missing_file, mode="r", encoding="utf-8") as file:
        data = file.read()
except FileNotFoundError:
    print(
        f"\nError Handled: The file '{missing_file}' was not found. Continuing execution cleanly."
    )

with open("exercise1_input.txt", "w", encoding="utf-8") as f:
    f.write("Hello world!\nWelcome to the Python File I/O lab.\nHappy coding!")

line_count = 0
word_count = 0
with open("exercise1_input.txt", "r", encoding="utf-8") as file:
    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)
print(f"Total Lines: {line_count}")
print(f"Total Words: {word_count}")

with open("source.txt", "w", encoding="utf-8") as file:
    file.write("Important Data Row 1\nImportant Data Row 2\nImportant Data Row 3\n")

source_filename = "source.txt"
backup_filename = "backup.txt"

with open(source_filename, mode="r", encoding="utf-8") as src, \
     open(backup_filename, mode="w", encoding="utf-8") as dest:
    content = src.read()
    dest.write(content)

print(f"Successfully copied '{source_filename}' to '{backup_filename}'.")

with open(backup_filename, mode="r", encoding="utf-8") as check_file:
    print("\nVerified Backup Content:")
    print(check_file.read())
