document = open('day_6.txt', 'r')

print("begin")
text = document.read()
list = []
for char in text:
    list.append(char)
checker = []

for i in range(0, (len(list)-4)):
    sub = []
    found = 0
    for x in range(0,4):
        sub.append(list[x+i])
    for a in range(0,4):
        checker = sub[a]
        
        print(sub)
        for b in range(0,4):
            next = sub[b]
            if next == checker:
                found += 1
            print(checker, next, found)
            
    if found == 4:
        print(i+4, "found")
        quit()    