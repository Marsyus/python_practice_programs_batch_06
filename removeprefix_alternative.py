#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
#Create a function to replicate removeprefix()
def removeprefix_replicate(text, remove):
    if text.startswith(remove):
        output = text.replace(remove, "")
    else:
        output = text
    print(output)
#Utilize the created function
name = "MarxiusIvan"
removeprefix_replicate(name, "Marxius")
