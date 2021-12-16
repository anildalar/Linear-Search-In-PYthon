searchFor = input("Please enter the character ")
list = ['A','B','C','D','E','F',"G","H",'I','J','K','L','M','N','O']

count  = len(list)

print(count)

# Global Varible
isFound = False
# define the function
def linearSearch(l,sfor):
    # We will create a local variable
    #print(type(sfor))
    #pass
    for x in l:
        #print(type(x))
        if(x == sfor):
            return True
    
    return False
            
    #print(x)
# Call the function


if(linearSearch(list,searchFor)):
    print("Yes {}, is Availabe in List".format(searchFor))
else:
    print("No {}, is Not Availabe in List".format(searchFor))
    