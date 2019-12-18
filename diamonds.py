def diamond(n):
    if n%2 ==0 or n<=0:
        return None
    else:
        di = "*"*n+"\n"
        for i in range(n-2, 0, -2):
            di = " "*int((n-i)/2) + "*"*i + "\n" + di + " "*int((n-i)/2) + "*"*i + "\n"
    return di
    
print(diamond(15))   
    

# range(stop) 
# range(start, stop) 
# range(start, stop, step)

#    test.assert_equals(diamond(1), "*\n")
#test.assert_equals(diamond(2), None)
#test.assert_equals(diamond(3), expected)
#Test.assert_equals(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
#test.assert_equals(diamond(0), None)
#test.assert_equals(diamond(-3), None)

"""
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\ n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size."""
