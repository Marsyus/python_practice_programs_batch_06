#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
#Create a function to replicate isupper()
def isupper_replicate(text):
    upper_count = 0
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for i in text:
        if i in uppercase:
            upper_count += 1
    if upper_count == len(text):
        return True
    else:
        return False
#Utilize the created function
name = "MARXIUS IVAN"
call = isupper_replicate(name)
print(call)
