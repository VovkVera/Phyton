
#if
#example_number = 14
#than
#sum_digits(example_number) = 5

#if
#example_number = 'gh'
#than
#sum_digits(example_number) = "Are you sure?"



def sum_digits(num):
    str_num = str(num)
    sumdig = 0
    for el in str_num:
        try:
            sumdig = sumdig + int(el)
        except: return 'Are you sure?'
    return sumdig



# list comprehension

def sum_digits2(num):
    try:
        sumdig = sum ( [ int(el) for el in  str(num) ])
        return sumdig
    except: return 'Are you sure?'
    

example_number = 1234


print(sum_digits2(example_number))
