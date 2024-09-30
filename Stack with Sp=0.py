global StackData
global StackPointer
StackData=[0]*10
StackPointer=0
def PrintStack():
    global StackData
    for x in range(len(StackData)):
        print(StackData[x])
    print("StackPointer:"+" "+str(StackPointer))
def Push(integerP):
    global StackData
    global StackPointer
    if StackPointer>9:
        return False
    else:
        StackData[StackPointer]=integerP
        StackPointer=StackPointer+1
        return True
for x in range(11):
    userinput=int(input("Please enter the numbers you want to add to Stack: "))
    temp=Push(userinput)
    if temp==True:
        print("Successfully added")
    else:
        print("Stack is full")
PrintStack()
def Pop():
    global StackData
    global StackPointer
    if StackPointer==0:
        return -1
    else:
        StackPointer=StackPointer-1
        temp=StackData[StackPointer]
        return temp
    



