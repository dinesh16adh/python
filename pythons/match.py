x = input("enter teh value of x: ")
match x:
    case 0:
        print ("X is 0")
        
    case 4:
        print ("X is 4")
        
    case _:
        print ("X is ",x)