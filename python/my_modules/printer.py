print_this = input("Type something, and waaaaaatch me print it: ")

print(print_this)

list_this = input("Aaaaaand now, we'll do the same in a weirder way: ")

char_list = []
n = 0
while n < len(list_this):
    char_list.append(list_this[n])
    n += 1
print(char_list)

dict_this = input("Aaaaaaand finally, we'll count occurrences: ")

char_dict = {}
for i in dict_this:
    if i in char_dict:
        char_dict[i] += 1
    else:
        char_dict[i] = 1
print(char_dict)
