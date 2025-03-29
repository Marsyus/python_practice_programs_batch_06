#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
#Create a function to replicate title()
def title_replicate(text):
    output = ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    upper_to_lower = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    lower_to_upper = str.maketrans("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    first = True
    for i in text:
        if first:
            output += i.translate(lower_to_upper)
            first = False
        else:
            if i in uppercase or i in lowercase:
                output += i.translate(upper_to_lower)
            else:
                first = True
                output += i
    return output
#Utilize the created function
name = "MaRxIuS Ivan Adolf Denniel"
call = title_replicate(name)
print(call)
