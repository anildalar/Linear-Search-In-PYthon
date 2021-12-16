searchFor = input("Please enter the character ")
list = ['A','B','C','D','E','F',"G","H",'I','J','K','L','M','N','O']

count  = len(list)

print(count)

# Global Varible
isFound = False

indexNo = ''
# define the function
def linearSearch(l,sfor):
    global indexNo
    # We will create a local variable
    #print(type(sfor))
    #pass
    for x in range(len(l)):
        #print(type(x))
        if(l[x] == sfor):
            indexNo = x
            return True
    return False
            
    #print(x)
# Call the function


print(indexNo)

if(linearSearch(list,searchFor)):
    print("Yes {}, is Availabe in List at index no {}".format(searchFor,indexNo))
else:
    print("No {}, is Not Availabe in List".format(searchFor))
    