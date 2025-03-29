#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
#Create a function to replicate swapcase()
def swapcase_replicate(text):
    output = ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    upper_to_lower = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    lower_to_upper = str.maketrans("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in text:
        if i in uppercase:
            output += i.translate(upper_to_lower)
        elif i in lowercase:
            output += i.translate(lower_to_upper)
        else:
            output += i
    print(output)
#Utilize the created function
name = "MaRxIuS"
swapcase_replicate(name)
