#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
def high_and_low(numbers):
    # ...
    listofNumbers = numbers.split()
    listInt = []
    for n in listofNumbers:
        i = int(n)
        listInt.append(i)
    numbers = str(max(listInt))   + " " + str(min(listInt))
    return numbers    
  Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
