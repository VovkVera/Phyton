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
#In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
#At the end of the first year there will be: 
#1000 + 1000 * 0.02 + 50 => 1070 inhabitants

def nb_year(p0, percent, aug, p):
    years = 0
    while p0<p:
        years +=1
        p0+= p0*percent/100 + aug
        print(p0)
    return years
    
print(nb_year(1500000, 2.5, 10000, 2000000))

#--------------- or
def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years


def xo(s):
    amountX = 0
    amountO = 0
    for i in s:
        if i == 'x' or i == 'X':
            amountX += 1
        if i == 'o' or i == 'O':
            amountO += 1
    return amountX == amountO
    
    # or ???? чуть сомнительно (не все поддерживают count ... проверить)
    return s.lower().count("x") == s.lower().count("o")
print(xo("xooxx"))
