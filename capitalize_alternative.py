#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
#Create a function to replicate capitalize()
def capitalize_replicate(prefix):
    output = ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    upper_to_lower = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    lower_to_upper = str.maketrans("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    first = True
    for i in prefix:
        if first:
            output += i.translate(lower_to_upper)
            first = False
        else:
            output += i.translate(upper_to_lower)
#Utilize the created function
