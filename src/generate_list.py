import random
def generate_list():
     alist = [x for x in range (random.randint(-10, 10))]
     assert len(alist) != 0 ,"the list must empty"
     assert sum(alist) > -100, "sum of list must < -100"
     return alist
     
"""
print a generate list
"""
def printIt():
    print (generate_list() )
    
def main():
    printIt()
    
"""
If this script file is called, it will run main() directly
"""  
if __name__=='__main__':
    print("Test printIT():" )
    main()
    

    