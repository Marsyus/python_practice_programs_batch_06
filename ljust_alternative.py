#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
#Create a function to replicate ljust()
def ljust_replicate(text, width, char):
    text += char * width
    print(text)
#Utilize the created function
name = "Marxius"
ljust_replicate(name, 10, "-")
