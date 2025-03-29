#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
#Create a function to replicate title()
def title_replicate(prefix):
    output = ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    upper_to_lower = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    lower_to_upper = str.maketrans("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    first = True
#Utilize the created function
