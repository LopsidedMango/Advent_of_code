stack = [[], [], [], [], [], [], [],[], []]
a = 0


temp_list = []
actual = ""
document = open("day_5.txt", "r")
for i in range(0, 8):
    a = 0 
    top =str(document.readline())
    temp_list.clear()
 
    for char in top:
        if char != "\n":
            temp_list.append(char)
    
 
    for i in range(0, 9):
        for x in range(0,3):
            if (x+a) <=35:
                if temp_list[x+a] != " ":
                    actual = actual + temp_list[x+a]
        a+=4
        
        if actual != "":
            stack[i].append(actual)
        
        actual = ""



def commander(stack, document):
    numbers = []
    for i in range(0,2):
        command = str(document.readline())
    for i in range(0,10):
        
        numbers.append(str(i))
    found =  False
    while found == False:
        command = str(document.readline())
        if command == "":
            found = True
        else:
            
            if len(command) == 19:
                move = command[5]
                from_ = command[12]
                to = command[17]
                
            else:
                move = command[5:7]
                from_ = command[13]
                to = command[18]
          
            mover(int(move), int(from_), int(to), stack)
    string = ""
 
    for i in range(0,9):
        string = string + stack[i][0]
    print(string)
def mover(move, from_, to, stack):
    
    from_ -= 1
    to -= 1
    
    for i in range(0, move):
    
        value = stack[from_][0]
        
        stack[from_].remove(value)
        stack[to].insert(0, value)

                
                        
                
                    
            
commander(stack, document)  
    
        
   
