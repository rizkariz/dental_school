# Guessing what lesion is that

q_1 = input("Is the lesion raised above the skin? y/n:")
if q_1 == "y":
    q_12 = input("Is it filled by a liquid like substance? y/n:")
    if q_12 == "y":
        q_12a = input("Is it filled with clear liquid? y/n:")
        if q_12a == "y":
            q_12a1 = input("How about the diameter? Is it less than 1 cm? y/n:")
            if q_12a1 == "y":
                print("Ah, it's called vesicle.")
            elif q_12a1 == "n":
                print("Oh, it's bigger than 1 cm?\nMust be bullae then.")
        elif q_12a == "n":
            print("hmm, if it's filled with yellow or cloud like substance?\nIt's called pustulae")
            
    elif q_12 == "n":
        q_12b = input("hmmm take a look at the border of the lesion\nDoes it looks like a crater? y/n:")
        if q_12b == "y":
            print("Aha! If it's resembled a crater and it's a bit sunken.. it's an ulcer")
        elif q_12b == "n":
            q_12b1 = input("Does it appear multiple with scale-like appearance? y/n:")
            if q_12b1 == "y":
                print("Oh, that's must be a plaque then")
            elif q_12b1 == "n":
                q_12b1 = input("How about the diameter? Is it less than 1 cm? y/n:")
                if q_12b1 == "y":
                    print("Papule answer then it is")
                elif q_12b1 == "n":
                    print("Yup, it's a nodule then")

elif q_1 == "n":
    q_2 = input("How about the colour? Is it more red-ish and purple-ish colour wise? y/n:")
    if q_2 == "y":
        q_2a = input("Take a look at the size, Is it smaller than 1 cm? y/n:")
        if q_2a == "y":
            print("Eyyyy, that's called petechiae.")
        elif q_2a == "n":
            print("It's called purpura. ")
    elif q_2 == "n":
        q_2b = input("Check the sizes, is it smaller than 1 cm? y/n:")
        if q_2b == "y":
            print("Nice, that's what we called maculae.")
        elif q_2b == "n":
            print("Ay, it's called patch.")
                
            
        










       
