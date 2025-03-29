#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
#Create a function to replicate lower()
def lower_replicate(prefix):
    table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    output = prefix.translate(table)
    print(output)
#Utilize the created function
