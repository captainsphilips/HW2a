def Reverse_list(list):
    myList = list[::-1]
    #return myList
    
    
list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    list.append(item)
#print("User list is ", list)    
    
    
    
list = []
list.extend([12, 35, 5, 9, 56, 24])
#print(Reverse_list(list))
