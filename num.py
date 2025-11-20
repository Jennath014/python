
    
import re

# Read the file
with open('xyz.txt', 'r') as f:
    data = f.read()

# Compile regex for 10-digit numbers starting with 6–9
pattern = re.compile(r'\b[6-9]\d{9}\b')

# Find all phone numbers
numbers = pattern.findall(data)

# Print results
print("Phone numbers found in file:")
for num in numbers:
    print(num)
