# sialolithiasis, sialadenitis, or mukokel

print("Answer the question with y/n")
while True:
    num_1 = input("Does the swelling painful?")
    if num_1 == "y":
        num_1a = input("Is there any prodromal sympton?")
        if num_1a == "y":
            print("It might be Sialadenitis")
            break
        elif num_1a == "n":
            print("might be sialolithiasis")
            break
        else:
            print("Invalid answer")
    elif num_1 == "n":
        num_1b = input("Is it located in the tongue?")
        if num_1b == "y":
            print("might be mukokel")
        elif num_1n == "n":
            print("Look out for the other anamnesis component")
        else:
            print("invalid answer")
    else:
        print("invalid answer")
            
        
        
        
    
