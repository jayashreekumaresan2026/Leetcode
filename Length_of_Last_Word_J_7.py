s = "Hello world"
count = 0
splittedstring = s.split()
if len(splittedstring) > 0:
 count = len(splittedstring[-1])
print(count)