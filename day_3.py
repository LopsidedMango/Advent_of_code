document = open("day_3.txt", "r")
found = False
list = []

while found == False:
    line = str(document.readline())
   
    line = line[0:(len(line)-1)]
    list.append(line)
    if line == "":
        found = True

def checker(first, second):
    found = []
    for i in range(0, (len(first))):
        check = first[i]
        
        for x in range(0, (len(second))):
           
            next = second[x]
           
            if next == check:
                found.append(check)
    return found


total = 0 
dup_found = False 

for i in range(0, (len(list)-1)):

    actual = list[i]
    first = actual[0:int((len(actual)/2))]
    second = actual[int((len(actual)/2)): int(len(actual))]
  
    found = checker(first, second)
    duplicate = [""]
    
    for x in range(0, (len(found))):
        dupe = 0 
        check = found[x]
        thing = len(found)
        for a in range(0, thing):
            next = found[a]
            if next == check:
                dupe += 1 
                if dupe >= 2:
                    found[a] = ''

    for b in range(0, len(found)):
        converter = found[b]
        
        if converter != "":
            
            if converter == converter.lower():
                
                converter = (((ord(converter)-97)%26)+1)
                total += converter 
            else:
                converter = (((ord(converter)-65)%26)+27)
                total += converter
print(total)

                
        


