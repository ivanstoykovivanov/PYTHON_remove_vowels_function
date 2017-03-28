def disemvowel(word):
    word = word.lower()
    vowels = ["a" , "e", "i", "o", "u"]
    return "".join([char for char in word if char not in vowels])  

print( disemvowel("Aaaaron"))

