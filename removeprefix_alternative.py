#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
#Create a function to replicate removeprefix()
def removeprefix_replicate(prefix, remove):
    if prefix.startswith(remove):
        output = prefix.replace(remove, "")
    else:
        output = prefix
    print(output)
#Utilize the created function
