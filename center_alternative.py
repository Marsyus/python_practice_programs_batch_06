#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
#Create a function to replicate center()
def center_replicate(prefix, width, char):
    right = 0
    left = 0
    need = width - len(prefix)
#Utilize the created function
