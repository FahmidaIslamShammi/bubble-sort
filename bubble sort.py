#list=[23,45,78, 92, 23, 110, 92, 45, 15, 20, 22, 21, 15, 17, 20, 80] 
list = input ("Enter the list: ")

for j in range(len(list)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(list)-1:
        #comparing the adjacent elements
        if list[i]>list[i+1]:
            #swapping
            list[i],list[i+1] = list[i+1],list[i]
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break
print (list)
#Copy the duplcate element in other list
def duplicate(k): 
    size = len(k) 
    list1 = [] 
    for i in range(size): 
        m = i + 1
        for j in range(m, size): 
            if k[i] == k[j] and k[i] not in list1: 
                list1.append(k[i]) 
    print("duplicate element in list1: ",list1)
duplicate(list)