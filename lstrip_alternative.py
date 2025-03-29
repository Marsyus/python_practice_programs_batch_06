#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
#Create a function to replicate lstrip()
def lstrip_replicate(text):
    strip = True
    output = ""
    for i in text:
        if strip and i == " ":
	    continue
	else:
	    strip = False
            output += i
    return output
#Utilize the created function
name = "    Marxi   us"
call = lstrip_replicate(name)
print(call)
