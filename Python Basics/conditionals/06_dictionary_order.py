# Print two given words in dictionary order
# ord() --> gives unicode of given character


# useless program


word1, word2 = input("Enter two space separated words having different characters:\n ").split()

if word1 == word2:
    print("Enter different words")
else:
    w1_first_letter = ord(word1[0])
    w2_first_letter = ord(word2[0])

    if w1_first_letter < w2_first_letter:
        print(word1, word2)
    else:
        print(word2, word1)