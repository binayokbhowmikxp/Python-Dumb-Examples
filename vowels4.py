vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Please provide a word to search vowels: ")

found = {}

for v in vowels:
    found[v] = 0
 
for letter in word:
    if letter in vowels:
        found[letter] += 1
for vowel in found:
    print(f"{vowel} : {found[vowel]}")
       
