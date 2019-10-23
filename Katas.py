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
