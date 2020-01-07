
#if
#list_example = [1,4,4,2,1]
#than
#containn_dublicate(list_example) = True
#if
#list_example = [1,3,2,4571]
#than
#containn_dublicate(list_example) = False

def containn_dublicate(l):
    return len(l) != len(set(l))
    

list_example = [1,3,2,4571]
print(containn_dublicate(list_example) )
