#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
#Create a function to replicate isupper()
def isupper_replicate(text):
    upper_count = 0
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for i in text:
        if i in uppercase:
            upper_count += 1
    if upper_count == len(text):
        print("True")
    else:
        print("False")
#Utilize the created function
name = "MARXIUS IVAN"
isupper_replicate(name)
