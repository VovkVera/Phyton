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

#------------------------------------------------------------------------
  Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
    
# -------------------------  or ------------------------------------------
    def high_and_low(numbers): return " ".join(x(numbers.split(), key=int) for x in (max, min))

# -------------------------  or ------------------------------------------

def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

# -------------------------  or ------------------------------------------

def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))

# -------------------------  or ------------------------------------------

def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return "{} {}".format(max(n), min(n))

# -------------------------  or ------------------------------------------
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])

# -------------------------  or ------------------------------------------
def high_and_low(numbers):
    results = map(int, numbers.split())
    numbers = "%s %s" %(max(results), min(results))
    return numbers

# -------------------------  or ------------------------------------------
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"


#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
def is_isogram(string): return len(string) == len(set(string.lower()))

string = "aba"
print(is_isogram(string))

"""

Test.assert_equals(is_isogram("Dermatoglyphics"), True )
Test.assert_equals(is_isogram("isogram"), True )
Test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
Test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
Test.assert_equals(is_isogram("isIsogram"), False )
Test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )

"""


