'''2.1. Write a program to create a list of names; then define a function 
to display all the elements in the received list. Call the function to 
execute its statements and display all names in the list.'''
names=[]
for i in range(5):
    n=input("Enter names")
    names.append(n)
def fun():
    print(names)
fun()
    
