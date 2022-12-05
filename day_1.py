document = open("day_1.txt", "r")
found = False
summer =  0
sums = [] 

while found == False:
        
    number = str(document.readline())
    
    if number == "end":
        found = True
        found2= True
    elif number == "\n":
        sums.append(summer)
        summer = 0
    elif number == " ":
        pass
    else:
        actual = int(number)
        summer += actual
print(max(sums))
