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
  a = b =1
  for i in range(n):
     yield a
     a, b = b, a + b

print(sum(fibonacci(100)))
