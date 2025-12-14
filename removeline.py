result = []

with open("file.txt") as f:
    for line in f:
        s = line.strip()
        if not (s.startswith('a') and s.endswith('e')):
            result.append(s)

# Write filtered lines back to file
with open("file.txt", "w") as f:
    for line in result:
        f.write(line + "\n")

# Print lines for verification
print("Remaining lines:")
for line in result:
    print(line)


