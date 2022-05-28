
# Giraffe Language 
# vowels -> g
# ---------------
# dog -> dgg 
# cat -> cgt 

#Converting vowels into some other letter 

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        # if letter in "AEIOU":
        #     translation = translation + "g"
        # elif letter in "aeiou":
        #     translation += "G"
        else:
            translation = translation + letter
    return translation


print(translator(input("Enter a phrase: ")))