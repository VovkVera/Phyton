def fibo(n):
   f=1
   i=1
   a=[1,1]
   while i<n-1:
      f=f+a[i-1]
      a.append(f)
      i=i+1
   return a
      
n = int(input())
if n>1:
  print(fibo(n))
elif n==1:
  print([1])
else:
  print("please let your number be more then 1")


# or
def fibonacci(n):
     
  a = b = 1
  fibo_arr = [a]
  for i in range(n-1):
     a, b = b, a + b
     fibo_arr.append(a)
  return fibo_arr
     
print(fibonacci(10))
