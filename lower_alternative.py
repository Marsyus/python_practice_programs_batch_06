#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
#Create a function to replicate lower()
def lower_replicate(text):
    table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    output = text.translate(table)
    return output
#Utilize the created function
name = "MArxIuS"
call = lower_replicate(name)
print(call)
