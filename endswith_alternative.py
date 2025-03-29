#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
#Create a function to replicate endswith()
def endswith_replicate(text, ending):
    text += "x"
    if ending + "x" in text:
        return True
    else:
        return False
#Utilize the created function
name = "Marxius Ivan"
call = endswith_replicate(name, "Ivan")
print(call)
