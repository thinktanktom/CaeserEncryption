mylist = []
c = "a"
for i in range(26):
    mylist.append(c)
    mylist[i]= chr(ord(c) + i)
print(mylist)

word = input("Enter the word")
l = list(word)
m = len(word)
key = int(input("Enter the key"))
for i in range(m):
    position = mylist.index(l[i])
    newposition = position + key
    print (mylist[newposition])
