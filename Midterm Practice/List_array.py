mainlist = []
#source1 = [1,2,3,4]
source1 = []
source2 = [5,6,7,8]


while source1 != [] or source2 != []:
    
    if source1 != [] and source2 == []:
        mainlist.append(source1.pop())
        
    elif source1 == [] and source2 != []:
        mainlist.append(source2.pop())
        
    elif source1 != [] and source2 != []:
        mainlist.append(source1.pop())
        mainlist.append(source2.pop())

    

print (mainlist)




