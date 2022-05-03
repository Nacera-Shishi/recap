def is_a_word(Word):
    
    if Word[0].isupper():
        print(True)
    elif Word[0].islower():
        print(False)
    elif Word[0].isalpha():
        print(False)
    elif Word == "Mot-clé":
        print(True)

is_a_word("*")
        
        
            
        
    