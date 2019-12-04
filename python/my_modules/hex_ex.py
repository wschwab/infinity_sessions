string = "i never think of the future - it comes soon enough"

new_string = ""
for i in range(0,len(string)):
     if string[i] in ['a','b','c','d','e','f']:
          new_string = new_string + hex(ord(string[i])) + " "

print(new_string)
