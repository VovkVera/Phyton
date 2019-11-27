# Write Number in Expanded Form
def expanded_form(num):
    exp = len(str(num))-1
    expand = str(int(str(num)[0])*(10**exp))
    t = num - int(expand)
    if exp>0 and t>0: expand += " + " + str(expanded_form(t))
    return expand
    
print(expanded_form(70300))



def expanded_form2(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
    
    
print(expanded_form2(70300))


def expanded_form3(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)
    
    
print(expanded_form3(70300))


"""

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

https://www.codewars.com/kata/write-number-in-expanded-form/python

"""