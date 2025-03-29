#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
#Create a function to replicate center()
def center_replicate(prefix, width, char):
    right = 0
    left = 0
    need = width - len(prefix)
    if need % 2 == 0:
        right = need // 2
        left = right
    else:
        right = need // 2
        left = right + 1
    ljust = char * right
    rjust = char * left
    print(rjust + prefix + ljust)
#Utilize the created function
name = "Marxius"
center_replicate(name, 27, "-")
