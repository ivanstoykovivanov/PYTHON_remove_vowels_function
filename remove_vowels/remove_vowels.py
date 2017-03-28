def disemvowel(word):
    word_as_list = list(word)
    vowels = ["a" , "e", "i", "o", "u"]
    for char in word_as_list:
        for v in vowels : 
            if char == v : 
                word_as_list.remove(v)
    return "".join(word_as_list)  
        

print(disemvowel("apple"))
