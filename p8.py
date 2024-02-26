age=int(input("enter your age"))
if age>0 and age < 120:
    if age>0 and age <13:
        print("you are child")
    elif age >=13 and age <=18:
        print("you are teenager")
    elif age >18 and age <60:
        print("you are adult")
    else:
        print("you are senior")
else:
    print("Enter the valid age")
