# Read the manually cleaned file
with open("preproinsulin-seq-clean.txt", "r") as file:
    clean_sequence = file.read().strip()

# Make sure the clean sequence is exactly 110 characters long
assert len(clean_sequence) == 110, "The clean sequence does not have 110 characters!"


# Splits the sequence and creates the required files

# amino acids 1–24
with open("lsinsulin-seq-clean.txt", "w") as file:
    file.write(clean_sequence[:24])

# amino acids 25–54
with open("binsulin-seq-clean.txt", "w") as file:
    file.write(clean_sequence[24:54])

# amino acids 55–89
with open("cinsulin-seq-clean.txt", "w") as file:
    file.write(clean_sequence[54:89])

# amino acids 90–110
with open("ainsulin-seq-clean.txt", "w") as file:
    file.write(clean_sequence[89:110])

print("Files successfully created!")

