
#for each X we want a numbers of lines wich contain a numbers of y
print("'Exercice 1'")
var1 = int(input("ur range"))
for x in range(var1):
    for y in range(var1):
        print("*",end=" ")
    print()    

print("'Exercice 2'\n*numbers*")

for i in range(var1):
    for j in range(var1):
        print(i,end=" ")#we put here i because we wante to print i 
        #depending on j
    print()

for i in range(1,7):
    for j in range(1,6):
        print(j,end=" ")#on the contrary here we make j depending on i
    print()    

print("'Exercice 3'\n *characters*")

for x in 'ABCDE':
    for y in 'ABCDEF':#ABCDE means that's each charac from '--'will 
    #repeat 6 times.
        print(x,end="")
    print()    
#by anothor way we look at the ASCI and take the index of the
# characters want it and put it in a range function.
#look at https://theasciicode.com.ar/ for more.

for x in range(65,70):
    for y in range(1,6):
        print(chr(x),end="")
    print() 
print("Pattern 5")
for x in range(1,6):
    for y in range(65,70):
        print(chr(y),end="")
    print()
print("pattern 6")
for x in range(var1,-1):
    for y in range(var1,-1):
        print(x,end="")
    print()    
print("pattern 7")
for x in range(var1,-1):
    for y in range(var1,-1):
        print(y,end="")
    print()
print("pattern 8")
for x in range(69,64,-1):#we need to take ware about range be carefull
    for y in range(1,6,):
        print(chr(x),end="")
    print() 
print("pattern 9")
for x in range(1,6):
    for y in range(69,64,-1):
        print(chr(y),end="")
    print()  
print("pattern 10") 
for x in range(var1):
    for y in range(1,x + 1):
        print("*",end="")
    print()       

