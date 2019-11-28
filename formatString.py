#Hello John Doe. Your current balance is $53.44.


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % (data[0],data[1],data[2]))



#Your task is to write a function which returns the sum of following series upto nth term(parameter)
#Series: 1/1+(i*3) + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 
def series_sum(n):
    suma = 0
    
    for i in range(n):
        suma+=  1/(1+ i*3)
        
    s = "%.2f"%suma
    return s
    
print(series_sum(3))

#orrrrrrrr

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

#--------------------------------------  
 
def toJadenCase(string):
    """
    u = string[0].upper()
    string = u + string[1:]
            
    for i in range(len(string)-1):
        if string[i] == " ":
            print(i)
            u = string[i+1].upper()
            string = string[:(i+1)] + u + string[i+2:]
            
    return string
    """
    # or
    return " ".join(w.capitalize() for w in string.split())
    
    
print(toJadenCase("jow can mirrors "))
