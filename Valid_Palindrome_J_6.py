s = "A man, a plan, a canal: Panama"
my_string = ""
for char in s.lower():
 if char.isalnum():
    my_string += char
print(my_string==my_string[::-1])