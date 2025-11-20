
input_string = "Hello, World!"


resultant_string = input_string[::2]

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in resultant_string if char in vowels)

print("Resultant String:", resultant_string)
print("Number of vowels in the resultant string:", vowel_count)
